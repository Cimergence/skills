"""
abb_brand.py — ABB Brand Guideline helper utilities

Provides color constants, font helpers, and reusable drawing primitives
for Python-based document generation (python-pptx, ReportLab, etc.).

Usage:
    from scripts.abb_brand import ABBColor, ABBFont, ABBLayout
    from scripts.abb_brand import draw_red_dash, draw_section_badge, draw_card
"""

from __future__ import annotations
import os
import subprocess


# ─────────────────────────────────────────────────────────────────────────────
# COLOR CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

class ABBColor:
    """ABB official brand colors as hex strings and RGB tuples."""

    # Primary
    RED        = "#FF000F"   # ABB Red — primary accent, icons, CTAs
    RED_DARK   = "#CC0000"   # Deep red — hover / emphasis

    # Backgrounds
    WHITE      = "#FFFFFF"   # Standard page/slide background
    DARK_BG    = "#141414"   # Dark cover slides
    GRAY_CARD  = "#F2F2F2"   # Card / row backgrounds
    GRAY_LINE  = "#E8E8E8"   # Dividers and grid lines

    # Text
    BLACK      = "#1A1A1A"   # Primary body text
    GRAY_TEXT  = "#555555"   # Secondary / supporting text
    GRAY_MUTE  = "#888888"   # Captions, labels, metadata

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """Convert #RRGGBB string to (R, G, B) int tuple."""
        h = hex_color.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def to_reportlab(hex_color: str):
        """Convert hex string to ReportLab HexColor."""
        try:
            from reportlab.lib.colors import HexColor
            return HexColor(hex_color)
        except ImportError:
            raise ImportError("reportlab is required: pip install reportlab --break-system-packages")

    @staticmethod
    def to_pptx_rgb(hex_color: str):
        """Convert hex string to python-pptx RGBColor."""
        try:
            from pptx.dml.color import RGBColor
            r, g, b = ABBColor.hex_to_rgb(hex_color)
            return RGBColor(r, g, b)
        except ImportError:
            raise ImportError("python-pptx is required: pip install python-pptx --break-system-packages")


# ─────────────────────────────────────────────────────────────────────────────
# FONT HELPERS
# ─────────────────────────────────────────────────────────────────────────────

class ABBFont:
    """ABB Voice font names and availability helpers."""

    FAMILY     = "ABB Voice"
    FALLBACK   = "Barlow"
    FALLBACK2  = "Arial"

    CSS_STACK  = '"ABB Voice", "Barlow", "Barlow Condensed", "Arial Narrow", Arial, Helvetica, sans-serif'

    # Font names by weight (for python-pptx and CSS)
    WEIGHT_NAMES = {
        "light":   "ABB Voice Light",
        "regular": "ABB Voice",
        "medium":  "ABB Voice Medium",
        "bold":    "ABB Voice Bold",
    }

    # TTF filenames
    TTF_FILES = {
        "light":   "ABBVoice-Light.ttf",
        "regular": "ABBVoice.ttf",
        "medium":  "ABBVoice-Medium.ttf",
        "bold":    "ABBVoice-Bold.ttf",
    }

    # ReportLab internal names (after registration)
    REPORTLAB_NAMES = {
        "light":   "ABBVoice-Light",
        "regular": "ABBVoice",
        "medium":  "ABBVoice-Medium",
        "bold":    "ABBVoice-Bold",
    }

    @staticmethod
    def is_installed() -> bool:
        """Return True if ABB Voice is available on this system."""
        try:
            result = subprocess.run(
                ["fc-list", "--format=%{family}\n"],
                capture_output=True, text=True, timeout=5
            )
            return "ABB Voice" in result.stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # Windows fallback
            win_fonts = os.path.join(
                os.environ.get("WINDIR", "C:\\Windows"), "Fonts"
            )
            return os.path.exists(os.path.join(win_fonts, "ABBVoice.ttf"))

    @staticmethod
    def system_name(weight: str = "regular") -> str:
        """
        Return the system font name for the given weight.
        Falls back to Arial / Arial Black if ABB Voice is not installed.
        """
        if ABBFont.is_installed():
            return ABBFont.WEIGHT_NAMES.get(weight, "ABB Voice")
        fallbacks = {
            "light":   "Arial",
            "regular": "Arial",
            "medium":  "Arial",
            "bold":    "Arial Black",
        }
        return fallbacks.get(weight, "Arial")

    @staticmethod
    def register_reportlab(font_dir: str = "./fonts") -> dict[str, bool]:
        """
        Register ABB Voice TTF files with ReportLab.
        Returns a dict of {weight: registered_successfully}.
        """
        try:
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
        except ImportError:
            raise ImportError("reportlab is required: pip install reportlab --break-system-packages")

        results = {}
        for weight, filename in ABBFont.TTF_FILES.items():
            path = os.path.join(font_dir, filename)
            rl_name = ABBFont.REPORTLAB_NAMES[weight]
            if os.path.exists(path):
                try:
                    pdfmetrics.registerFont(TTFont(rl_name, path))
                    results[weight] = True
                except Exception as e:
                    print(f"  ⚠ Could not register {rl_name}: {e}")
                    results[weight] = False
            else:
                results[weight] = False
        return results

    @staticmethod
    def reportlab_name(weight: str = "regular", font_dir: str = "./fonts") -> str:
        """
        Return the ReportLab font name. Registers the font if needed.
        Falls back to Helvetica if the TTF is unavailable.
        """
        try:
            from reportlab.pdfbase import pdfmetrics
        except ImportError:
            return "Helvetica-Bold" if weight == "bold" else "Helvetica"

        rl_name = ABBFont.REPORTLAB_NAMES.get(weight, "ABBVoice")
        try:
            pdfmetrics.getFont(rl_name)
            return rl_name
        except Exception:
            # Try registering
            ABBFont.register_reportlab(font_dir)
            try:
                pdfmetrics.getFont(rl_name)
                return rl_name
            except Exception:
                return "Helvetica-Bold" if weight == "bold" else "Helvetica"


# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

class ABBLayout:
    """Standard spacing and sizing tokens."""

    MARGIN_PX       = 32     # px — web page margin
    SECTION_GAP_PX  = 24     # px — between major sections
    CARD_PAD_PX     = 16     # px — inside cards
    GUTTER_PX       = 8      # px — between cards in a grid
    RADIUS_PX       = 4      # px — border radius for cards

    RED_DASH_W_PX   = 32     # px — signature red dash width
    RED_DASH_H_PX   = 4      # px — signature red dash height

    # Print (mm)
    MARGIN_MM       = 15.0   # mm — page margin for A3 poster
    BLEED_MM        = 3.0    # mm — bleed for professional printing


# ─────────────────────────────────────────────────────────────────────────────
# REPORTLAB DRAWING PRIMITIVES
# ─────────────────────────────────────────────────────────────────────────────

def _require_reportlab():
    try:
        import reportlab
    except ImportError:
        raise ImportError("reportlab is required: pip install reportlab --break-system-packages")


def draw_red_dash(c, x, y, width_mm=30, height_mm=3):
    """Draw the ABB signature red title dash."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    c.setFillColor(HexColor(ABBColor.RED))
    c.rect(x, y, width_mm * mm, height_mm * mm, fill=1, stroke=0)


def draw_section_badge(c, x, y, text, width_mm=28, height_mm=5, font_dir="./fonts"):
    """Draw a red STEP/SECTION badge label."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    c.setFillColor(HexColor(ABBColor.RED))
    c.rect(x, y, width_mm * mm, height_mm * mm, fill=1, stroke=0)
    c.setFillColor(HexColor(ABBColor.WHITE))
    c.setFont(ABBFont.reportlab_name("bold", font_dir), 8)
    c.drawCentredString(x + (width_mm * mm) / 2, y + 1.5 * mm, text.upper())


def draw_card(c, x, y, width, height, fill_hex=None, stroke_hex=None, radius_mm=2):
    """Draw a light gray card background with optional custom colors."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    c.setFillColor(HexColor(fill_hex or ABBColor.GRAY_CARD))
    c.setStrokeColor(HexColor(stroke_hex or ABBColor.GRAY_LINE))
    c.setLineWidth(0.5)
    c.roundRect(x, y, width, height, radius_mm * mm, fill=1, stroke=1)


def draw_red_top_card(c, x, y, width, height, border_height_mm=2.5):
    """Draw a card with the ABB red top accent border."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    draw_card(c, x, y, width, height)
    bh = border_height_mm * mm
    c.setFillColor(HexColor(ABBColor.RED))
    c.rect(x, y + height - bh, width, bh, fill=1, stroke=0)


def draw_abb_logo(c, page_width, page_height, margin_mm=15, size_pt=14, font_dir="./fonts"):
    """Place ABB logo text at bottom-right of page."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    c.setFillColor(HexColor(ABBColor.RED))
    c.setFont(ABBFont.reportlab_name("bold", font_dir), size_pt)
    c.drawRightString(page_width - margin_mm * mm, margin_mm * mm + 2 * mm, "ABB")


def draw_footer(c, page_width, text_left, text_right,
                margin_mm=15, font_dir="./fonts"):
    """Draw the standard ABB copyright footer strip."""
    _require_reportlab()
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    m = margin_mm * mm
    c.setFillColor(HexColor(ABBColor.GRAY_CARD))
    c.rect(0, 0, page_width, m, fill=1, stroke=0)
    c.setFillColor(HexColor(ABBColor.GRAY_MUTE))
    c.setFont(ABBFont.reportlab_name("regular", font_dir), 7)
    c.drawString(m, m - 4 * mm, text_left)
    c.drawRightString(page_width - m - 20 * mm, m - 4 * mm, text_right)


# ─────────────────────────────────────────────────────────────────────────────
# PYTHON-PPTX HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def pptx_set_text(run, text: str, size_pt: float,
                  weight: str = "regular", hex_color: str | None = None):
    """
    Apply ABB Voice font and brand color to a python-pptx text run.

    Args:
        run:       pptx text run object
        text:      string to set
        size_pt:   font size in points
        weight:    'light' | 'regular' | 'medium' | 'bold'
        hex_color: optional hex color string, e.g. '#FF000F'
    """
    from pptx.util import Pt
    run.text = text
    run.font.name = ABBFont.system_name(weight)
    run.font.size = Pt(size_pt)
    run.font.bold = (weight == "bold")
    if hex_color:
        run.font.color.rgb = ABBColor.to_pptx_rgb(hex_color)


def pptx_solid_shape(shape, hex_color: str, border: bool = False,
                     border_color: str | None = None):
    """
    Fill a python-pptx shape with a solid ABB brand color.

    Args:
        shape:        pptx shape object
        hex_color:    fill color as hex string
        border:       whether to draw a border
        border_color: hex string for border; defaults to GRAY_LINE
    """
    from pptx.util import Pt
    shape.fill.solid()
    shape.fill.fore_color.rgb = ABBColor.to_pptx_rgb(hex_color)
    if border:
        shape.line.color.rgb = ABBColor.to_pptx_rgb(
            border_color or ABBColor.GRAY_LINE
        )
        shape.line.width = Pt(0.5)
    else:
        shape.line.fill.background()


# ─────────────────────────────────────────────────────────────────────────────
# CSS TEMPLATE GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

def generate_css_variables() -> str:
    """Return a CSS :root block with all ABB brand variables."""
    return f""":root {{
  /* ABB Brand Colors */
  --abb-red:       {ABBColor.RED};
  --abb-red-dark:  {ABBColor.RED_DARK};
  --abb-white:     {ABBColor.WHITE};
  --abb-black:     {ABBColor.BLACK};
  --abb-gray-text: {ABBColor.GRAY_TEXT};
  --abb-gray-mute: {ABBColor.GRAY_MUTE};
  --abb-gray-card: {ABBColor.GRAY_CARD};
  --abb-gray-line: {ABBColor.GRAY_LINE};
  --abb-dark-bg:   {ABBColor.DARK_BG};

  /* ABB Typography */
  --font-abb: {ABBFont.CSS_STACK};

  /* ABB Spacing */
  --gap-page:    {ABBLayout.MARGIN_PX}px;
  --gap-section: {ABBLayout.SECTION_GAP_PX}px;
  --gap-card:    {ABBLayout.CARD_PAD_PX}px;
  --gap-gutter:  {ABBLayout.GUTTER_PX}px;
  --radius:      {ABBLayout.RADIUS_PX}px;
}}"""


if __name__ == "__main__":
    print("ABB Brand Helper — self-test")
    print(f"ABB Voice installed: {ABBFont.is_installed()}")
    print(f"Font for 'bold': {ABBFont.system_name('bold')}")
    print()
    print(generate_css_variables())
