# ABB Brand — PowerPoint (PPTX)

Use this guide when creating or restyling `.pptx` presentations to ABB's
visual identity using `python-pptx`.

Always read the [pptx SKILL.md](/mnt/skills/public/pptx/SKILL.md) alongside
this file for slide creation mechanics.

---

## Slide Dimensions

ABB standard: **widescreen 16:9**

```python
from pptx.util import Inches
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
```

---

## Color Constants

```python
from pptx.dml.color import RGBColor

class ABBColor:
    RED        = RGBColor(0xFF, 0x00, 0x0F)  # #FF000F — primary accent
    RED_DARK   = RGBColor(0xCC, 0x00, 0x00)  # #CC0000 — hover / deep red
    WHITE      = RGBColor(0xFF, 0xFF, 0xFF)  # #FFFFFF — background
    BLACK      = RGBColor(0x1A, 0x1A, 0x1A)  # #1A1A1A — body text
    GRAY_TEXT  = RGBColor(0x55, 0x55, 0x55)  # #555555 — secondary text
    GRAY_MUTE  = RGBColor(0x88, 0x88, 0x88)  # #888888 — captions / metadata
    GRAY_CARD  = RGBColor(0xF2, 0xF2, 0xF2)  # #F2F2F2 — card backgrounds
    GRAY_LINE  = RGBColor(0xE8, 0xE8, 0xE8)  # #E8E8E8 — dividers / borders
    DARK_BG    = RGBColor(0x14, 0x14, 0x14)  # #141414 — dark title slides
```

---

## Font Application

ABB Voice must be installed on the system for python-pptx to embed it.

```python
from pptx.util import Pt

ABB_FONT       = "ABB Voice"
ABB_FONT_FALLBACK = "Arial"   # Used if ABB Voice is not installed

def set_font(run, size_pt, bold=False, weight="regular", color=None):
    """
    Apply ABB Voice typography to a text run.
    weight: "light" | "regular" | "medium" | "bold"
    """
    run.font.name = ABB_FONT
    run.font.size = Pt(size_pt)
    run.font.bold = bold or (weight == "bold")
    if color:
        run.font.color.rgb = color
    # Note: python-pptx does not expose font-weight directly.
    # For Light / Medium weights, embed the correct TTF variant
    # by setting font name to "ABB Voice Light" or "ABB Voice Medium".
    if weight == "light":
        run.font.name = "ABB Voice Light"
    elif weight == "medium":
        run.font.name = "ABB Voice Medium"


# Typography scale
SIZES = {
    "slide_title":   (36, True,  "bold"),    # Slide title — Bold 36pt
    "section_head":  (20, True,  "bold"),    # Section headers — Bold 20pt
    "body":          (14, False, "regular"), # Body text — Regular 14pt
    "caption":       (10, False, "regular"), # Captions — Regular 10pt
    "stat":          (48, True,  "bold"),    # Big stat callout — Bold 48pt
    "badge":         (11, True,  "bold"),    # Badge labels — Bold 11pt CAPS
}
```

---

## Slide Layouts

### Layout 1 — Standard content (white bg, red accent)

```
┌─────────────────────────────────────────────────────────┐
│  ─  (red dash 0.35", 0.1" tall)                         │
│  SLIDE TITLE  (ABB Voice Bold, 36pt, #1A1A1A)           │
│                                                         │
│  [content area: rows, cards, columns]                   │
│                                                         │
│  © 2026 ABB  ·  Slide N                    [ABB logo]   │
└─────────────────────────────────────────────────────────┘
```

```python
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN

def add_standard_slide(prs, title_text, subtitle=None):
    slide_layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(slide_layout)

    # Red dash accent above title
    dash = slide.shapes.add_shape(
        MSO_SHAPE_TYPE.RECTANGLE,
        Inches(0.5), Inches(0.35),
        Inches(0.35), Inches(0.07)
    )
    dash.fill.solid()
    dash.fill.fore_color.rgb = ABBColor.RED
    dash.line.fill.background()

    # Slide title
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.5), Inches(8.5), Inches(0.7)
    )
    tf = title_box.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title_text
    set_font(run, 28, bold=True, color=ABBColor.BLACK)

    return slide
```

### Layout 2 — Dark title / cover slide

```python
def add_cover_slide(prs, title_text, subtitle=None):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Full dark background
    bg = slide.shapes.add_shape(
        MSO_SHAPE_TYPE.RECTANGLE,
        Inches(0), Inches(0),
        prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = ABBColor.DARK_BG
    bg.line.fill.background()

    # Red left accent bar
    bar = slide.shapes.add_shape(
        MSO_SHAPE_TYPE.RECTANGLE,
        Inches(0), Inches(0),
        Inches(0.12), prs.slide_height
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = ABBColor.RED
    bar.line.fill.background()

    # Title text
    tb = slide.shapes.add_textbox(
        Inches(0.5), Inches(2.8), Inches(7), Inches(1.5)
    )
    tf = tb.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title_text
    set_font(run, 36, bold=True, color=ABBColor.WHITE)

    return slide
```

---

## Red Icon Square

```python
from pptx.util import Inches

def add_icon_square(slide, left, top, size_inches=0.35):
    """Add a red square icon placeholder (fill manually with an image or symbol)."""
    sq = slide.shapes.add_shape(
        MSO_SHAPE_TYPE.RECTANGLE,
        Inches(left), Inches(top),
        Inches(size_inches), Inches(size_inches)
    )
    sq.fill.solid()
    sq.fill.fore_color.rgb = ABBColor.RED
    sq.line.fill.background()
    return sq
```

---

## Card Row (gray background list item)

```python
def add_card_row(slide, left, top, width, height, label, title, cta=None):
    # Gray card background
    card = slide.shapes.add_shape(
        MSO_SHAPE_TYPE.RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = ABBColor.GRAY_CARD
    card.line.color.rgb = ABBColor.GRAY_LINE
    card.line.width = Pt(0.5)

    # Label text (small caps style)
    label_box = slide.shapes.add_textbox(
        Inches(left + 0.15), Inches(top + 0.05),
        Inches(width - 0.3), Inches(0.2)
    )
    lp = label_box.text_frame.paragraphs[0]
    lr = lp.add_run()
    lr.text = label.upper()
    set_font(lr, 9, color=ABBColor.GRAY_MUTE)

    # Title text
    title_box = slide.shapes.add_textbox(
        Inches(left + 0.15), Inches(top + 0.22),
        Inches(width - 0.3), Inches(height - 0.28)
    )
    tp = title_box.text_frame.paragraphs[0]
    tr = tp.add_run()
    tr.text = title
    set_font(tr, 13, bold=True, color=ABBColor.BLACK)
```

---

## Applying ABB Brand to an Existing PPTX

```python
from pptx import Presentation
from pptx.util import Pt

def rebrand_presentation(input_path, output_path):
    """Apply ABB brand colors and fonts to an existing presentation."""
    prs = Presentation(input_path)

    for slide in prs.slides:
        for shape in slide.shapes:
            # Recolor solid fills
            if shape.fill.type == 1:  # SOLID
                rgb = shape.fill.fore_color.rgb
                # Map any bright red to ABB Red
                if rgb.red > 180 and rgb.green < 50 and rgb.blue < 50:
                    shape.fill.fore_color.rgb = ABBColor.RED
                # Map dark fills to ABB dark bg
                elif rgb.red < 40 and rgb.green < 40 and rgb.blue < 40:
                    shape.fill.fore_color.rgb = ABBColor.DARK_BG

            # Recolor text and apply ABB Voice
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        # Apply font family
                        run.font.name = ABB_FONT
                        # Map red text to ABB Red
                        try:
                            c = run.font.color.rgb
                            if c.red > 180 and c.green < 50 and c.blue < 50:
                                run.font.color.rgb = ABBColor.RED
                        except Exception:
                            pass

    prs.save(output_path)
    print(f"Saved rebranded presentation: {output_path}")
```

---

## Slide-by-Slide Checklist

Before delivering any ABB-branded PPTX, verify:

- [ ] White or `#141414` background (no other background colors)
- [ ] Red dash above every major section title
- [ ] ABB Red used only for accents — no second accent color
- [ ] ABB Voice (or Arial fallback) applied to all text
- [ ] Title text ≥ 24pt, body text 14–16pt, captions 10–12pt
- [ ] ABB logo bottom-right on every slide
- [ ] Footer strip with `©` on content slides
- [ ] No underlines used as decorative title accents (use red dash instead)
- [ ] No font-weight 600 (jump from 500 Medium to 700 Bold)
