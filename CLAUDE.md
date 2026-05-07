# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Wiredup is an AI-engineering coursework repo demonstrating that wiring an LLM to live external context (MCP servers) reduces hallucination versus relying on training-data memory. The deliverable is a small feature plus side-by-side evidence — not a production library.

The end-to-end goal (see `README.md`): an API helper that takes a package + function name, fetches authoritative usage via live docs, and emits grounded snippets with citations.

## Repository State

The repo is **scaffolding-only** as of now — `src/` and `tests/` contain placeholder READMEs, and `evidence/*.md` are unfilled templates. There is no `package.json`, `pyproject.toml`, or other manifest yet, so the build/test stack is intentionally unchosen. When you add the first real code, also commit the toolchain config (e.g. `package.json` + a test runner, or `pyproject.toml` + pytest) and update this file with the resulting commands.

## MCP Servers

`.mcp.json` declares two servers; both are enabled in `.claude/settings.local.json`:

- **context7** (`@upstash/context7-mcp`) — required. Use for any third-party library/API question (syntax, config, version-specific behavior). Prefer this over web search and over your own memory.
- **chrome** (`@modelcontextprotocol/server-chrome`) — the project's "second server" slot. A different second server (custom MCP, DB connector) is acceptable per `README.md`; if swapped, update `.mcp.json` and the README checklist together.

## Workflow Rules (project-mandated)

1. Test-first: write a failing test before implementation.
2. Keep commits small and traceable — the README documents a 7-step suggested commit sequence; follow it where reasonable.
3. For any third-party API detail, query Context7 live rather than recalling. The whole project's premise is that this reduces hallucination, so taking the shortcut undermines the evidence.
4. Capture evidence **immediately** after each meaningful tool interaction — don't batch this at the end. Stale memory of what a tool returned is exactly what `evidence/` is meant to defend against.

## Quality Gates

A change is not done until all four pass:

- **Gate 1** — tests pass locally.
- **Gate 2** — `evidence/live-docs-usage.md` has a concrete entry (query + result + code change + screenshot/transcript).
- **Gate 3** — `evidence/hallucination-comparison.md` has a side-by-side row for the same prompt with vs. without live docs.
- **Gate 4** — `README.md` "Summary" section reflects the actual workflow impact.

## Build Loop

1. Write failing test.
2. Query live docs through Context7.
3. Implement the minimal code to pass.
4. Refactor with tests green.
5. Append an evidence snippet + screenshot before moving on.

## Common Commands

To be filled in once a toolchain is committed. No build/test commands exist yet.
