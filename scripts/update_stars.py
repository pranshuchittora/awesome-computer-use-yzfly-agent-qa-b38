#!/usr/bin/env python3
"""Refresh public GitHub Star counts using gh; write only after every fetch succeeds."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from render_readme import ROOT, load_catalog


def fetch_repository(repo):
    result = subprocess.run(
        ["gh", "api", "--hostname", "github.com", f"repos/{repo}", "--jq",
         "{full_name, stargazers_count, private, archived}"],
        capture_output=True, text=True, timeout=40,
    )
    if result.returncode:
        raise ValueError(f"{repo}: GitHub API failed; check authentication, rate limits, and repository visibility")
    data = json.loads(result.stdout)
    if data["private"]:
        raise ValueError(f"{repo}: refusing to publish private-repository metadata")
    if data["full_name"].lower() != repo.lower():
        raise ValueError(f"{repo}: repository moved to {data['full_name']}; update catalog and sources first")
    count = data["stargazers_count"]
    if type(count) is not int or count < 0 or type(data["archived"]) is not bool:
        raise ValueError(f"{repo}: invalid GitHub response")
    return repo, {"stars": count, "archived": data["archived"]}


def main():
    temporary = None
    try:
        repos = sorted({item["repository"] for item in load_catalog()}, key=str.casefold)
        with ThreadPoolExecutor(max_workers=6) as pool:
            stats = dict(pool.map(fetch_repository, repos))
        snapshot = {
            "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "source": "GitHub REST API /repos/{owner}/{repo}: stargazers_count",
            "repositories": stats,
        }
        destination = ROOT / "data/github-stars.json"
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent,
                                         prefix=".github-stars-", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
        os.replace(temporary, destination)
        archived = [repo for repo, meta in stats.items() if meta["archived"]]
        print(f"Updated {len(stats)} repositories at {snapshot['updated_at']}")
        if archived:
            print("Review archived repositories: " + ", ".join(archived))
        print("Next: python3 scripts/render_readme.py")
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f"Error: {exc}. Previous Star snapshot preserved.", file=sys.stderr)
        return 1
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


if __name__ == "__main__":
    raise SystemExit(main())
