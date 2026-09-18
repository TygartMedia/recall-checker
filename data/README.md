# Data: agency recall files

The checker sits on files that already exist. Nothing here requires a new behavior from the agencies.

## Sources

- **CPSC** — consumer product recalls (305 events in 2024, 420 in 2025 per the RecallBench mirror)
- **FDA enforcement reports** + **USDA-FSIS** — food recall events (516 in 2024, 642 in 2025)
- **NHTSA** — vehicle recall campaigns (996 in 2025; 645 through mid-September 2026)

## Mirror

RecallBench mirrors the official feeds nightly (public, as of September 2026).
TODO: `mirror.py` that pulls the mirror into `data/mirror/` and indexes by UPC, lot, establishment number, and VIN prefix.

## Schema (planned)

`data/mirror/index.json` — one entry per event: agency, event id, date, class (when the agency uses one), affected identifiers, agency URL.
