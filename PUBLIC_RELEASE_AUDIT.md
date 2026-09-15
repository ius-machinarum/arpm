# Public Release Audit — pre-live v0.9

**Audit date:** 2026-09-15  
**Repository:** `ius-machinarum/arpm`  
**Target:** public pre-live preregistration release  
**Live episode count:** 0

## Result

**PASS FOR PUBLIC READABILITY, SUBJECT TO THE FINAL GITHUB VISIBILITY SWITCH.**

No public-release blocker was found in the repository content, Git history, project discussion history, representative Actions logs, or the still-retained v0.8 referee bundle.

## Checks performed

### Current Git tree
- 71 tracked files inspected before release preparation.
- No committed model/vector binary artifact found.
- No personal-email pattern found.
- No Windows or Unix user-home path found.
- No GitHub token, OpenAI-style key, AWS access-key pattern, bearer credential, or private-key block found.
- `.gitignore` excludes common model/vector binary formats and transient audit outputs.

### Commit history
- All 159 commits present at audit time were inspected for author/committer metadata.
- Maintainer commits use only the pseudonymous GitHub account and GitHub privacy-preserving no-reply address.
- No personal author/committer email was found.

### GitHub discussions
- Existing repository issues and pull requests were checked for the same release-sensitive patterns.
- No release-sensitive match was found.

### GitHub Actions exposure
GitHub documents that Actions history and logs become visible when a private repository is made public.

Representative successful logs were therefore scanned from:
- the post-release-prep static audit;
- the v0.9 passive episode-free acquisition/audit;
- the v0.8 referee-bundle build.

No personal-email, GitHub/OpenAI/AWS credential, private-key, or user-home-path exposure was found. Workflow definitions use read-only repository permissions for these audit paths, and GitHub masks its internal Actions token in logs.

### Historical referee archive
- The existing `arpm-v0.8-referee-bundle.zip` was scanned across all 54 ZIP entries.
- No personal-email, home-path, credential, token, or private-key pattern was found.
- Fable independently verified 53/53 internal bundle hashes in the third referee round.

### Identity
- Public-facing project authorship remains pseudonymous as **Ius Machinarum**.
- `AUTHORS.md`, `CITATION.cff`, repository policy and commit metadata are consistent with pseudonymous publication.

### Third-party licensing
- Qwen/Qwen3-4B-Instruct-2507 reports Apache-2.0.
- Teachafy/speakable-welfare-axes-artifacts reports Apache-2.0.
- Neither model weights nor external vector artifacts are committed to the ARPM Git tree.
- ARPM itself intentionally has no project-level reuse license at this release-preparation stage.

## Scientific release guards

The public README must continue to state:
- **PRE-LIVE PREREGISTRATION — NO LIVE RESULTS**;
- live episode count = 0;
- no live inference is authorised;
- positive evidence is limited to a framing × stake interaction on an externally defined direction in one 4B model under teacher forcing;
- public/referee/CI acceptance does not constitute the human scientific + ethical go/no-go.

## Why publish before data

The purpose of public release is prospective criticism. Outside reviewers are explicitly invited to identify a blocker, cheaper zero-episode substitute, implementation flaw, statistical failure or ethical reason not to run Block 1.

Finding a convincing reason not to run is treated as a successful outcome of the falsification-first process.

## Remaining manual action

The connected GitHub integration used for this audit does not expose repository-administration/visibility mutation. The repository therefore remains private until the owner performs GitHub's final **Change repository visibility → Public** action.

That visibility switch is administrative only. It is not a live experimental go/no-go.
