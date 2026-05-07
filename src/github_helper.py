"""Helpers for querying GitHub API data."""

from __future__ import annotations

from typing import Any

import requests


GITHUB_USER_URL = "https://api.github.com/users/{username}"


def fetch_user(username: str, timeout: float = 10.0) -> dict[str, Any]:
    """Fetch key public profile fields for a GitHub user."""
    url = GITHUB_USER_URL.format(username=username)
    headers = {"Accept": "application/vnd.github+json"}

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
    except requests.RequestException:
        return {"error": "Network request failed"}

    if response.status_code == 404:
        return {"error": "User not found"}
    if response.status_code >= 400:
        return {"error": f"GitHub API error: {response.status_code}"}

    data = response.json()
    return {
        "login": data.get("login", ""),
        "name": data.get("name") or "(no public name)",
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
        "html_url": data.get("html_url", ""),
    }
