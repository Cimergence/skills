# ABB Brand — Web / HTML / SVG / Widget

Use this guide when creating HTML artifacts, inline SVG diagrams, React
components, or interactive widgets that must follow ABB's visual identity.

---

## CSS Variables (copy into every project)

```css
:root {
  /* Brand colors */
  --abb-red:       #FF000F;
  --abb-red-dark:  #CC0000;
  --abb-white:     #FFFFFF;
  --abb-black:     #1A1A1A;
  --abb-gray-text: #555555;
  --abb-gray-mute: #888888;
  --abb-gray-card: #F2F2F2;
  --abb-gray-line: #E8E8E8;
  --abb-dark-bg:   #141414;

  /* Typography */
  --font-abb: "ABB Voice", "Barlow", "Arial Narrow", Arial, Helvetica, sans-serif;

  /* Spacing */
  --gap-page:    32px;
  --gap-section: 24px;
  --gap-card:    16px;
  --gap-gutter:  8px;
  --radius:      4px;
}
```

---

## Font Loading

ABB Voice is a proprietary typeface. Load it from the user's local system or
from a self-hosted path. Always include the full fallback stack.

```css
/* Option A: Local system install (requires ABB Voice to be installed) */
@font-face {
  font-family: "ABB Voice";
  src: local("ABB Voice Light"),    local("ABBVoice-Light");
  font-weight: 300;
}
@font-face {
  font-family: "ABB Voice";
  src: local("ABB Voice"),          local("ABBVoice");
  font-weight: 400;
}
@font-face {
  font-family: "ABB Voice";
  src: local("ABB Voice Medium"),   local("ABBVoice-Medium");
  font-weight: 500;
}
@font-face {
  font-family: "ABB Voice";
  src: local("ABB Voice Bold"),     local("ABBVoice-Bold");
  font-weight: 700;
}

/* Option B: Self-hosted (place .ttf files in /fonts/) */
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Light.ttf")  format("truetype");
  font-weight: 300;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice.ttf")        format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Medium.ttf") format("truetype");
  font-weight: 500;
}
@font-face {
  font-family: "ABB Voice";
  src: url("/fonts/ABBVoice-Bold.ttf")   format("truetype");
  font-weight: 700;
}

/* Fallback when ABB Voice is unavailable (Google Font) */
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800;900&family=Barlow:wght@400;500;600;700&display=swap');
```

---

## Typography Scale

```css
/* Page / poster title */
.title-xl {
  font-family: var(--font-abb);
  font-size: 32px;
  font-weight: 700;    /* Bold */
  line-height: 1.05;
  color: var(--abb-black);
  letter-spacing: 0.3px;
}

/* Section heading */
.title-section {
  font-family: var(--font-abb);
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--abb-black);
}

/* Body copy */
.body {
  font-family: var(--font-abb);
  font-size: 13px;
  font-weight: 400;
  line-height: 1.6;
  color: var(--abb-black);
}

/* Caption / metadata */
.caption {
  font-family: var(--font-abb);
  font-size: 10px;
  font-weight: 400;
  color: var(--abb-gray-mute);
  letter-spacing: 0.5px;
}

/* Large stat callout */
.stat {
  font-family: var(--font-abb);
  font-size: 28px;
  font-weight: 700;
  color: var(--abb-red);
  line-height: 1;
}
```

---

## Core Component Patterns

### Red dash title block

```html
<div class="title-block">
  <span class="red-dash"></span>
  <h1 class="title-xl">Emergency Response</h1>
  <p class="caption">ABB Switzerland · Safety / HSE</p>
</div>

<style>
.title-block { padding: 20px 32px 16px; }
.red-dash {
  display: block;
  width: 32px; height: 4px;
  background: var(--abb-red);
  margin-bottom: 8px;
}
</style>
```

### Section header with step badge

```html
<div class="sec-header">
  <span class="sec-badge">STEP 1</span>
  <span class="sec-title">Identify the problem</span>
</div>

<style>
.sec-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 24px 10px;
  border-bottom: 1px solid var(--abb-gray-line);
}
.sec-header::before {
  content: '';
  display: inline-block;
  width: 18px; height: 3px;
  background: var(--abb-red);
  flex-shrink: 0;
}
.sec-badge {
  background: var(--abb-red);
  color: #fff;
  font-family: var(--font-abb);
  font-size: 11px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 2px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.sec-title {
  font-family: var(--font-abb);
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--abb-black);
}
</style>
```

### Red icon square

```html
<!-- 28x28 red tile with white SVG icon -->
<div class="icon-tile">
  <svg viewBox="0 0 24 24"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>
</div>

<style>
.icon-tile {
  width: 28px; height: 28px;
  background: var(--abb-red);
  border-radius: 3px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.icon-tile svg { width: 16px; height: 16px; fill: #fff; }
</style>
```

### Light gray card row

```html
<div class="card-row">
  <div class="icon-tile"><!-- svg --></div>
  <div class="card-row-text">
    <div class="card-row-label">Situation label</div>
    <div class="card-row-title">Main action or description</div>
  </div>
  <span class="card-row-cta">→ Section 3</span>
</div>

<style>
.card-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 24px;
  border-bottom: 1px solid var(--abb-gray-card);
  background: var(--abb-white);
}
.card-row:hover { background: var(--abb-gray-card); }
.card-row-label { font-size: 11px; color: var(--abb-gray-mute); }
.card-row-title { font-size: 13px; font-weight: 600; color: var(--abb-black); }
.card-row-cta {
  margin-left: auto;
  background: var(--abb-gray-card);
  border-radius: 3px;
  padding: 4px 10px;
  font-family: var(--font-abb);
  font-size: 12px;
  font-weight: 700;
  color: var(--abb-red);
}
</style>
```

### Contact card (red top border)

```html
<div class="contact-card">
  <div class="contact-label">Medical emergency</div>
  <div class="contact-who">First Helper / ADZ</div>
  <div class="contact-num">058 58 5 41 01</div>
  <div class="contact-extra">Available 24/7</div>
</div>

<style>
.contact-card {
  background: var(--abb-gray-card);
  border-top: 3px solid var(--abb-red);
  border-radius: var(--radius);
  padding: 10px 12px;
}
.contact-label {
  font-size: 9px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--abb-gray-mute);
  margin-bottom: 3px;
}
.contact-who {
  font-family: var(--font-abb);
  font-size: 14px;
  font-weight: 700;
  color: var(--abb-black);
  margin-bottom: 3px;
}
.contact-num {
  font-family: var(--font-abb);
  font-size: 18px;
  font-weight: 700;
  color: var(--abb-red);
  line-height: 1.1;
}
.contact-extra { font-size: 10px; color: var(--abb-gray-mute); margin-top: 3px; }
</style>
```

### Red chevron step connector

```html
<!-- Use between horizontal step boxes -->
<div class="chevron-right"></div>

<style>
.chevron-right {
  width: 0; height: 0;
  border-top: 9px solid transparent;
  border-bottom: 9px solid transparent;
  border-left: 14px solid var(--abb-red);
  flex-shrink: 0;
}
</style>
```

### ABB logo block (bottom-right placement)

```html
<div class="abb-logo">
  <div class="abb-logo-mark">ABB</div>
  <div class="abb-logo-sub">v0.1.4 · Safety / HSE</div>
</div>

<style>
.abb-logo { display: flex; flex-direction: column; align-items: flex-end; gap: 2px; }
.abb-logo-mark {
  font-family: var(--font-abb);
  font-size: 26px;
  font-weight: 700;
  color: var(--abb-red);
  letter-spacing: 5px;
  line-height: 1;
}
.abb-logo-sub { font-size: 10px; color: var(--abb-gray-mute); letter-spacing: 1px; }
</style>
```

### Footer strip

```html
<footer class="abb-footer">
  <span>© 2026 ABB Switzerland. All rights reserved.</span>
  <span>Document ref: v0.1.4</span>
  <div class="abb-logo-mark" style="font-size:20px;letter-spacing:4px;color:var(--abb-red)">ABB</div>
</footer>

<style>
.abb-footer {
  background: var(--abb-gray-card);
  border-top: 1px solid var(--abb-gray-line);
  padding: 8px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10px;
  color: var(--abb-gray-mute);
}
</style>
```

---

## SVG Diagrams — Brand Rules

When building SVG diagrams within ABB materials:

- **Accent color**: use `#FF000F` only for active/highlight nodes, arrows, and borders
- **Neutral nodes**: use `#F2F2F2` fill + `#E8E8E8` stroke
- **Text**: `#1A1A1A` primary, `#888888` secondary; minimum 12px
- **Arrows**: `stroke="#FF000F"` with filled arrowhead for decision flows
- **No rounded corners beyond rx="4"** unless drawing pill shapes intentionally
- **Section label convention**: short ALLCAPS badge in `#FF000F` background + white text

```svg
<!-- Branded arrow marker for SVG -->
<defs>
  <marker id="abb-arrow" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
          stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<!-- Usage -->
<line x1="100" y1="50" x2="200" y2="50"
      stroke="#FF000F" stroke-width="1.5"
      marker-end="url(#abb-arrow)"/>
```

---

## Don'ts

- ❌ Never use a second accent color alongside `#FF000F`
- ❌ Never use purple, teal, orange, or blue as ABB accent colors
- ❌ Never replace the red dash motif with an underline on titles
- ❌ Never place the ABB logo anywhere other than bottom-right
- ❌ Never use font-weight 600 — ABB Voice has no 600 weight; use 500 or 700
- ❌ Never use all-caps for body text — only for labels and badges
- ❌ Never set font-size below 10px in any user-facing element
