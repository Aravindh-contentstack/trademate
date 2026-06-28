#!/usr/bin/env python3
"""
Notion Trading Journal Sync
Pulls entries from your Notion database and saves them locally.

Run: python3 sync_notion.py
"""

import os
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).parent

PAIR_FOLDERS = {
    "eu": "eu", "eurusd": "eu",
    "xau": "xau", "xauusd": "xau", "gold": "xau",
}

DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "36d100a156ba80acaac7f4412c82b6cf")


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_text(rich_text):
    return "".join(t.get("plain_text", "") for t in (rich_text or []))


def prop(props, name, ptype):
    p = props.get(name)
    if not p:
        return None
    if ptype == "title":
        return get_text(p.get("title", [])) or None
    if ptype == "date":
        d = p.get("date")
        return d["start"] if d else None
    if ptype == "select":
        s = p.get("select")
        return s["name"] if s else None
    if ptype == "multi_select":
        items = p.get("multi_select", [])
        return ", ".join(i["name"] for i in items) if items else None
    if ptype == "rich_text":
        return get_text(p.get("rich_text", [])) or None
    if ptype == "number":
        return p.get("number")
    return None


def fetch_all_db_pages(client):
    db_id = DATABASE_ID.replace("-", "")
    pages, cursor = [], None
    while True:
        kwargs = {"filter": {"value": "page", "property": "object"}, "query": ""}
        if cursor:
            kwargs["start_cursor"] = cursor
        result = client.search(**kwargs)
        for p in result.get("results", []):
            if p.get("parent", {}).get("database_id", "").replace("-", "") == db_id:
                pages.append(p)
        if not result.get("has_more"):
            break
        cursor = result["next_cursor"]
    return pages


def download_image(url, path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            path.write_bytes(r.read())
        return True
    except Exception as e:
        print(f"    Warning: image download failed — {e}")
        return False


def localise_images(markdown, img_dir):
    """Download all images in markdown and replace with local relative paths."""
    pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    counter = [0]

    def replace(m):
        url = m.group(2)
        idx = counter[0]
        fname = "image.png" if idx == 0 else f"image {idx}.png"
        counter[0] += 1
        img_dir.mkdir(parents=True, exist_ok=True)
        save_path = img_dir / fname
        if download_image(url, save_path):
            return f"![image.png]({img_dir.name}/{fname.replace(' ', '%20')})"
        return m.group(0)

    return pattern.sub(replace, markdown)


def build_header(entry_num, date_str, pair, props):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    lines = [
        f"# {entry_num}",
        "",
        f"Date: {dt.strftime('%B %-d, %Y')}",
        f"Day: {dt.strftime('%A').upper()}",
        f"ATTENDANCE: {prop(props, 'ATTENDANCE', 'select') or 'UNKNOWN'}",
        f"Pair: {pair.upper()}",
        f"DAY RESULT: {prop(props, 'DAY RESULT', 'multi_select') or 'UNKNOWN'}",
    ]

    htf = prop(props, "HTF Strength", "number")
    if htf is not None:
        lines.append(f"HTF Strength: {htf * 100:.2f}%")

    narrative = prop(props, "Narrative Achieved", "select")
    if narrative:
        lines.append(f"Narrative Achieved: {narrative}")

    comments = prop(props, "Comments", "rich_text")
    if comments:
        lines.append(f"Comments: {comments}")

    lines.append("")
    return "\n".join(lines) + "\n"


# ── Main sync ─────────────────────────────────────────────────────────────────

def sync(client, force=False):
    print("Fetching entries from Notion…")
    pages = fetch_all_db_pages(client)
    print(f"Found {len(pages)} entries.\n")

    synced = skipped = errors = 0

    for page in pages:
        props = page["properties"]

        entry_num = prop(props, "Day No.", "title") or "?"
        date_str  = prop(props, "Date", "date")
        pair      = prop(props, "Pair", "select")

        day_result = prop(props, "DAY RESULT", "multi_select")
        if not day_result:
            continue

        if not date_str or not pair:
            print(f"  Skip '{entry_num}': missing date or pair")
            errors += 1
            continue

        folder_name = PAIR_FOLDERS.get(pair.lower().replace("/", ""))
        if not folder_name:
            print(f"  Skip '{entry_num}': unrecognised pair '{pair}'")
            errors += 1
            continue

        dt = datetime.strptime(date_str, "%Y-%m-%d")
        filename = f"{date_str}-{dt.strftime('%A')}.md"
        filepath = WORKSPACE / folder_name / filename
        img_dir  = WORKSPACE / folder_name / entry_num

        last_edited = page.get("last_edited_time", "")
        marker = f"<!-- synced: {last_edited} -->"
        if not force and filepath.exists() and marker in filepath.read_text(encoding="utf-8"):
            skipped += 1
            continue

        print(f"  Syncing {entry_num:>5}  →  {folder_name}/{filename}")

        try:
            md_resp = client.pages.retrieve_markdown(page_id=page["id"])
            raw_body = md_resp.get("markdown", "")
            body = localise_images(raw_body, img_dir)

            header = build_header(entry_num, date_str, pair, props)
            (WORKSPACE / folder_name).mkdir(exist_ok=True)
            filepath.write_text(header + body + f"\n\n{marker}\n", encoding="utf-8")
            synced += 1

        except Exception as e:
            print(f"  Error on '{entry_num}': {e}")
            errors += 1

    print(f"\nDone — {synced} synced, {skipped} already up-to-date, {errors} errors.")


def main():
    try:
        from notion_client import Client
    except ImportError:
        print("Run: pip3 install notion-client")
        sys.exit(1)

    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("Error: NOTION_TOKEN not set.\nAdd to ~/.zshrc: export NOTION_TOKEN=...")
        sys.exit(1)

    force = "--force" in sys.argv
    sync(Client(auth=token), force=force)


if __name__ == "__main__":
    main()
