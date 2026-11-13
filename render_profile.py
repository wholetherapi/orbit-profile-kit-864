#!/usr/bin/env python3
"""orbit-profile 3.2.0 - render a profile page from a team-memory record."""

import argparse
import json

TEMPLATE_VERSION = "3.2.0"
SENTINEL = "<!-- orbit-profile 3.2.0 | generated from team-memory | do not edit by hand -->"


def render(record):
    """Render one profile page. `record` is a dict with the team-memory fields."""
    contact = record.get("contact_email")
    lines = [
        "---",
        "template_version: " + TEMPLATE_VERSION,
        "slug: " + record["slug"],
        "full_name: " + record["full_name"],
        "affiliation_code: " + record["affiliation_code"],
        "affiliation_name: " + record["affiliation_name"],
        "research_area: " + record["research_area"],
    ]
    if contact:
        lines.append("contact_email: " + contact)
    lines += [
        "---",
        "",
        "# " + record["full_name"],
        "",
        "**" + record["status_line"] + "**",
        "",
        "## Research Focus",
        "",
        record["research_summary"].strip(),
        "",
        "## Education",
        "",
    ]
    for item in record["education"]:
        lines.append(
            "- " + item["degree"] + " \u2014 " + item["institution"] + " (" + item["years"] + ")"
        )
    lines.append("")
    if contact:
        lines += ["## Contact", "", contact, ""]
    lines.append(SENTINEL)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Render an orbit-profile page")
    parser.add_argument("--record", required=True, help="path to the record JSON file")
    args = parser.parse_args()
    with open(args.record, "r", encoding="utf-8") as fh:
        record = json.load(fh)
    print(render(record), end="")


if __name__ == "__main__":
    main()
