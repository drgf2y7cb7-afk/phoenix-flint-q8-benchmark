#!/usr/bin/env python3
"""Audit saved measurements and regenerate tables offline. Never calls a model or service."""
from pathlib import Path
import argparse, csv, hashlib, io, json, math

ROOT=Path(__file__).resolve().parents[1]
E=ROOT/'evidence'
def read(p): return json.loads(p.read_text())
def lines(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
rows=[]; checks=[]
def check(label, ok):
    checks.append({'check':label,'pass':bool(ok)})
    if not ok: raise AssertionError(label)
def near(a,b):return math.isclose(a,b,rel_tol=1e-8,abs_tol=.011)
def add(group,m,gpu,backend,temp_status='reported; UI application unverified',exclude=''):
    name=m['profile'];v=m['last_sample'];d=E/group
    data=lines(d/'samples.jsonl')
    sends=lines(d/('send-times.jsonl' if group=='dual-gpu-coding' else 'sends.jsonl'))
    ix=next(i for i,s in enumerate(sends) if s['profile']==name)
    event=sends[ix];end=sends[ix+1]['unix'] if ix+1<len(sends) else float('inf')
    ss=[s for s in data if event['unix']<=s['unix']<end and s.get('profile')==name]
    active=[s for s in ss if s.get('health',{}).get('live')]
    last=active[-1];live=last['health']['live'][0]
    idle=next((s for s in ss if s['unix']>last['unix'] and s.get('health',{}).get('scheduler',{}).get('active')==0),None)
    check(group+'/'+name+' last sampled decode rate',v['tok_s']==live['tok_s'])
    check(group+'/'+name+' sampled token count',v['tokens']==live['tokens'])
    check(group+'/'+name+' completion bracket',near(m['completion_lower_s'],round(last['unix']-event['unix'],2)) and idle is not None and near(m['completion_upper_s'],round(idle['unix']-event['unix'],2)))
    prof=d/(name+'-profile.json')
    p=read(prof)['turns'][-1] if prof.exists() else None
    conv=d/(name+'-conversation.json')
    finish='unknown'
    if conv.exists():
        c=read(conv);assistant=[x for x in c.get('messages',[]) if x.get('role')=='assistant'];finish=assistant[-1].get('finish','unknown') if assistant else 'unknown'
    isfull=finish=='stop'
    temp=event.get('temperature_verified',event.get('temperature','not in event'))
    if group=='dual-gpu-coding':temp=read(d/'protocol.json')['temperature'];temp_status='protocol-reported; request payload unavailable'
    row={'run_id':group+'/'+name,'gpu_inference':gpu,'backend':backend,'workload':'async-cache repair' if group=='dual-gpu-coding' else 'insulation explanation','kind':'full response' if isfull else 'short screen' if finish=='length' else 'see evidence','finish':finish,'temperature_recorded':temp,'temperature_evidence':temp_status,'output_limit':event.get('max_tokens',6144 if group in {'prefill-cache-1080ti','gpu-role-1080ti','dual-gpu-coding'} else ''),'tokens_per_second':round(p['completion_tokens']/p['wall_s'],9) if p else v['tok_s'],'rate_method':'completed tokens / decode-loop seconds' if p else 'last active cumulative health average','tokens':p['completion_tokens'] if p else v['tokens'],'token_count_method':'completed profile' if p else 'last live sample; incomplete count','decode_seconds':p['wall_s'] if p else '', 'prompt_seconds':v['read_s'],'send_to_completion_lower_s':m['completion_lower_s'],'send_to_completion_upper_s':m['completion_upper_s'],'peak_rss_gib_metric_window':m['max_rss_gib'],'status':exclude or ('preliminary; unrepeated short screen' if group=='tuned-1080ti' and name=='cuda-auto' else 'observed; workload-specific'),'source':str((prof if p else d/'metrics.json').relative_to(ROOT)),'raw_samples':str((d/'samples.jsonl').relative_to(ROOT))}
    rows.append(row)

for group in ['early-backends-1070','thread-cache-1070','split-8020-1070','initial-1080ti','tuned-1080ti','prefill-cache-1080ti','gpu-role-1080ti','dual-gpu-coding']:
    for m in read(E/group/'metrics.json'):
        n=m['profile'];backend='Vulkan' if n.startswith(('vulkan','t8-','t6-','t4-')) else 'CUDA'
        gpu='RTX 4060 + GTX 1070' if group.endswith('1070') else 'RTX 4060 + GTX 1080 Ti'
        if group=='early-backends-1070' and n in {'cuda-baseline','vulkan'}:gpu='RTX 4060 only'
        excluded=''
        if group=='initial-1080ti':excluded='excluded from clean comparison: desktop GPU load'
        if group=='tuned-1080ti' and n=='cuda-matched':excluded='excluded from clean comparison: concurrent 176B service'
        if group=='prefill-cache-1080ti' and n=='cache-off':excluded='excluded from matched comparison: UI temperature remained 0.7'
        temp_status='verified visible label 0.0' if group in {'prefill-cache-1080ti','gpu-role-1080ti'} and not excluded else 'reported; UI application unverified'
        add(group,m,gpu,backend,temp_status,excluded)

# The five targeted quality cases retain multi-turn dependence and their own timing schema.
d=E/'quality-cases';metrics=read(d/'metrics.json');events=lines(d/'send-events.jsonl');ss=lines(d/'health-samples.jsonl')
for i,m in enumerate(metrics['cases']):
    ev=events[i];end=events[i+1]['unix'] if i+1<len(events) else float('inf')
    samples=[s for s in ss if ev['unix']<=s['unix']<end];active=[s for s in samples if s.get('health',{}).get('live')];last=active[-1]
    check('quality/'+m['case']+str(m['turn'])+' rate',last['health']['live'][0]['tok_s']==m['average_generation_tokens_per_second'])
    r=dict.fromkeys(rows[0],'')
    r.update(run_id='quality-cases/'+m['case']+'/'+str(m['turn']),gpu_inference='RTX 4060 only',backend='CUDA',workload=m['case'],kind='full response',finish=m['finish'],temperature_recorded=1,temperature_evidence='reported visible setting',output_limit=6144,tokens_per_second=m['average_generation_tokens_per_second'],rate_method='last active cumulative health average',tokens=m['last_sample_tokens'],token_count_method='last live sample; incomplete count',prompt_seconds=m['first_token_approx_seconds'],send_to_completion_lower_s=m['completion_lower_seconds'],send_to_completion_upper_s=m['completion_upper_seconds'],peak_rss_gib_metric_window=metrics['peak_engine_rss_gib'],status='targeted quality case; follow-ups not independent',source='evidence/quality-cases/metrics.json',raw_samples='evidence/quality-cases/health-samples.jsonl')
    rows.append(r)

d=E/'single-gpu-coding';m=read(d/'results.json');ss=lines(d/'final-resource-samples.jsonl')
check('single GPU code rate and token count in raw samples',any(s.get('health',{}).get('live') and s['health']['live'][0]['tok_s']==m['last_sampled_decode_tokens_per_second'] and s['health']['live'][0]['tokens']==m['last_sampled_completion_tokens'] for s in ss))
r=dict.fromkeys(rows[0],'');r.update(run_id='single-gpu-coding/completed',gpu_inference='RTX 4060 only',backend='CUDA',workload='async-cache repair',kind='full response',finish='stop',temperature_recorded=1,temperature_evidence='reported visible setting',output_limit=6144,tokens_per_second=m['last_sampled_decode_tokens_per_second'],rate_method='last active cumulative health average',tokens=m['last_sampled_completion_tokens'],token_count_method='last live sample; incomplete count',prompt_seconds=m['prompt_read_seconds'],send_to_completion_lower_s=m['completion_time_seconds_bounds'][0],send_to_completion_upper_s=m['completion_time_seconds_bounds'][1],peak_rss_gib_metric_window=m['engine_rss_peak_GiB'],status='repeated prompt after initial 2048-token truncation; send timestamp not found as separate event',source='evidence/single-gpu-coding/results.json',raw_samples='evidence/single-gpu-coding/final-resource-samples.jsonl');rows.insert(0,r)

# Independently check the repeated full-response baseline text and its exact arithmetic.
a=read(E/'prefill-cache-1080ti/cache-off-zero-conversation.json')['messages'][-1]
b=read(E/'gpu-role-1080ti/4060-primary-conversation.json')['messages'][-1]
check('full baseline repeated final answer and reasoning match',a['content']==b['content'] and a.get('reasoning')==b.get('reasoning'))
for group,n in [('prefill-cache-1080ti','cache-off-zero'),('prefill-cache-1080ti','cache-on'),('gpu-role-1080ti','4060-primary'),('gpu-role-1080ti','ti-primary')]:
    p=read(E/group/(n+'-profile.json'))['turns'][-1];c=read(E/group/'comparison.json')[n]
    check(group+'/'+n+' recorded completed rate',near(p['completion_tokens']/p['wall_s'],c['tokens_per_second']))

with (ROOT/'data/evidence-manifest.csv').open() as f:
    for ent in csv.DictReader(f):
        p=ROOT/ent['public_path'];check('SHA256 '+ent['public_path'],hashlib.sha256(p.read_bytes()).hexdigest()==ent['public_sha256'])

out=io.StringIO();w=csv.DictWriter(out,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
md=['# Complete run ledger','', 'Rates include reasoning. Sampled health rates are not exact completed-run rates. See METHODS.md for timing boundaries and LIMITATIONS.md for temperature and cache caveats. Each row is one recorded run or case; no aggregate accuracy is implied.','', '| Run | GPUs | Backend | Type | tok/s | Complete/send bracket (s) | Status |','|---|---|---|---|---:|---:|---|']
for r in rows:
    md.append(f"| `{r['run_id']}` | {r['gpu_inference']} | {r['backend']} | {r['kind']} | {r['tokens_per_second']:.3f} | {r['send_to_completion_lower_s']:.2f}–{r['send_to_completion_upper_s']:.2f} | {r['status']} |")
md.extend(['','CSV with token counts, prompt timings, measurement methods and evidence paths: [runs.csv](../data/runs.csv).',''])
verification=json.dumps({'status':'PASS','checks':len(checks),'run_rows':len(rows),'checks_detail':checks},indent=2)+'\n'
generated={ROOT/'data/runs.csv':out.getvalue(),ROOT/'docs/ALL-RUNS.md':'\n'.join(md),ROOT/'data/verification.json':verification}
if '--check' in __import__('sys').argv:
    for f,t in generated.items():check('generated file matches '+str(f.relative_to(ROOT)),f.read_text()==t)
else:
    for f,t in generated.items():f.write_text(t)
print(f'PASS: {len(rows)} measured run/case rows, {len(checks)} evidence/measurement checks. No inference executed.')
