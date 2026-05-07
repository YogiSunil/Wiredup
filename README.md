# Wiredup

Connect dev tools to live external context so AI output is grounded in current information.

## Goal

This project demonstrates:
- 2+ protocol server integrations
- live documentation usage during feature work
- side-by-side hallucination comparison
- test-first implementation of a real feature

## Protocol Servers

- [ ] Context7 (required)
- [ ] Second server (choose one): Chrome MCP, database connector, or custom MCP server
- [ ] Optional third server (stretch)

## Project Checklist

### V1.0 - Configuration and Live Docs

- [ ] Configure at least 2 protocol servers
- [ ] Build a feature that uses a third-party library API
- [ ] Capture evidence of live docs queries
- [ ] Fill evidence/live-docs-usage.md
- [ ] Add, commit, and push

### V1.1 - Second Integration

- [ ] Use second protocol server in real development
- [ ] Document workflow impact in this README and evidence docs
- [ ] Add, commit, and push

### V1.2 - Hallucination Comparison and Polish

- [ ] Compare output with vs without live docs for the same API call
- [ ] Fill evidence/hallucination-comparison.md side-by-side
- [ ] Complete feature with test-first workflow
- [ ] Add architecture notes/design doc links
- [ ] Add, commit, and push

## Feature Idea (Fastest Path)

Build a small API helper command that:
- reads a package name and function name
- fetches authoritative usage guidance via live docs
- generates grounded code snippets with citations to docs lookup results

## Suggested Commit Sequence

1. chore: scaffold wiredup repo structure and docs
2. chore: configure context7 and second mcp server
3. test: add failing tests for feature behavior
4. feat: implement feature using live docs queries
5. docs: add live docs evidence and screenshots
6. docs: add hallucination comparison with and without live docs
7. docs: polish readme summary and next steps

## Summary (to complete before submission)

- Servers used:
- How they changed workflow:
- Biggest reduction in hallucination risk:
- Next improvements:
