# Modern-Quilt Jekyll Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the GitHub Pages config and replace the visual design with a modern-quilt theme (bold solids, animated stitching, Bricolage Grotesque + Inter), without touching the content of weekly modules, readings, or exercises.

**Architecture:** Pure Jekyll — no JS framework, no bundler, no build step beyond `jekyll build`. The design system lives in `assets/css/style.css` and a small set of `_includes`. The schedule grid is rendered by a Liquid loop over `site.pages` filtered to `/weeks/`, reading new `kind` and `theme` keys we'll add to each weekly module's YAML front-matter.

**Tech Stack:** Jekyll (GitHub Pages gem), Liquid templates, vanilla CSS (custom properties, `@keyframes`, variable-font `font-variation-settings`), one inline SVG for the animated stitch border. Google Fonts: Bricolage Grotesque + Inter + JetBrains Mono.

---

## Spec reference

Approved spec: `docs/superpowers/specs/2026-04-27-fiber-arts-jekyll-design.md`. Re-read it before starting.

## Note on testing

There is no test runner in this repo (it's a static-site theme). "Verification" in each task means running `bundle exec jekyll build` (must succeed with no errors) and visiting the local server (`bundle exec jekyll serve`) at `http://localhost:4000/NEH_AI_DH/` to confirm the visible behavior described. A task is not complete until both succeed.

## File structure

| Path | Disposition | Owns |
|---|---|---|
| `_config.yml` | modify | site metadata, baseurl, plugins |
| `Gemfile` | create | github-pages + relative-links + webrick |
| `.gitignore` | already exists, augmented in spec commit | exclude `_site/`, caches, `.superpowers/` |
| `_data/` | (not used) | — front-matter loop reads from `site.pages` instead |
| `_includes/header.html` | modify | site title, plus-sign decoration, nav |
| `_includes/footer.html` | modify | ink-on-bone footer with stitched rule above |
| `_includes/weeks-grid.html` | create | Liquid loop rendering the 12 week blocks |
| `_layouts/default.html` | modify | font preconnect + skip link + page wrap |
| `assets/css/style.css` | rewrite | the entire design system |
| `weeks/week-01.md` … `week-12.md` | modify (front-matter only) | add `kind:` and `theme:` keys |
| `index.md` | modify | replace markdown schedule table + weekly-modules list with `{% include weeks-grid.html %}` |
| `README.md` | modify | document design system, preview command, GH Pages source |

Bodies of `weeks/*.md`, `readings.md`, and `exercises.md` are **not** edited.

---

## Task 1: GitHub Pages plumbing — `_config.yml`, `Gemfile`

**Files:**
- Modify: `_config.yml`
- Create: `Gemfile`

- [ ] **Step 1: Rewrite `_config.yml`**

```yaml
title: NEH DH+AI Workshop Series
description: Building a Digital Humanities Generative AI Learning Community at UCF — Summer 2026
baseurl: "/NEH_AI_DH"
url: "https://amsucf.github.io"

markdown: kramdown
kramdown:
  input: GFM
  auto_ids: true

plugins:
  - jekyll-seo-tag
  - jekyll-relative-links

# jekyll-relative-links rewrites .md links in markdown bodies to the
# rendered .html URL — keeps existing weeks/week-NN.md hrefs working.
relative_links:
  enabled: true
  collections: false

defaults:
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "default"

exclude:
  - README.md
  - LICENSE
  - Gemfile
  - Gemfile.lock
  - vendor
  - docs
  - .superpowers
```

- [ ] **Step 2: Create `Gemfile`**

```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-relative-links"
end
```

- [ ] **Step 3: Install gems**

Run: `bundle install`
Expected: completes without error. On Windows, if it fails on a native gem, run `bundle config set --local force_ruby_platform true` first and retry.

- [ ] **Step 4: Confirm a clean build**

Run: `bundle exec jekyll build`
Expected: prints "done in X seconds" with no warnings beyond the existing site (the legacy CSS still applies; that gets replaced in Task 4).

- [ ] **Step 5: Commit**

```bash
git add _config.yml Gemfile
git commit -m "fix(jekyll): correct baseurl, add Gemfile + relative-links"
```

---

## Task 2: Front-matter augmentation — add `kind` and `theme` to each week

**Files:**
- Modify: `weeks/week-01.md` through `weeks/week-12.md` (front-matter only — never the body)

The schedule grid needs two new keys per page: `kind` (`workshop` or `async`) and `theme` (the short headline shown in the grid block).

- [ ] **Step 1: Edit each week's front-matter**

For each file, add the two keys immediately after `title:`. The exact values are below — do not paraphrase, these match the schedule table on the current `index.md`:

`weeks/week-01.md` — add:
```yaml
kind: workshop
theme: "LLMs, models, harnesses, the higher-ed crisis"
```

`weeks/week-02.md` — add:
```yaml
kind: async
theme: "LLM fundamentals reinforcement"
```

`weeks/week-03.md` — add:
```yaml
kind: workshop
theme: "Text analysis with Claude Projects"
```

`weeks/week-04.md` — add:
```yaml
kind: async
theme: "Distant reading reinforcement"
```

`weeks/week-05.md` — add:
```yaml
kind: workshop
theme: "Visual analysis with Claude Artifacts"
```

`weeks/week-06.md` — add:
```yaml
kind: async
theme: "Image generation, detection, and visual ethics"
```

`weeks/week-07.md` — add:
```yaml
kind: workshop
theme: "Building interactive tools with Claude Code Web"
```

`weeks/week-08.md` — add:
```yaml
kind: async
theme: "Code Web reinforcement: rebuild a static handout"
```

`weeks/week-09.md` — add:
```yaml
kind: workshop
theme: "Playful, accessible, creative code; AI policy drafting"
```

`weeks/week-10.md` — add:
```yaml
kind: async
theme: "UDL and AI syllabus policy"
```

`weeks/week-11.md` — add:
```yaml
kind: workshop
theme: "Cowork, Claude CLI, agentic futures"
```

`weeks/week-12.md` — add:
```yaml
kind: async
theme: "Sustainability, sharing, final reflection"
```

- [ ] **Step 2: Verify with a quick Liquid sanity check**

Add a temporary block to the **bottom** of `index.md`:

```liquid
{% assign weekpages = site.pages | where_exp:"p","p.week" | sort:"week" %}
{% for w in weekpages %}- {{ w.week }} / {{ w.kind }} / {{ w.theme }} / {{ w.url }}
{% endfor %}
```

Run: `bundle exec jekyll serve`
Visit: `http://localhost:4000/NEH_AI_DH/`
Expected: at the bottom of the page, a list of 12 lines reading e.g. `1 / workshop / LLMs, models, harnesses, the higher-ed crisis / /NEH_AI_DH/weeks/week-01.html`. Order is 1→12.

- [ ] **Step 3: Remove the temporary block**

Delete the Liquid block from `index.md`.

- [ ] **Step 4: Commit**

```bash
git add weeks/ index.md
git commit -m "data: add kind+theme front-matter to weekly modules"
```

---

## Task 3: Skeleton layout + font loading + skip link

**Files:**
- Modify: `_layouts/default.html`

- [ ] **Step 1: Replace `_layouts/default.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title | default: site.title }}</title>
  <meta name="description" content="{{ page.description | default: site.description }}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..125,400;12..96,75..125,600;12..96,75..125,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
  {% seo %}
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>

  {% include header.html %}

  <main id="main-content" class="content-wrap" tabindex="-1">
    <article class="page-content">
      {{ content }}
    </article>
  </main>

  {% include footer.html %}
</body>
</html>
```

- [ ] **Step 2: Build and confirm**

Run: `bundle exec jekyll build`
Expected: no errors. The site still uses the old header/footer/CSS — that's fine, this task only swaps the shell.

- [ ] **Step 3: Commit**

```bash
git add _layouts/default.html
git commit -m "layout: load Bricolage+Inter+JetBrains, add skip link"
```

---

## Task 4: Replace `style.css` with the design-system foundation

**Files:**
- Modify: `assets/css/style.css` (full rewrite)

This is the largest single edit. Tasks 5–9 then add components on top of the foundation.

- [ ] **Step 1: Replace `assets/css/style.css` with the foundation**

```css
/* ============================================================
   NEH DH+AI Workshop Series — Modern-Quilt Design System
   ============================================================ */

:root {
  /* Palette */
  --bone:   #faf6ec;
  --paper:  #ffffff;
  --ink:    #141414;
  --rule:   #1a1a1a;
  --muted:  #5a5a5a;
  --coral:  #ff5a4e;
  --cobalt: #1545c4;
  --mustard:#e8b53a;
  --sage:   #7a8f4a;
  --plum:   #5d2e5f;

  /* Type */
  --display: "Bricolage Grotesque", "Inter", system-ui, sans-serif;
  --sans:    "Inter", system-ui, sans-serif;
  --mono:    "JetBrains Mono", Menlo, monospace;

  /* Layout */
  --max-width: 64rem;
  --gutter: 1.5rem;
}

*, *::before, *::after { box-sizing: border-box; }

html { font-size: 17px; -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--bone);
  color: var(--ink);
  font-family: var(--sans);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

/* Skip link */
.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
  background: var(--ink);
  color: var(--bone);
  padding: 0.6rem 1rem;
  font-family: var(--sans);
  font-weight: 600;
  text-decoration: none;
  z-index: 100;
}
.skip-link:focus { left: 0; }

/* Focus visible — independent of any decorative animation */
:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

/* Layout */
.content-wrap {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 2.5rem var(--gutter) 3rem;
}

.page-content > :first-child { margin-top: 0; }

/* Headings — variable Bricolage with optical-size scaling */
.page-content h1,
.page-content h2,
.page-content h3,
.page-content h4 {
  font-family: var(--display);
  color: var(--ink);
  line-height: 1.05;
  letter-spacing: -0.02em;
  margin: 2.4rem 0 0.6rem;
}

.page-content h1 {
  font-size: clamp(2rem, 4.5vw, 3rem);
  font-variation-settings: "opsz" 96, "wdth" 108, "wght" 700;
  margin-top: 0.5rem;
  animation: heroRise 480ms cubic-bezier(.2,.7,.2,1) both;
}

.page-content h2 {
  font-size: clamp(1.45rem, 2.6vw, 1.85rem);
  font-variation-settings: "opsz" 48, "wdth" 105, "wght" 700;
}

.page-content h3 {
  font-size: 1.18rem;
  font-variation-settings: "opsz" 24, "wdth" 100, "wght" 600;
}

.page-content h4 {
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 600;
  margin-top: 1.6rem;
}

@keyframes heroRise {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Body copy */
.page-content p { margin: 0.7rem 0 1rem; max-width: 42rem; }
.page-content ul,
.page-content ol { padding-left: 1.4rem; max-width: 42rem; }
.page-content li { margin: 0.35rem 0; }

/* Links */
a {
  color: var(--cobalt);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 2px;
  text-decoration-style: dashed;
}
a:hover, a:focus {
  color: var(--ink);
  text-decoration-style: solid;
  text-decoration-color: var(--coral);
}

/* Code */
.page-content code {
  font-family: var(--mono);
  font-size: 0.9em;
  background: rgba(232, 181, 58, 0.22);
  padding: 0.1rem 0.35rem;
  border-radius: 2px;
}
.page-content pre {
  font-family: var(--mono);
  background: var(--ink);
  color: var(--bone);
  padding: 1rem 1.1rem;
  border: 2px solid var(--ink);
  overflow-x: auto;
  font-size: 0.88em;
  line-height: 1.55;
}
.page-content pre code { background: transparent; padding: 0; color: inherit; }

/* Blockquote */
.page-content blockquote {
  border-left: 4px solid var(--coral);
  margin: 1.2rem 0;
  padding: 0.4rem 1rem;
  color: var(--muted);
  background: transparent;
  font-style: italic;
}

/* Tables (the readings page uses several; the schedule table on index is replaced by the grid) */
.page-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.4rem 0;
  font-family: var(--sans);
  font-size: 0.95rem;
  border: 2px solid var(--ink);
}
.page-content th,
.page-content td {
  border: 1px solid var(--ink);
  padding: 0.55rem 0.7rem;
  text-align: left;
  vertical-align: top;
}
.page-content th {
  background: var(--mustard);
  color: var(--ink);
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-size: 0.82rem;
}

/* Horizontal rule — animated stitch (Task 7 adds the .stitch-divider class; bare <hr> falls back) */
.page-content hr {
  border: 0;
  height: 4px;
  background-image: linear-gradient(90deg, var(--ink) 0 8px, transparent 8px 16px);
  background-size: 16px 4px;
  background-repeat: repeat-x;
  margin: 2rem 0;
}

/* Reduced-motion gate — kill decorative animations, keep state changes */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}

@media (max-width: 640px) {
  html { font-size: 16px; }
  .content-wrap { padding: 1.75rem var(--gutter) 2rem; }
}
```

- [ ] **Step 2: Build and visit `index.md`**

Run: `bundle exec jekyll serve`
Visit: `http://localhost:4000/NEH_AI_DH/`
Expected: bone background, headings in Bricolage Grotesque (visibly different from the old serif), body in Inter, dashed-underline links in cobalt that turn coral on hover. The old header/footer still show because they haven't been rewritten yet — that's fine.

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "css: rewrite design system foundation (palette, type, base)"
```

---

## Task 5: Header — plus-sign decoration, title, nav with stitch hover

**Files:**
- Modify: `_includes/header.html`
- Append to: `assets/css/style.css`

- [ ] **Step 1: Replace `_includes/header.html`**

```html
<header class="site-header" role="banner">
  <div class="header-content">
    <span class="header-plus" aria-hidden="true"></span>
    <div class="header-titles">
      <a class="site-title-link" href="{{ '/' | relative_url }}">
        <h1 class="site-title">{{ site.title }}</h1>
      </a>
      <p class="site-tagline">{{ site.description }}</p>
    </div>
    <nav class="site-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}" class="nav-link{% if page.url == '/' %} is-active{% endif %}">Overview</a>
      <a href="{{ '/readings.html' | relative_url }}" class="nav-link{% if page.url contains 'readings' %} is-active{% endif %}">Readings</a>
      <a href="{{ '/exercises.html' | relative_url }}" class="nav-link{% if page.url contains 'exercises' %} is-active{% endif %}">Exercises</a>
    </nav>
  </div>
</header>
```

- [ ] **Step 2: Append the header CSS to `assets/css/style.css`**

Append at the end of the file:

```css
/* ===== Site header ===== */
.site-header {
  background: var(--bone);
  border-bottom: 2px solid var(--ink);
  padding: 2.25rem var(--gutter) 1.75rem;
  position: relative;
  overflow: hidden;
}

.header-content {
  max-width: var(--max-width);
  margin: 0 auto;
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-areas:
    "plus titles"
    "nav  nav";
  column-gap: 1.25rem;
  row-gap: 1.25rem;
  align-items: center;
}

.header-plus {
  grid-area: plus;
  position: relative;
  width: 56px;
  height: 56px;
  display: block;
  animation: plusTurn 18s linear infinite;
  flex-shrink: 0;
}
.header-plus::before,
.header-plus::after {
  content: "";
  position: absolute;
  background: var(--coral);
}
.header-plus::before {
  left: 50%; top: 0; bottom: 0;
  width: 12px; transform: translateX(-50%);
}
.header-plus::after {
  top: 50%; left: 0; right: 0;
  height: 12px; transform: translateY(-50%);
}
@keyframes plusTurn { to { transform: rotate(360deg); } }

.header-titles { grid-area: titles; min-width: 0; }

.site-title-link { text-decoration: none; color: inherit; display: inline-block; }
.site-title-link:hover, .site-title-link:focus { color: inherit; text-decoration: none; }

.site-title {
  font-family: var(--display);
  font-variation-settings: "opsz" 96, "wdth" 110, "wght" 700;
  font-size: clamp(1.6rem, 3.6vw, 2.4rem);
  letter-spacing: -0.025em;
  margin: 0 0 0.15rem;
  line-height: 1;
  color: var(--ink);
  animation: none; /* override the .page-content h1 hero animation */
}

.site-tagline {
  font-family: var(--sans);
  font-style: italic;
  margin: 0;
  color: var(--muted);
  font-size: 0.98rem;
  max-width: 38rem;
}

/* Nav */
.site-nav {
  grid-area: nav;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  border-top: 1px dashed var(--ink);
  padding-top: 1rem;
}

.nav-link {
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 600;
  font-size: 0.95rem;
  letter-spacing: 0.02em;
  color: var(--ink);
  text-decoration: none;
  position: relative;
  padding-bottom: 8px;
  text-transform: uppercase;
}
.nav-link::after {
  content: "";
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 3px;
  width: 0;
  background-image: linear-gradient(90deg, var(--coral) 0 6px, transparent 6px 12px);
  background-size: 12px 3px;
  background-repeat: repeat-x;
  transition: width 380ms cubic-bezier(.55,.06,.26,1);
}
.nav-link:hover::after,
.nav-link:focus::after,
.nav-link.is-active::after { width: 100%; }
.nav-link:hover, .nav-link:focus { color: var(--ink); text-decoration: none; }

@media (max-width: 640px) {
  .header-plus { width: 40px; height: 40px; }
  .header-plus::before { width: 9px; }
  .header-plus::after  { height: 9px; }
  .site-nav { gap: 1rem; }
  .nav-link { font-size: 0.85rem; }
}
```

- [ ] **Step 3: Verify in browser**

Run (or refresh) `bundle exec jekyll serve`.
Visit `http://localhost:4000/NEH_AI_DH/`.
Expected:
1. Bone background with a slowly rotating coral plus-sign top-left of the header.
2. Site title in big Bricolage Grotesque, italic Inter tagline below.
3. Nav with three links underneath a dashed ink rule.
4. Hover any nav link — a coral running-stitch underline draws left-to-right (~380ms).
5. The Overview link shows the stitched underline persistently because we're on `/`.

- [ ] **Step 4: Commit**

```bash
git add _includes/header.html assets/css/style.css
git commit -m "header: rotating plus, Bricolage title, stitch-hover nav"
```

---

## Task 6: Weeks-grid include and `index.md` integration

**Files:**
- Create: `_includes/weeks-grid.html`
- Modify: `index.md`
- Append to: `assets/css/style.css`

The grid is the marquee element of the page. It replaces the existing markdown schedule table AND the duplicated weekly-modules link list — they collapse into one source.

- [ ] **Step 1: Create `_includes/weeks-grid.html`**

```liquid
{% assign weekpages = site.pages | where_exp:"p","p.week" | sort:"week" %}
{%- assign workshop_colors = "coral,cobalt,mustard,plum,coral,cobalt" | split: "," -%}
{%- assign workshop_seen = 0 -%}
<ol class="weeks-grid" aria-label="Twelve-week schedule">
{% for w in weekpages %}
  {%- if w.kind == "workshop" -%}
    {%- assign color = workshop_colors[workshop_seen] -%}
    {%- assign workshop_seen = workshop_seen | plus: 1 -%}
    {%- assign block_class = "is-workshop is-color-" | append: color -%}
    {%- assign label = "Workshop" -%}
  {%- else -%}
    {%- assign block_class = "is-async" -%}
    {%- assign label = "Async" -%}
  {%- endif %}
  <li class="week-block {{ block_class }}">
    <a class="week-block-link" href="{{ w.url | relative_url }}">
      <span class="week-num">W{{ w.week }}</span>
      <span class="week-kind">{{ label }}</span>
      <span class="week-theme">{{ w.theme }}</span>
      {% if w.workshop.date %}<span class="week-date">{{ w.workshop.date | date: "%a %b %-d" }}</span>{% endif %}
    </a>
  </li>
{% endfor %}
</ol>
```

- [ ] **Step 2: Append the grid CSS**

Append to `assets/css/style.css`:

```css
/* ===== Weeks grid (the quilt top) ===== */
.weeks-grid {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0 2rem;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
  border: 2px solid var(--ink);
  background: var(--ink); /* shows as the seams between blocks */
  max-width: none;
}

.week-block {
  position: relative;
  background: var(--bone);
  margin: 0;
  border: 0;
  outline: 1px solid var(--ink); /* gives every block a clean ink seam */
  transition: transform 220ms ease, box-shadow 220ms ease, z-index 0s linear 220ms;
}

.week-block:hover { z-index: 2; transform: translate(-3px, -3px); box-shadow: 6px 6px 0 var(--ink); transition: transform 220ms ease, box-shadow 220ms ease; }

.week-block-link {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 1.1rem 1rem 1rem;
  text-decoration: none;
  color: inherit;
  min-height: 9.5rem;
}
.week-block-link:hover, .week-block-link:focus { text-decoration: none; color: inherit; }

.week-num {
  font-family: var(--display);
  font-variation-settings: "opsz" 96, "wdth" 115, "wght" 700;
  font-size: 2.6rem;
  line-height: 1;
  letter-spacing: -0.04em;
}
.week-kind {
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 700;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}
.week-theme {
  font-family: var(--sans);
  font-size: 0.9rem;
  line-height: 1.35;
  margin-top: auto;
}
.week-date {
  font-family: var(--mono);
  font-size: 0.72rem;
  margin-top: 0.4rem;
  opacity: 0.85;
}

/* Workshop color rotation */
.week-block.is-color-coral   { background: var(--coral);   color: var(--bone); }
.week-block.is-color-cobalt  { background: var(--cobalt);  color: var(--bone); }
.week-block.is-color-mustard { background: var(--mustard); color: var(--ink); }
.week-block.is-color-plum    { background: var(--plum);    color: var(--bone); }
.week-block.is-async         { background: var(--bone);    color: var(--ink); }

@media (max-width: 880px) {
  .weeks-grid { grid-template-columns: repeat(2, 1fr); }
  .week-num { font-size: 2.2rem; }
  .week-block-link { min-height: 8rem; }
}
@media (max-width: 480px) {
  .weeks-grid { grid-template-columns: 1fr; }
  .week-block-link { min-height: 0; padding: 0.85rem 1rem 1rem; }
}
```

- [ ] **Step 3: Update `index.md` — replace the schedule table and weekly-modules list**

In `index.md`, remove:

1. The entire `## Schedule` section's markdown table (the `| Week | Of | In-person | Theme |` table and its body — keep the `## Schedule` heading and the lead sentence above the table).
2. The entire `## Weekly Modules` bulleted list under that heading (keep the heading).

Replace **both** sections' table/list contents with `{% include weeks-grid.html %}`. Concretely:

After the lead sentence under `## Schedule`, insert:
```liquid
{% include weeks-grid.html %}
```

Under `## Weekly Modules`, replace the bullet list with a one-line note:
```markdown
The grid above links to each module. Workshop weeks are colored; async weeks are bone.
```

(Do not touch any other section of `index.md`.)

- [ ] **Step 4: Verify in browser**

Refresh `http://localhost:4000/NEH_AI_DH/`.
Expected:
1. Under "Schedule," a 4-up grid (3 rows of 4) showing W1–W12.
2. Workshop weeks (1, 3, 5, 7, 9, 11) carry the color rotation coral→cobalt→mustard→plum→coral→cobalt.
3. Async weeks (2, 4, 6, 8, 10, 12) are bone with a 1px ink seam.
4. Hover any block: it lifts -3px / -3px and grows a 6px ink offset shadow.
5. Click W1: lands on `/NEH_AI_DH/weeks/week-01.html`.
6. Resize the window narrower: grid collapses to 2-up, then 1-up.

- [ ] **Step 5: Commit**

```bash
git add _includes/weeks-grid.html index.md assets/css/style.css
git commit -m "feat: schedule renders as a modern-quilt grid from front-matter"
```

---

## Task 7: Workshop & async callouts (animated stitched border)

**Files:**
- Append to: `assets/css/style.css`

The existing markdown bodies use `<div class="workshop-callout" markdown="1">` and `<div class="async-callout" markdown="1">`. We restyle those classes; the markdown stays as-is, so we don't have to touch any of the 12 weekly files.

The "stitched border" is achieved with four `linear-gradient` backgrounds (top / bottom / left / right edges) on a `::after` pseudo-element. Animating `background-position` makes the dashes appear to march around the frame — purer CSS, no SVG, no JS.

- [ ] **Step 1: Append the callout CSS**

```css
/* ===== Workshop callout — animated stitched border ===== */
.workshop-callout {
  position: relative;
  background: var(--paper);
  padding: 1.1rem 1.35rem;
  margin: 1.5rem 0;
  font-family: var(--sans);
  isolation: isolate;
}
.workshop-callout strong {
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 700;
  color: var(--cobalt);
}
.workshop-callout::before {
  content: "";
  position: absolute;
  inset: 0;
  border: 2px solid var(--ink);
  pointer-events: none;
}
.workshop-callout::after {
  content: "";
  position: absolute;
  inset: 4px;
  pointer-events: none;
  background:
    linear-gradient(90deg, var(--coral) 50%, transparent 0) repeat-x top    left  / 16px 3px,
    linear-gradient(90deg, var(--coral) 50%, transparent 0) repeat-x bottom left  / 16px 3px,
    linear-gradient(0deg,  var(--coral) 50%, transparent 0) repeat-y left   top   / 3px 16px,
    linear-gradient(0deg,  var(--coral) 50%, transparent 0) repeat-y right  top   / 3px 16px;
  animation: stitchRun 18s linear infinite;
}
@keyframes stitchRun {
  to {
    background-position:
      16px top,
      -16px bottom,
      left -16px,
      right 16px;
  }
}

/* ===== Async callout — calmer, non-animated counterpart ===== */
.async-callout {
  position: relative;
  background: rgba(232, 181, 58, 0.18);
  border: 2px dashed var(--ink);
  padding: 1.1rem 1.35rem;
  margin: 1.5rem 0;
  font-family: var(--sans);
}
.async-callout strong {
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 700;
  color: var(--ink);
}
```

- [ ] **Step 2: Verify**

Visit `http://localhost:4000/NEH_AI_DH/weeks/week-01.html`.
Expected: the workshop callout has a white background, a solid 2px ink border, and an inset coral stitched border whose dashes march continuously around the frame.

Visit `http://localhost:4000/NEH_AI_DH/weeks/week-02.html`.
Expected: async callout has a dashed ink border on a warm mustard tint, no animation.

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "components: workshop+async callouts with marching stitch border"
```

---

## Task 8: Tags (Light/Standard/Deep) and stitch divider

**Files:**
- Append to: `assets/css/style.css`

- [ ] **Step 1: Append tag + divider CSS**

```css
/* ===== Reading-time tags ===== */
.tag {
  display: inline-block;
  font-family: var(--display);
  font-variation-settings: "opsz" 14, "wdth" 100, "wght" 700;
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.18rem 0.6rem;
  margin-right: 0.4rem;
  border: 2px solid var(--ink);
  background: var(--bone);
  color: var(--ink);
  white-space: nowrap;
}
.tag-light    { background: var(--sage);    color: var(--bone); }
.tag-standard { background: var(--mustard); color: var(--ink); }
.tag-deep     { background: var(--plum);    color: var(--bone); }

/* ===== Animated stitch divider — opt-in via class ===== */
.stitch-divider {
  height: 4px;
  margin: 2.25rem auto;
  max-width: 100%;
  background-image: linear-gradient(90deg, var(--ink) 0 8px, transparent 8px 16px);
  background-size: 16px 4px;
  background-repeat: repeat-x;
  animation: stitchDraw 1.4s 0.1s cubic-bezier(.55,.06,.26,1) both;
  width: 100%;
  transform-origin: left center;
}
@keyframes stitchDraw {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

- [ ] **Step 2: Verify**

Visit `http://localhost:4000/NEH_AI_DH/readings.html`.
Expected: every `<span class="tag tag-light">Light</span>` etc. renders as a hard-bordered uppercase pill in the right color (sage / mustard / plum). All three colors meet contrast.

(The animated divider isn't emitted automatically — markdown `---` produces a static `<hr>`. The class is available for future Liquid-rendered dividers; the static hr already gets the dashed look from Task 4. No verification needed beyond build success.)

- [ ] **Step 3: Commit**

```bash
git add assets/css/style.css
git commit -m "css: tags pills + animated stitch-divider class"
```

---

## Task 9: Footer

**Files:**
- Modify: `_includes/footer.html`
- Append to: `assets/css/style.css`

- [ ] **Step 1: Replace `_includes/footer.html`**

```html
<footer class="site-footer" role="contentinfo">
  <div class="footer-content">
    <div class="footer-stitch" aria-hidden="true"></div>
    <p class="footer-copy">
      Building a Digital Humanities Generative AI Learning Community
      &middot; National Endowment for the Humanities
      &middot; University of Central Florida
      &middot; &copy; {{ 'now' | date: "%Y" }}
    </p>
    <p class="footer-note">
      This material is based upon work supported by the National Endowment for the Humanities.
      Any views, findings, conclusions, or recommendations expressed do not necessarily reflect those of the NEH.
    </p>
  </div>
</footer>
```

- [ ] **Step 2: Append the footer CSS**

```css
/* ===== Site footer ===== */
.site-footer {
  background: var(--bone);
  color: var(--ink);
  padding: 2.5rem var(--gutter) 3rem;
  margin-top: 4rem;
  border-top: 2px solid var(--ink);
}
.footer-content {
  max-width: var(--max-width);
  margin: 0 auto;
  font-family: var(--sans);
  font-size: 0.9rem;
  line-height: 1.55;
  position: relative;
}
.footer-stitch {
  height: 4px;
  margin: 0 0 1.5rem;
  background-image: linear-gradient(90deg, var(--coral) 0 8px, transparent 8px 16px);
  background-size: 16px 4px;
  background-repeat: repeat-x;
}
.footer-copy { margin: 0 0 0.6rem; color: var(--ink); }
.footer-note { margin: 0; color: var(--muted); font-style: italic; max-width: 56rem; }
```

- [ ] **Step 3: Verify**

Refresh any page. Footer expected:
- Ink-on-bone block at the bottom with a 2px ink rule above it.
- A coral stitched rule inside, above the copy line.
- Copy line and italic NEH note legible.

- [ ] **Step 4: Commit**

```bash
git add _includes/footer.html assets/css/style.css
git commit -m "footer: ink-on-bone with coral stitch rule"
```

---

## Task 10: Accessibility verification + README update

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Manual a11y walk-through**

In the browser, perform each check on `http://localhost:4000/NEH_AI_DH/`:

1. Press Tab from the address bar. **Expected:** the "Skip to content" link appears in the top-left.
2. Activate it. **Expected:** focus jumps to `<main>` and the main content area becomes the active region.
3. Tab through each nav link. **Expected:** every link shows a visible 2px ink outline + the running-stitch coral underline draws in.
4. Tab through the week-grid blocks. **Expected:** every block shows the focus outline; activating one navigates to the corresponding week page.
5. Open OS-level reduced-motion (Windows: Settings → Accessibility → Visual effects → Animation effects OFF). Reload. **Expected:** plus-sign stops rotating, callout stitch border freezes, hero-h1 doesn't fade-in. Hover-lift on week blocks still works (it's a transform on `:hover`, gated only by `prefers-reduced-motion` killing the transition duration — that's intentional).
6. Run a contrast check on:
   - Coral (#ff5a4e) bg + bone (#faf6ec) text: ≥ 4.5:1 (AA normal). If it fails, raise the coral darkness or use ink text on coral. **(Use a contrast checker like webaim.org/resources/contrastchecker/.)**
   - Cobalt (#1545c4) bg + bone text: should pass comfortably.
   - Mustard (#e8b53a) bg + ink text: should pass comfortably.
   - Plum (#5d2e5f) bg + bone text: should pass comfortably.

If coral/bone fails, add `color: var(--ink);` to `.week-block.is-color-coral` and `.is-color-cobalt` is unaffected. Document the change in the commit.

- [ ] **Step 2: Update `README.md`**

Replace the current `## To publish` section with:

```markdown
## Local preview

```bash
bundle install            # first time only
bundle exec jekyll serve
```

Visit `http://localhost:4000/NEH_AI_DH/`.

## Deploying to GitHub Pages

This repo deploys via GitHub Pages. In the repo settings → **Pages** → **Build and deployment**, set:

- **Source:** Deploy from a branch
- **Branch:** `main` / root (`/`)

The site will publish to `https://amsucf.github.io/NEH_AI_DH/`.

## Design system

The site uses a custom modern-quilt theme — palette, typography, motion, and the schedule-grid component are documented in `docs/superpowers/specs/2026-04-27-fiber-arts-jekyll-design.md`.
```

- [ ] **Step 3: Commit**

```bash
git add README.md assets/css/style.css   # include style.css if Step 1 required a contrast fix
git commit -m "a11y+docs: contrast pass and updated README preview/deploy steps"
```

---

## Task 11: Cross-page sweep + final build

**Files:** none — verification only.

- [ ] **Step 1: Page-by-page visual check**

Visit each in order and confirm no obvious regressions:

1. `/NEH_AI_DH/` — header with rotating plus, hero-h1 fade-rise, schedule grid renders 12 blocks in correct color rotation, footer present.
2. `/NEH_AI_DH/readings.html` — tags render as hard-bordered pills in sage/mustard/plum; long lists are readable; tables (none currently) would render with mustard headers.
3. `/NEH_AI_DH/exercises.html` — same tag rendering; long-form prose is readable; `~30 min`/`~90 min`/`~3 hours` lines visible.
4. `/NEH_AI_DH/weeks/week-01.html` — workshop callout has marching stitched border.
5. `/NEH_AI_DH/weeks/week-02.html` — async callout has dashed ink border, no animation.
6. `/NEH_AI_DH/weeks/week-09.html` — workshop callout, longer body (this week is the AI-policy week; verify code blocks and links inside the callout still render legibly).

- [ ] **Step 2: Production build**

Run: `JEKYLL_ENV=production bundle exec jekyll build`
Expected: completes without errors.
Inspect: `_site/index.html` for the rendered weeks-grid and `_site/assets/css/style.css` for the compiled CSS.

- [ ] **Step 3: Push and confirm GitHub Pages deploy**

```bash
git push origin main
```

Wait ~1–2 minutes, then visit `https://amsucf.github.io/NEH_AI_DH/`.
Expected: identical to local preview, with all internal `weeks/week-NN.md` links resolved to `weeks/week-NN.html` (courtesy of `jekyll-relative-links`).

If any link 404s, check the GitHub Actions log for the Pages build for warnings — most likely cause is the relative-links plugin not installed (re-confirm `Gemfile.lock` was committed by GitHub Pages, not by us — we excluded it locally).

- [ ] **Step 4: Final commit if anything was tweaked**

If Steps 1–3 surfaced anything (contrast tweaks, a markdown link that wasn't caught by relative-links, etc.), commit those fixes:

```bash
git add -A
git commit -m "polish: post-deploy sweep"
git push
```

If nothing needed tweaking, this task closes with no commit.

---

## Done condition

The redesign is complete when:

1. `bundle exec jekyll serve` builds and serves locally without errors.
2. `https://amsucf.github.io/NEH_AI_DH/` resolves and every internal link works.
3. All 12 week pages, the readings page, and the exercises page render with the modern-quilt design system (palette, type, stitched callouts, hard offset shadows on the schedule grid).
4. Reduced-motion users get a still site.
5. Tab-through reaches every interactive element with a visible focus outline.
