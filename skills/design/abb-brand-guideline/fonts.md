# ABB Voice — Font Installation & Embedding

ABB Voice is ABB's proprietary corporate typeface. It is a humanist sans-serif
designed for clarity at all sizes, from emergency posters to digital dashboards.

---

## Font Weights & Files

| Weight | Font name (CSS/system) | TTF filename | Use |
|--------|------------------------|-------------|-----|
| Light (300) | ABB Voice Light | `ABBVoice-Light.ttf` | Long body copy, footnotes |
| Regular (400) | ABB Voice | `ABBVoice.ttf` | Body text, paragraphs |
| Medium (500) | ABB Voice Medium | `ABBVoice-Medium.ttf` | Sub-headings, labels, nav |
| Bold (700) | ABB Voice Bold | `ABBVoice-Bold.ttf` | Titles, badges, callouts |

> ⚠ ABB Voice has **no 600 weight**. Always jump from 500 (Medium) to 700 (Bold).

---

## Download

The font family is available for free personal use from:

**https://en.maisfontes.com/font-family/abb-voice-font-download**

Individual weight pages:
- ABB Voice (Regular): https://en.maisfontes.com/abbvoice.font
- ABB Voice Bold: https://en.maisfontes.com/abbvoice-bold.font
- ABB Voice Light: https://en.maisfontes.com/abbvoice-light.font
- ABB Voice Medium: https://en.maisfontes.com/abbvoice-medium.font

> For commercial use, contact ABB directly for licensing.

---

## System Installation

### Windows

1. Download the `.ttf` files from the links above
2. Right-click each file → **Install for all users** (or double-click → Install)
3. Restart any open Office / design applications

### macOS

1. Download the `.ttf` files
2. Double-click each → **Install Font** in Font Book
3. Or drag to `/Library/Fonts/` (system-wide) or `~/Library/Fonts/` (user)

### Linux

```bash
mkdir -p ~/.local/share/fonts/ABBVoice
cp ABBVoice*.ttf ~/.local/share/fonts/ABBVoice/
fc-cache -fv
fc-list | grep -i "abb"   # verify installation
```

### Docker / sandbox environment

```bash
# In Dockerfile or setup script
RUN mkdir -p /usr/share/fonts/truetype/abbvoice
COPY ABBVoice*.ttf /usr/share/fonts/truetype/abbvoice/
RUN fc-cache -fv
```

---

## Checking Installation in Python

```python
import subprocess

def is_abb_voice_installed():
    """Return True if ABB Voice is available on this system."""
    try:
        result = subprocess.run(
            ["fc-list", "--format=%{family}\n"],
            capture_output=True, text=True
        )
        return "ABB Voice" in result.stdout
    except FileNotFoundError:
        # Windows: check via registry or fonts folder
        import os
        win_fonts = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
        return os.path.exists(os.path.join(win_fonts, "ABBVoice.ttf"))

def get_abb_font_name(weight="regular"):
    """
    Return the font name to use — ABB Voice if installed, fallback otherwise.
    weight: 'light' | 'regular' | 'medium' | 'bold'
    """
    if is_abb_voice_installed():
        return {
            "light":   "ABB Voice Light",
            "regular": "ABB Voice",
            "medium":  "ABB Voice Medium",
            "bold":    "ABB Voice Bold",
        }[weight]
    else:
        # Graceful fallback
        return {
            "light":   "Arial",
            "regular": "Arial",
            "medium":  "Arial",
            "bold":    "Arial Black",
        }[weight]
```

---

## Embedding in ReportLab (PDF)

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FONT_DIR = "./fonts"  # directory containing ABBVoice*.ttf files

_FONT_REGISTERED = False

def register_abb_fonts():
    global _FONT_REGISTERED
    if _FONT_REGISTERED:
        return
    fonts = {
        "ABBVoice":        "ABBVoice.ttf",
        "ABBVoice-Light":  "ABBVoice-Light.ttf",
        "ABBVoice-Medium": "ABBVoice-Medium.ttf",
        "ABBVoice-Bold":   "ABBVoice-Bold.ttf",
    }
    for name, filename in fonts.items():
        path = os.path.join(FONT_DIR, filename)
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path))
        else:
            print(f"  ⚠ Font not found: {path} — falling back to Helvetica")
    _FONT_REGISTERED = True

def abb_font(weight="regular"):
    """Return ReportLab font name for ABB Voice weight."""
    register_abb_fonts()
    mapping = {
        "light":   "ABBVoice-Light",
        "regular": "ABBVoice",
        "medium":  "ABBVoice-Medium",
        "bold":    "ABBVoice-Bold",
    }
    name = mapping.get(weight, "ABBVoice")
    # Fall back to Helvetica if not registered
    try:
        pdfmetrics.getFont(name)
        return name
    except Exception:
        return "Helvetica-Bold" if weight == "bold" else "Helvetica"
```

---

## Embedding in python-pptx (PPTX)

python-pptx uses the font name string. If ABB Voice is installed on the
system where the PPTX is generated, it will be embedded on save.

```python
from pptx.util import Pt

def apply_abb_voice(run, size_pt, weight="regular", color=None):
    """Apply ABB Voice to a python-pptx text run."""
    font_name_map = {
        "light":   "ABB Voice Light",
        "regular": "ABB Voice",
        "medium":  "ABB Voice Medium",
        "bold":    "ABB Voice Bold",
    }
    run.font.name = font_name_map.get(weight, "ABB Voice")
    run.font.size = Pt(size_pt)
    run.font.bold = (weight == "bold")
    if color:
        run.font.color.rgb = color
```

---

## CSS @font-face (Web / HTML Artifacts)

```css
/* Self-hosted TTF — place files in /fonts/ relative to stylesheet */
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Light.ttf") format("truetype");
  font-weight: 300;
  font-style: normal;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Medium.ttf") format("truetype");
  font-weight: 500;
  font-style: normal;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Bold.ttf") format("truetype");
  font-weight: 700;
  font-style: normal;
}

/* Usage */
body {
  font-family: "ABB Voice", "Barlow", Arial, Helvetica, sans-serif;
}
```

---

## Fallback Stack

When ABB Voice is not available, use this ordered fallback:

```
"ABB Voice", "Barlow", "Barlow Condensed", "Arial Narrow", Arial, Helvetica, sans-serif
```

Barlow is the closest free alternative — it is a humanist grotesque with similar
proportions and weight distribution. Load it from Google Fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Barlow:wght@300;400;500;700&display=swap');
```
