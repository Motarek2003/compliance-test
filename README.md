# compliance-test

Test repository for **CloudSentry / Cloud2Comply** GitHub external integration.

## Purpose

This repo is scanned by the CloudSentry compliance scanner to validate the GitHub
external integration end-to-end:

| Check | What it verifies |
|---|---|
| Secret scanning | No leaked credentials in code |
| Branch protection (`main`) | At least 1 review + status checks required |
| Dependabot | Dependency vulnerabilities tracked |
| Code scanning (CodeQL) | Static analysis enabled |
| Change tickets | Approved PRs serve as change records |

## Files

- `.github/workflows/codeql.yml` — enables GHAS code scanning
- `.github/dependabot.yml` — Dependabot config for pip, npm, GitHub Actions
- `requirements.txt` — Python dependencies (Dependabot target)
- `package.json` — Node dependencies (Dependabot target)

## Required GitHub Settings

Enable in **Settings → Code security and analysis**:

- Dependabot alerts
- Dependabot security updates
- Secret scanning
- Code scanning (CodeQL via Actions)

Enable in **Settings → Branches → Branch protection rules** for `main`:

- Require a pull request before merging
- Require approvals (minimum 1)
- Require status checks to pass before merging
