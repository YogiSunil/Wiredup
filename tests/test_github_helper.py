from __future__ import annotations

import requests

from src.github_helper import fetch_user


class DummyResponse:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict:
        return self._payload


def test_fetch_user_success(monkeypatch):
    def fake_get(url, headers, timeout):
        assert "octocat" in url
        assert headers["Accept"] == "application/vnd.github+json"
        assert timeout == 10.0
        return DummyResponse(
            200,
            {
                "login": "octocat",
                "name": "The Octocat",
                "public_repos": 8,
                "followers": 100,
                "following": 0,
                "html_url": "https://github.com/octocat",
            },
        )

    monkeypatch.setattr("src.github_helper.requests.get", fake_get)

    result = fetch_user("octocat")
    assert result["login"] == "octocat"
    assert result["public_repos"] == 8


def test_fetch_user_not_found(monkeypatch):
    def fake_get(url, headers, timeout):
        return DummyResponse(404, {})

    monkeypatch.setattr("src.github_helper.requests.get", fake_get)

    result = fetch_user("missing-user")
    assert result == {"error": "User not found"}


def test_fetch_user_network_error(monkeypatch):
    def fake_get(url, headers, timeout):
        raise requests.RequestException("network down")

    monkeypatch.setattr("src.github_helper.requests.get", fake_get)

    result = fetch_user("octocat")
    assert result == {"error": "Network request failed"}
