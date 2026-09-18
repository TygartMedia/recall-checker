#!/usr/bin/env python3
"""Recall Checker — photo of the label in, match/no-match out.

Pipeline:
    photo -> identifier extraction (vision model) -> agency feed match -> verdict

Current state: scaffold. Extraction and feed-match are stubs with TODO
markers; the CLI and the verdict contract are real.
"""
import argparse
import json
import sys


def extract_identifiers(photo_path):
    """TODO: vision-model call. Returns dict with upc, lot, brand,
    product_name, vin — unreadable fields marked as such, never guessed."""
    print(f"[stub] extracting identifiers from {photo_path} ...", file=sys.stderr)
    return {
        "upc": None,
        "lot": None,
        "brand": None,
        "product_name": None,
        "vin": None,
        "note": "STUB — wire up the vision call (see prompts/first-pass.md)",
    }


def match_feeds(identifiers):
    """TODO: match against mirrored agency files (see data/README.md)."""
    print("[stub] matching against agency feeds ...", file=sys.stderr)
    return {
        "verdict": "STUB",
        "matches": [],
        "note": "STUB — needs the nightly feed mirror",
    }


def main():
    ap = argparse.ArgumentParser(
        description="Recall Checker: match a label photo against live recall files."
    )
    ap.add_argument("--photo", required=True, help="Path to the label/package/VIN photo")
    args = ap.parse_args()

    identifiers = extract_identifiers(args.photo)
    result = match_feeds(identifiers)
    print(json.dumps({"identifiers": identifiers, "result": result}, indent=2))


if __name__ == "__main__":
    main()
