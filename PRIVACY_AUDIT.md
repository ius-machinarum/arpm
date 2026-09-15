# Pseudonymity / Privacy Audit

**Repository:** `ius-machinarum/arpm`  
**Maintainer identity:** `Ius Machinarum`  
**Release target:** public pre-live preregistration  
**Audit date:** 2026-09-15

## Current release audit

The repository was re-audited immediately before public-release preparation.

### Git history
- 159 commits inspected.
- Maintainer commit identity is pseudonymous.
- Maintainer email is GitHub's privacy-preserving `users.noreply.github.com` address.
- GitHub-generated merge commits use `noreply@github.com`.
- No personal author/committer email was found.

### Current tracked tree
- 71 tracked files inspected before release-prep edits.
- No personal-email pattern found.
- No local Windows user-home path found.
- No `/home/<user>/` path found.
- No GitHub token, OpenAI-style key, AWS access-key pattern, bearer credential, or private-key block found.
- No model/vector binary artifact is committed.

### Repository discussions
Existing issues and pull requests were scanned for the same release-sensitive patterns. No match was found.

### Historical referee bundle
The existing v0.8 referee ZIP was scanned across all 54 entries. No personal-email, home-path, token, credential, or private-key pattern was found.

### Preventive controls
- `.gitignore` excludes common model/vector binary formats and transient audit outputs.
- `public_release_audit.py` now performs a repeatable current-tree privacy/status guard in CI.
- `README.md` must retain the pre-live/no-live-results banner and episode count 0.
- Project authorship remains pseudonymous as **Ius Machinarum**.

## Third-party artifacts

Model weights and external vector artifacts are not committed to the Git repository.

Public-release licensing/provenance is documented in `THIRD_PARTY_LICENSES.md`.

## Limitation

This audit substantially reduces accidental disclosure risk but cannot guarantee anonymity against external correlation or information outside this repository.

The connected GitHub integration does not expose repository-visibility administration, so the final private→public switch remains a separate owner-side GitHub action.
