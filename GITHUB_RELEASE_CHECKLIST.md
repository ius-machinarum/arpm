# GitHub public-release checklist

## Completed before visibility change

- [x] Public-facing maintainer identity is pseudonymous: **Ius Machinarum**.
- [x] Commit history uses privacy-preserving GitHub no-reply email metadata.
- [x] Full current tracked tree scanned for personal-email, local-path, credential/token and private-key patterns.
- [x] All 159 commits present at audit time checked for author/committer email metadata.
- [x] Existing issues and pull requests checked for release-sensitive patterns.
- [x] Historical v0.8 referee ZIP scanned across all 54 entries.
- [x] No model weights or vector binaries are committed to the Git tree.
- [x] README prominently states **PRE-LIVE PREREGISTRATION — NO LIVE RESULTS**.
- [x] README and STATUS state episode count 0 and no live authorisation.
- [x] Episode-free tokenizer/vector/provenance audits pass.
- [x] Three adversarial referee rounds completed before live data.
- [x] Third-referee preregistration fixes frozen in v0.9.
- [x] Fresh literature re-check completed before human go/no-go.
- [x] Qwen and Teachafy external artifact sources checked as Apache-2.0.
- [x] Third-party licensing/provenance recorded in `THIRD_PARTY_LICENSES.md`.
- [x] Repeatable public-release privacy/status guard added to CI.
- [x] Redundant uppercase v0.6 referee-summary duplicate removed; full canonical report retained.
- [x] Project-level license decision made for this release: **no explicit ARPM reuse license yet**; public readability is not presented as reuse permission.
- [x] OSF archival decision made for this release: **not a prerequisite** to the pre-live public GitHub release; it may be added separately later.

## Final administrative action

- [ ] GitHub repository visibility changed from **Private** to **Public** by the repository owner.

The visibility switch is administrative only. It does not constitute the separate human scientific + ethical go/no-go and does not authorise live inference.
