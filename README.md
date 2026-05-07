# Wiredup

Connect dev tools to live external context so AI output is grounded in current information.

## Goal

This project demonstrates:
- 2+ protocol server integrations
- live documentation usage during feature work
- side-by-side hallucination comparison
- test-first implementation of a real feature

## Protocol Servers

- [x] Context7 (required)
- [x] Second server: Chrome MCP
- [ ] Optional third server (stretch)

## Project Checklist

### V1.0 - Configuration and Live Docs

- [x] Configure at least 2 protocol servers
- [x] Build a feature that uses a third-party library API
- [x] Capture evidence of live docs queries
- [x] Fill evidence/live-docs-usage.md
- [x] Add, commit, and push

### V1.1 - Second Integration

- [x] Use second protocol server in real development
- [x] Document workflow impact in this README and evidence docs
- [x] Add, commit, and push

### V1.2 - Hallucination Comparison and Polish

- [x] Compare output with vs without live docs for the same API call
- [x] Fill evidence/hallucination-comparison.md side-by-side
- [x] Complete feature with test-first workflow
- [x] Add architecture notes/design doc links
- [x] Add, commit, and push

## Implemented Feature (Step 1)

Build a small GitHub profile helper command that:
- accepts a GitHub username
- calls GitHub REST API with `requests`
- prints a normalized profile summary
- returns safe error messages for not-found and network-failure cases

Run it:

```bash
python -m src.app octocat
```

Run tests:

```bash
pytest -q
```

## Suggested Commit Sequence

1. chore: scaffold wiredup repo structure and docs
2. chore: configure context7 and second mcp server
3. test: add failing tests for feature behavior
4. feat: implement feature using live docs queries
5. docs: add live docs evidence and screenshots
6. docs: add hallucination comparison with and without live docs
7. docs: polish readme summary and next steps

## Architecture Notes

- Data flow: CLI input -> GitHub helper -> API call -> normalized output.
- Reliability strategy: explicit timeout, 404 handling, and generic 4xx/5xx fallback reduce runtime surprises.
- Verification strategy: unit tests plus live-doc evidence and hallucination comparison docs.

Design references:
- `src/github_helper.py`
- `src/app.py`
- `tests/test_github_helper.py`
- `tests/test_app.py`
- `evidence/live-docs-usage.md`
- `evidence/hallucination-comparison.md`

## Summary (to complete before submission)

- Servers used: Context7 and Chrome MCP.
- How they changed workflow: Context7 provided authoritative API behavior before coding, and Chrome MCP remains available for UI/browser verification tasks.
- Biggest reduction in hallucination risk: Live docs prevented incorrect assumptions about requests timeout/exception handling and GitHub users endpoint response behavior.
- Next improvements: Add a third MCP integration (database or custom tool), improve comparison coverage with additional no-doc vs with-doc scenarios, and expand automated tests.
