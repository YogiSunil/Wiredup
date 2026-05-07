"""CLI entrypoint for the Wiredup feature demo."""

from __future__ import annotations

import argparse
from typing import Sequence

from .github_helper import fetch_user


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch and print GitHub user profile data")
    parser.add_argument("username", help="GitHub username")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    user = fetch_user(args.username)
    if "error" in user:
        print(f"Error: {user['error']}")
        return 1

    print(f"Login: {user['login']}")
    print(f"Name: {user['name']}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Following: {user['following']}")
    print(f"Profile: {user['html_url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
