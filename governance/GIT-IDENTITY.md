# Git attribution and email privacy

## Current publication status (November 6, 2026)

The repository is public under the verified `drgf2y7cb7-afk` account. Its published commits use GitHub-managed attribution with an account-specific noreply address. Repository housekeeping does not configure a local or global Git email or substitute the public benchmark contact. Local commits in future still require a verified account-specific noreply identity.

## Historical package-preparation record (November 5, 2026)

Approved author: **Jaime Lawson**, Founder & Research Lead, Phoenix Applied Technologies.

The earlier v3 candidate has a local-only staging repository; the v4 contact and v5 license updates did not initialize another repository or change Git settings. Its local `user.name` is `Jaime Lawson` and local `user.useConfigOnly` is `true`. No email is configured, so Git cannot currently produce a complete author identity. No commits, remotes or public repository were created. Global Git identity was not changed. The downloadable ZIP excludes `.git`; these local settings therefore do not travel with the archive.

For a future local checkout, these commands apply only inside that repository:

```bash
git config --local user.name "Jaime Lawson"
git config --local user.useConfigOnly true
```

The remaining step is to obtain the **actual account-specific GitHub noreply address** from the approved account's Settings > Emails, confirm the account belongs to Jaime and use that address as the repository-local `user.email`. No address has been guessed or configured here. The parent verified the connected GitHub login; repository-creation capability in this executor and the actual account-specific noreply value remain unconfirmed. Review any final commit's author/committer fields before publishing; keep checks that display the address private.

[GitHub's commit-email guidance](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) explains repository-local identity and GitHub-provided noreply addresses. Email privacy protections and accidental-email publication checks should be enabled in the verified account. The public benchmark contact is expressly approved in [CONTACT.md](CONTACT.md). That address is not authorized for Git commit attribution and has not been configured as a Git email.
