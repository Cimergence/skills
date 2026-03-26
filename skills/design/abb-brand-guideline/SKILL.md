---
name: abb-brand-guideline
description: >
  Applies ABB's official brand colors, typography (ABB Voice), and visual
  identity system to any artifact — posters, PPTX slides, HTML pages, PDFs,
  SVG diagrams, or widgets. Use it whenever ABB brand colors, style guidelines,
  visual formatting, or ABB corporate design standards apply.
license: Complete terms in LICENSE.txt
---

# ABB Brand Guideline Skill

## Quick Reference

| Task | Guide |
|------|-------|
| Apply brand to HTML / SVG / widget | Read [web.md](web.md) |
| Apply brand to PPTX slides | Read [pptx.md](pptx.md) |
| Apply brand to print / PDF / poster | Read [print.md](print.md) |
| Install ABB Voice font | Read [fonts.md](fonts.md) |
| Python color / font helpers | `scripts/abb_brand.py` |

---

## Brand Identity Summary

ABB's visual identity is built on **three pillars**: bold simplicity, a single
dominant red accent, and disciplined whitespace. It never competes with itself —
one accent color, one font family, one hierarchy.

### Colors

| Role | Name | Hex | RGB | Usage |
|------|------|-----|-----|-------|
| **Primary accent** | ABB Red | `#FF000F` | 255, 0, 15 | CTAs, icons, borders, highlights, logo |
| **Dark Red** | ABB Red Dark | `#CC0000` | 204, 0, 0 | Hover states, deep red fills |
| **Primary background** | White | `#FFFFFF` | 255, 255, 255 | Page / slide background (standard) |
| **Primary text** | Near-black | `#1A1A1A` | 26, 26, 26 | All body copy and headings |
| **Secondary text** | Dark gray | `#555555` | 85, 85, 85 | Captions, subtext, footnotes |
| **Muted text** | Mid gray | `#888888` | 136, 136, 136 | Labels, metadata, timestamps |
| **Card background** | Light gray | `#F2F2F2` | 242, 242, 242 | Cards, table rows, info blocks |
| **Subtle divider** | Pale gray | `#E8E8E8` | 232, 232, 232 | Dividers, borders, grid lines |
| **Dark background** | Off-black | `#141414` | 20, 20, 20 | Dark-mode slides, title covers |

> **Rule**: ABB Red is the ONLY accent color. Never introduce a second accent.
> Never use purple, teal, orange, or blue as decorative colors in ABB materials.

### Typography — ABB Voice

ABB's proprietary typeface. It is a humanist sans-serif with four weights.

| Weight | File name | python-pptx constant | Use |
|--------|-----------|----------------------|-----|
| Light | `ABBVoice-Light.ttf` | n/a (set manually) | Long body copy, disclaimers |
| Regular | `ABBVoice.ttf` | `PP_REGULAR` | Body text, captions |
| Medium | `ABBVoice-Medium.ttf` | n/a (set manually) | Sub-headings, labels |
| Bold | `ABBVoice-Bold.ttf` | `PP_BOLD` | Titles, section headers, callouts |

**Download**: https://en.maisfontes.com/font-family/abb-voice-font-download  
**Fallback stack** (when ABB Voice is unavailable):
`"ABB Voice", "Barlow", "Arial Narrow", Arial, Helvetica, sans-serif`

> See [fonts.md](fonts.md) for installation and programmatic font embedding.

### Spacing & Layout

| Token | Value | Notes |
|-------|-------|-------|
| Page margin | 32 px (web) / 0.5 in (print/PPTX) | Minimum safe margin |
| Section gap | 24 px | Between major content blocks |
| Card padding | 16 px / 12 px (compact) | Internal card/row padding |
| Grid gutter | 8–12 px | Between cards in a grid |
| Border radius | 4 px | Subtle corner rounding on cards |
| Red dash width | 28–36 px, height 3–4 px | Signature title accent element |

### Signature Design Patterns

These recurring motifs appear throughout all ABB communications:

1. **Red dash above titles** — a short `#FF000F` horizontal bar (28–36 px wide,
   3–4 px tall) placed immediately above every major section title.

2. **Red-filled icon squares** — `#FF000F` square tiles (28–36 px) with white
   SVG icons inside, used as visual anchors next to list items and stats.

3. **ABB Red chevron arrows** — solid filled right-pointing triangles in
   `#FF000F`, used as connectors between horizontal steps or decision branches.

4. **Light gray card rows** — `#F2F2F2` background with 1 px `#E8E8E8` bottom
   border, for tabular data and feature lists.

5. **Red top-border cards** — cards with `border-top: 3px solid #FF000F` and
   `#F2F2F2` background, for contact blocks, data callouts, and info panels.

6. **ABB logo placement** — bottom-right corner, `#FF000F`, Barlow Condensed
   900 / ABB Voice Bold, letter-spacing 4–5 px. Never placed anywhere else.

7. **© footer strip** — `#F2F2F2` background, 10 px text, `#888888`, matching
   the slide footer style.

---

## What to read next

- Building a **web page, HTML artifact, SVG, or interactive widget** → [web.md](web.md)
- Styling a **PowerPoint presentation** → [pptx.md](pptx.md)
- Creating a **print poster or PDF** → [print.md](print.md)
- Installing or embedding **ABB Voice font** → [fonts.md](fonts.md)
- Using the **Python helper utilities** → `scripts/abb_brand.py`
