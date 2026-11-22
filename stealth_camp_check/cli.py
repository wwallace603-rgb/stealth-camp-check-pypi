import argparse
import json
import os
import sys

def load_states():
    path = os.path.join(os.path.dirname(__file__), "states.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def find_state(states, query):
    q = query.lower().strip()
    # Exact slug match
    for s in states:
        if s["slug"] == q:
            return s
    # Exact name match (case-insensitive)
    for s in states:
        if s["name"].lower() == q:
            return s
    # Partial match
    matches = [s for s in states if q in s["slug"] or q in s["name"].lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = ", ".join(m["name"] for m in matches[:5])
        print(f"Multiple matches: {names}. Be more specific.", file=sys.stderr)
        sys.exit(1)
    return None

def print_state(state):
    print(f"\n{'='*60}")
    print(f"  {state['name']} — Stealth Camping & Overnight Parking")
    print(f"{'='*60}\n")
    print(f"  SUMMARY:     {state['summary']}\n")
    print(f"  REST AREAS:")
    for line in wrap(state["restArea"]):
        print(f"    {line}")
    print(f"\n  PUBLIC LAND (BLM / National Forest / State):")
    for line in wrap(state["publicLand"]):
        print(f"    {line}")
    print(f"\n  CITY / TOWN STREETS:")
    for line in wrap(state["cityParking"]):
        print(f"    {line}")
    if state.get("legalBasis"):
        print(f"\n  LEGAL BASIS:   {state['legalBasis']}")
    print(f"\n  Last reviewed: {state['lastReviewed']}")
    print(f"\n  Full guide: https://carsteader.com/tools/stealth-camp-check/{state['slug']}/")
    print()

def wrap(text, width=72):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = cur + " " + w if cur else w
    if cur:
        lines.append(cur)
    return lines

def list_states(states):
    print("\nUS States with Stealth Camping Data:\n")
    col_width = 20
    for i, s in enumerate(sorted(states, key=lambda x: x["name"])):
        print(f"  {s['slug']:<18} {s['name']}")
    print(f"\n  Total: {len(states)} states")
    print(f"  Usage: sccheck <state>  (e.g., sccheck texas)")

def main():
    parser = argparse.ArgumentParser(
        prog="sccheck",
        description="Check stealth camping & overnight parking rules by US state.",
        epilog="Full guides at https://carsteader.com/tools/stealth-camp-check/"
    )
    parser.add_argument("state", nargs="?", help="State name or slug (e.g., 'texas', 'TX' not supported — use full name)")
    parser.add_argument("--list", "-l", action="store_true", help="List all available states")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    states = load_states()

    if args.list or not args.state:
        list_states(states)
        return

    state = find_state(states, args.state)
    if not state:
        print(f"No data found for '{args.state}'. Try --list to see available states.", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(state, indent=2, ensure_ascii=False))
    else:
        print_state(state)

if __name__ == "__main__":
    main()
