from __future__ import annotations

from src import app


def test_main_success(monkeypatch, capsys):
    monkeypatch.setattr(
        app,
        "fetch_user",
        lambda username: {
            "login": username,
            "name": "Demo User",
            "public_repos": 3,
            "followers": 2,
            "following": 1,
            "html_url": "https://github.com/demo",
        },
    )

    exit_code = app.main(["demo"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "Login: demo" in output
    assert "Public repos: 3" in output


def test_main_failure(monkeypatch, capsys):
    monkeypatch.setattr(app, "fetch_user", lambda username: {"error": "User not found"})

    exit_code = app.main(["missing"])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "Error: User not found" in output
