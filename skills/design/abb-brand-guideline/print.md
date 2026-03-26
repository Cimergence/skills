# ABB Brand — Print / PDF / Poster

Use this guide when producing print-ready posters, A3/A2 safety notices,
one-pagers, or PDF documents following ABB's visual identity.

Always read the [pdf SKILL.md](/mnt/skills/public/pdf/SKILL.md) alongside
this file for PDF generation mechanics.

---

## Print Color Mode

| Context | Mode | Notes |
|---------|------|-------|
| Digital display / screen | RGB | Use hex values as listed |
| Professional print | CMYK | Convert — see table below |
| Office laser / inkjet | RGB | Use hex values |

### CMYK Equivalents

| Color | Hex | CMYK |
|-------|-----|------|
| ABB Red | `#FF000F` | C:0 M:100 Y:94 K:0 |
| Near-black | `#1A1A1A` | C:0 M:0 Y:0 K:90 |
| Light gray card | `#F2F2F2` | C:0 M:0 Y:0 K:5 |
| White | `#FFFFFF` | C:0 M:0 Y:0 K:0 |

---

## Standard Paper Formats

| Format | Dimensions | Best use |
|--------|-----------|---------|
| A4 portrait | 210 × 297 mm | Quick reference card, 1-pager |
| A3 landscape | 420 × 297 mm | Operator poster (standard) |
| A2 portrait | 420 × 594 mm | Wall-mounted safety poster |
| A1 portrait | 594 × 841 mm | Large format floor signage |

For **operator posters** (like emergency response): **A3 landscape** is the
standard. Use 3 mm bleed on all sides for professional printing.

---

## Page Margins

| Format | Margin |
|--------|--------|
| A4 | 20 mm all sides |
| A3 landscape | 15 mm all sides |
| A2 / A1 | 20 mm all sides |
| Safe text area (from bleed) | margin + 3 mm bleed |

---

## Typography for Print

Use **ABB Voice** typeface. For print, point sizes differ from screen:

| Element | Size | Weight |
|---------|------|--------|
| Poster main title | 36–48 pt | Bold (700) |
| Section header | 14–16 pt | Bold (700), ALL CAPS |
| Body text | 10–12 pt | Regular (400) |
| Caption / footnote | 8–9 pt | Light (300) or Regular |
| Emergency number | 24–36 pt | Bold (700) |
| Stat callout | 48–72 pt | Bold (700) |

**Minimum legible size for print**: 8 pt. Never go below for safety-critical text.

---

## Layout Grid — A3 Landscape Poster

```
┌──────────────────────────────────────────────────────────────────────┐
│ 15mm margin                                                          │
│  ─ (red dash 30mm × 3mm)    [document tag: 9pt, #888888, ALLCAPS]   │
│  POSTER TITLE (ABB Voice Bold, 36pt, #1A1A1A)                       │
│  Subtitle line (ABB Voice Regular, 12pt, #888888)         [ABB logo] │
├──────────────────────────────────────────────────────────────────────┤  ← 3px red rule (optional) or 1px #E8E8E8
│                                                                      │
│  [LEFT COLUMN — 55% width]     │  [RIGHT COLUMN — 45% width]        │
│                                │                                     │
│  Step/workflow content          │  PPE / reference tables            │
│  Scenario cards                │  Contact cards                     │
│                                │  Quick reference                   │
│                                │                                     │
├──────────────────────────────────────────────────────────────────────┤
│  © 2026 ABB Switzerland. All rights reserved. · Ref: v0.1.4   [ABB] │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Generating a PDF Poster with ReportLab

```python
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --- ABB Colors ---
ABB_RED      = HexColor("#FF000F")
ABB_BLACK    = HexColor("#1A1A1A")
ABB_GRAY_88  = HexColor("#888888")
ABB_GRAY_F2  = HexColor("#F2F2F2")
ABB_GRAY_E8  = HexColor("#E8E8E8")
ABB_WHITE    = HexColor("#FFFFFF")

MARGIN = 15 * mm

# --- Register ABB Voice fonts ---
def register_abb_fonts(font_dir="./fonts"):
    """
    Register ABB Voice TTF files with ReportLab.
    font_dir should contain: ABBVoice.ttf, ABBVoice-Bold.ttf,
                              ABBVoice-Light.ttf, ABBVoice-Medium.ttf
    Falls back to Helvetica if files not found.
    """
    font_map = {
        "ABBVoice":        f"{font_dir}/ABBVoice.ttf",
        "ABBVoice-Bold":   f"{font_dir}/ABBVoice-Bold.ttf",
        "ABBVoice-Light":  f"{font_dir}/ABBVoice-Light.ttf",
        "ABBVoice-Medium": f"{font_dir}/ABBVoice-Medium.ttf",
    }
    for name, path in font_map.items():
        try:
            pdfmetrics.registerFont(TTFont(name, path))
        except Exception:
            pass  # Fall back to Helvetica

def abb_font(weight="regular"):
    """Return registered ReportLab font name for a given ABB Voice weight."""
    return {
        "light":   "ABBVoice-Light",
        "regular": "ABBVoice",
        "medium":  "ABBVoice-Medium",
        "bold":    "ABBVoice-Bold",
    }.get(weight, "Helvetica")


# --- Layout helpers ---
def draw_red_dash(c, x, y, width=30*mm, height=3*mm):
    """Draw the signature ABB red title dash."""
    c.setFillColor(ABB_RED)
    c.rect(x, y, width, height, fill=1, stroke=0)

def draw_section_badge(c, x, y, text, width=25*mm, height=5*mm):
    """Draw a red label badge (e.g. 'STEP 1')."""
    c.setFillColor(ABB_RED)
    c.rect(x, y, width, height, fill=1, stroke=0)
    c.setFillColor(ABB_WHITE)
    c.setFont(abb_font("bold"), 8)
    c.drawCentredString(x + width / 2, y + 1.5*mm, text.upper())

def draw_card(c, x, y, width, height, fill=None):
    """Draw a light gray card background."""
    c.setFillColor(fill or ABB_GRAY_F2)
    c.setStrokeColor(ABB_GRAY_E8)
    c.setLineWidth(0.5)
    c.roundRect(x, y, width, height, 2*mm, fill=1, stroke=1)

def draw_red_top_card(c, x, y, width, height):
    """Draw a card with a red top border."""
    draw_card(c, x, y, width, height)
    c.setFillColor(ABB_RED)
    c.rect(x, y + height - 2*mm, width, 2*mm, fill=1, stroke=0)

def draw_abb_logo(c, page_width, page_height, size=14):
    """Place ABB logo text bottom-right."""
    c.setFillColor(ABB_RED)
    c.setFont(abb_font("bold"), size)
    c.drawRightString(page_width - MARGIN, MARGIN + 2*mm, "ABB")

def draw_footer(c, page_width, text_left, text_right, y=None):
    """Draw the standard ABB footer strip."""
    if y is None:
        y = MARGIN - 4*mm
    c.setFillColor(ABB_GRAY_F2)
    c.rect(0, 0, page_width, MARGIN, fill=1, stroke=0)
    c.setFillColor(ABB_GRAY_88)
    c.setFont(abb_font("regular"), 7)
    c.drawString(MARGIN, y, text_left)
    c.drawRightString(page_width - MARGIN - 20*mm, y, text_right)


# --- Example: A3 landscape poster skeleton ---
def create_abb_poster(output_path, title, subtitle, doc_ref="v0.1.4"):
    register_abb_fonts()
    page_w, page_h = landscape(A3)
    c = canvas.Canvas(output_path, pagesize=landscape(A3))

    # White background
    c.setFillColor(ABB_WHITE)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    # Header
    header_y = page_h - MARGIN - 18*mm
    draw_red_dash(c, MARGIN, header_y + 16*mm)
    c.setFillColor(ABB_BLACK)
    c.setFont(abb_font("bold"), 28)
    c.drawString(MARGIN, header_y + 4*mm, title)
    c.setFillColor(ABB_GRAY_88)
    c.setFont(abb_font("regular"), 10)
    c.drawString(MARGIN, header_y - 2*mm, subtitle)

    # Thin separator line under header
    sep_y = header_y - 6*mm
    c.setStrokeColor(ABB_GRAY_E8)
    c.setLineWidth(0.5)
    c.line(MARGIN, sep_y, page_w - MARGIN, sep_y)

    # ABB logo + footer
    draw_abb_logo(c, page_w, page_h)
    draw_footer(c, page_w,
                f"© 2026 ABB Switzerland. All rights reserved.",
                f"Ref: {doc_ref}")

    # [Add content shapes here using the helpers above]

    c.save()
    print(f"Poster saved: {output_path}")
```

---

## Print QA Checklist

Before sending to print:

- [ ] Bleed: 3 mm on all sides (for professional printing)
- [ ] Color mode: CMYK for offset print, RGB for digital
- [ ] Minimum font size: 8 pt (10 pt for safety-critical instructions)
- [ ] ABB Red verified as `#FF000F` / CMYK 0-100-94-0
- [ ] Red dash above main title present
- [ ] ABB logo bottom-right, red, correct weight
- [ ] No other accent colors used
- [ ] Emergency phone numbers at ≥ 24 pt
- [ ] Footer with doc reference and © year
- [ ] All section headers in ALLCAPS, ABB Voice Bold
