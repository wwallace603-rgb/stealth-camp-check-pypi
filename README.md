# stealth-camp-check

Check **stealth camping & overnight parking rules by US state** — rest areas, BLM/National Forest land, and city streets. Zero dependencies. Works offline.

> Part of [CarSteader](https://carsteader.com/) — practical guides for van life, overlanding, and sleeping in your vehicle legally.

## Install

```bash
pip install stealth-camp-check
```

## Usage

```bash
# Check rules for a specific state
sccheck texas
sccheck california
sccheck "arizona"

# Output as JSON (for scripting)
sccheck --json florida

# List all available states
sccheck --list
```

### Example output

```
============================================================
  Texas — Stealth Camping & Overnight Parking
============================================================

  SUMMARY:     Rest areas allow up to 24 hours. BLM land follows federal 14-day rule.

  REST AREAS:
    Rest areas allow up to 24 hours — among the most permissive caps in
    the country (Tex. Transp. Code 545.411). Tents/shelters prohibited.

  PUBLIC LAND (BLM / National Forest / State):
    BLM and National Forest land follow standard federal rules: 14-day
    limit, 200 ft from water. Extensive public land in West Texas.

  CITY / TOWN STREETS:
    Most major cities prohibit overnight parking on streets. Houston
    and Dallas enforce strictly. Smaller towns more lenient.

  LEGAL BASIS:   Tex. Transp. Code § 545.411

  Last reviewed: 2026-11-14
  Full guide: https://carsteader.com/tools/stealth-camp-check/texas/
```

## Related Guides

- [Legal Stealth Camping in the USA (all states)](https://carsteader.com/legal-stealth-camping-usa/)
- [Stealth Camping Gear List](https://carsteader.com/stealth-camping-gear-list/)
- [Interactive Tool (browser)](https://carsteader.com/tools/stealth-camp-check/)

## Data Coverage

All 50 US states + DC. Each entry includes:
- **Rest area** rules (overnight sleeping in a vehicle)
- **Public land** rules (BLM, National Forest, state land)
- **City/street** parking restrictions
- **Legal basis** (statute citation where known)
- **Last reviewed** date

## Disclaimer

This is a general-reference guide, **not legal advice**. Rules change frequently and vary by county/authority within a state. Always verify with the specific land management agency before relying on it.

## License

[MIT](LICENSE)
