# Friday 20 November 2026 — world news in one image

A newspaper front page for Friday 20 November 2026: masthead, lead
story (four ballistic missiles hit Kyiv overnight), two illustrated
leads, a world map marking where the day happened, nine more stories
in three columns, and 24 numbered briefs — 36 verified stories in
all, every one reported on 20 November 2026.

- `build_frontpage.py` — draws `entry.png` (1024×1024, PIL).
- `main.ts` — copies `entry.png` to the output directory.
- `entry.png` — the front page itself.

Build: `python3 build_frontpage.py`, then
`mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`.
