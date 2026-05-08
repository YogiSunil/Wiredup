# Live Docs Usage Evidence

Document real moments where live documentation changed implementation decisions.

## Entry Template

### Task

What were you trying to build?

### Live Docs Query

What did you query in Context7?

### Result Used

What exact API behavior/signature/pattern did you use?

### Code Change

Which files changed and why?

### Evidence

- Screenshot path:
- Transcript/log excerpt:

## Entries

### Entry 1

- Task: Implement a GitHub profile lookup helper using a third-party HTTP client in Python.
- Live Docs Query: "requests.get timeout usage and exception handling patterns"
- Result Used: Use `requests.get(url, headers=headers, timeout=timeout)` and catch `requests.RequestException` for network-layer failures.
- Code Change: Updated [wiredup/src/github_helper.py](wiredup/src/github_helper.py) to include explicit timeout handling and a safe error response (`{"error": "Network request failed"}`) instead of crashing.
- Evidence:
	- Screenshot path: evidence/screenshots/context7-requests-timeout.png
	- Transcript/log excerpt: "Context7 docs confirmed timeout parameter support and recommended RequestException handling for robust client code."

### Entry 2

- Task: Normalize GitHub user API responses and handle missing-user scenarios in a predictable way for CLI output.
- Live Docs Query: "GitHub REST API users endpoint status codes and response fields"
- Result Used: `GET /users/{username}` returns `404` when user is missing, and profile payload includes keys like `login`, `name`, `public_repos`, `followers`, `following`, and `html_url`.
- Code Change: Added status-specific branches in [wiredup/src/github_helper.py](wiredup/src/github_helper.py) for 404 and 4xx/5xx responses; mapped JSON fields into a stable response schema used by [wiredup/src/app.py](wiredup/src/app.py).
- Evidence:
	- Screenshot path: evidence/screenshots/context7-github-users-endpoint.png
	- Transcript/log excerpt: "Context7 endpoint reference avoided guessing field names and prevented incorrect assumptions about not-found behavior."

### Entry 3

- Task: Verify GitHub users endpoint field names in a browser-driven integration step.
- Live Docs Query: "Chrome MCP open https://api.github.com/users/octocat and validate response keys used by the helper."
- Result Used: Confirmed that `login`, `name`, `public_repos`, `followers`, `following`, and `html_url` are present in live response payload.
- Code Change: No additional code changes were required; this step validated existing mapping behavior in [wiredup/src/github_helper.py](wiredup/src/github_helper.py).
- Evidence:
	- Screenshot path: evidence/screenshots/chrome-mcp-github-field-check.png
	- Transcript/log excerpt: "Browser-side API response inspection matched the fields consumed by the CLI formatter."

## Feature Validation Screenshots

- App run screenshot: evidence/screenshots/app-run-octocat.png
- Test pass screenshot: evidence/screenshots/tests-pass.png
