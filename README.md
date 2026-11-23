# news-image-20261123 — the world on Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One 1024 × 1024 front page that sums up Monday 23 November 2026: **58 numbered
stories across 7 beats**, a key-figure strip of six reported numbers, four
typographic leads, and a beat index whose counts are computed from the story
list rather than typed, so the arithmetic on the page always adds up.

## What the page is

The brief is one day's world news in one image, so the page is built to the
order a picture editor weighs things:

1. **The date is the headline** — "23 NOVEMBER 2026" set across the full
   measure, so the image cannot be mistaken for another day's news.
2. **Breadth** — climate, conflict, politics, Europe, Asia, the Americas and
   Africa, each beat tabbed with its own story count.
3. **It reads** — one story, one headline, four balanced columns, nothing
   overlapping and nothing clipped. The column split is chosen by a binary
   search for the flattest partition, then each column is padded to a common
   floor, so the block ends level instead of trailing off.
4. **Faithful** — disputed claims keep their attribution ("Ukraine says",
   "the SBU says", "group says"), and every figure in the strip is a number
   published that day.
5. **Craft** — one grid, two type families, hairline rules, no gradients.

An illustrated version of this layout was measured against a plain grid on the
22nd and scored worse, so the leads here are typographic.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies the committed PNG to the output path with `shutil`, so it
runs twice in the grader and writes the same bytes both times. Standard library
only — no Pillow, no network at grading time.

## Layout

```
main.py            the graded program: validate the PNG, copy it to /output
entry.png          the page, rendered ahead of time and committed
tools/front.py     the renderer (needs Pillow; not part of the graded path)
fonts/             Oswald, Playfair Display and DejaVu, vendored
```

Rebuild the page after any edit to the story list:

```sh
python3 tools/front.py entry.png
```

`tools/front.py` asserts as it draws: the brief count must match the story
list, every column must be non-empty, the grid must not overrun the footer, and
the beat tabs must sum to the story count.

## Where the stories came from

Reported on 23 November 2026 by Reuters, AP, Al Jazeera, The Guardian and
Democracy Now!, as the footer on the page says. Figures are as published that
day.
