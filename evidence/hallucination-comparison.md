# Hallucination Comparison

Use the same prompt/API task in two conditions:
- without live docs
- with live docs (Context7 enabled)

## Scenario

- Library/API: GitHub REST API `GET /users/{username}` via Python `requests`.
- Prompt used: "Write a helper that fetches a GitHub user profile and prints name, repos, followers, and profile URL."

## Side-by-Side Results

| Condition | Output Summary | Correctness Notes |
|:--|:--|:--|
| Without live docs | Assumed not-found responses would still return JSON fields and attempted to map guessed keys without status checks. | Incorrect handling for missing users; could produce confusing output or key errors when response is not successful. |
| With live docs | Implemented explicit status handling (`404` -> `User not found`, `>=400` -> API error), network exception handling, and stable mapping for known response fields (`login`, `name`, `public_repos`, `followers`, `following`, `html_url`). | Correct and resilient behavior for success, missing-user, and network failure paths; aligned with documented endpoint behavior. |

## Analysis

- Key differences: The no-doc approach guessed API behavior, while the live-doc approach encoded documented status and payload expectations.
- Error reduction observed: Prevented one runtime class of failures for missing users and one for network interruption; also prevented incorrect field assumptions.
- Confidence impact: Higher confidence in correctness because implementation decisions were traceable to live API docs instead of memory-based guesses.

## Evidence

- Screenshot without live docs: evidence/screenshots/no-live-docs-github-helper-draft.png
- Screenshot with live docs: evidence/screenshots/context7-github-404-behavior.png
- Supporting transcript/log snippets:
	- "Without docs: tentative mapping and no clear 404 strategy."
	- "With Context7: confirmed users endpoint fields and status handling before coding."
