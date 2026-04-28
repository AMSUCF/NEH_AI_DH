# NEH DH+AI Workshop Site — Modern-Quilt Jekyll Redesign

**Status:** approved (brainstorming) → ready for implementation plan
**Date:** 2026-04-27
**Repo:** `AMSUCF/NEH_AI_DH` → publishes at `https://amsucf.github.io/NEH_AI_DH/`

## Goal

Two outcomes in one pass:

1. **Fix the GitHub Pages setup** so the site actually builds and links resolve when deployed from `main`.
2. **Replace the visual design** with a modern-quilt-inspired theme — bold solids, generous negative space, animated stitching, contemporary type — in a way that keeps the long-form readings/exercises pages comfortable to read.

The site's content (12 weekly modules, readings list, exercise menu, overview) is solid and stays as-is. Only configuration, layouts, includes, and CSS change. Markdown bodies are touched only to update internal link extensions.

## Audience reminder

Faculty across humanities disciplines, mixed technical comfort, no assumed coding background. Plus graduate students in the parallel ENG 6813 seminar. Visual treatment should feel **handcrafted and serious**, not playful-startup.

---

## Part 1 — GitHub Pages plumbing fixes

### 1.1 `_config.yml` corrections

- `baseurl: "/NEHWorkshops"` → `baseurl: "/NEH_AI_DH"` (matches the repo name; this is what breaks on deploy today).
- Omit `theme` — the site is a custom theme via `_layouts` + `_includes`, no remote/gem theme.
- Keep `jekyll-seo-tag`. Add `jekyll-relative-links` (allow-listed on GH Pages) so `.md` links in markdown bodies are auto-rewritten to the rendered `.html` URL — **this lets the existing markdown link forms keep working without site-wide find/replace.** Loose pages keep Jekyll's default URL shape (`/weeks/week-01.html`); we don't override `permalink`, since that setting only applies to posts/collections and would not change loose-page URLs.
- Add SEO-tag fields: `author`, `twitter`, `social.links` (optional — only if AS wants them; not implementation-blocking).

### 1.2 Add `Gemfile`

A minimal GH-Pages-compatible Gemfile so `bundle exec jekyll serve` works locally on Windows (the current README promises this without a Gemfile present):

```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.8"   # Ruby 3+ no longer ships webrick
group :jekyll_plugins do
  gem "jekyll-relative-links"
end
```

### 1.3 `.gitignore` additions

Already partially in place. Confirm it covers `_site/`, `.jekyll-cache/`, `.jekyll-metadata`, `Gemfile.lock`, `.superpowers/`.

### 1.4 Internal link handling

The 44 `.md`-suffixed internal links across 15 files keep working via `jekyll-relative-links` — no body edits needed in week-XX.md, readings.md, exercises.md, index.md.

### 1.5 GitHub Pages source

Confirm in repo settings: **Pages → Build from branch → `main` → `/` (root)**. (Not the design's job to flip the toggle, but the README will document this.)

---

## Part 2 — Visual design

### 2.1 Direction (approved)

**Modern Minimal Quilt** with **Bricolage Grotesque + Inter** typography and **animated stitching** for personality.

Vibe references: Carolyn Friedlander piecing, Yoshiko Jinzenji negative space, Denyse Schmidt color confidence. Cream ground, a small palette of saturated solids deployed deliberately, hand-cut-paper feel for boundaries (offset hard shadows, not soft drop-shadows).

### 2.2 Palette

| Token | Hex | Role |
|---|---|---|
| `--bone` | `#faf6ec` | Page background, the "muslin" |
| `--ink` | `#141414` | Body text, structural lines, hard borders |
| `--coral` | `#ff5a4e` | Workshop blocks, primary accent, link underline stitches |
| `--cobalt` | `#1545c4` | Workshop blocks (alt), strong link color, callout strong-text |
| `--mustard` | `#e8b53a` | Workshop blocks (alt), plus-sign decoration, table headers |
| `--sage` | `#7a8f4a` | Tag (Light), gentle accent |
| `--plum` | `#5d2e5f` | Tag (Deep), occasional accent |
| `--paper` | `#ffffff` | Card surface (workshop callouts) |
| `--rule` | `#1a1a1a` | Borders (always 2px hard, never hairline) |
| `--muted` | `#5a5a5a` | Secondary text |

Workshop weeks rotate among coral / cobalt / mustard / plum across the schedule so the year of weeks reads like a quilt top, not a single-color bar.

Reading-tag colors:

- `tag-light` → `--sage` on bone
- `tag-standard` → `--mustard` on `#3a2900`
- `tag-deep` → `--plum` on bone (or coral on bone)

### 2.3 Typography

- **Display:** [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque) (variable; `opsz`, `wdth`, `wght` axes) — used for `h1`, `h2`, site title, week-block labels, nav. `font-variation-settings: "opsz" 96, "wdth" 108` for big headlines; tightened (`"wdth" 100`) for `h3`/`h4`.
- **Body:** [Inter](https://fonts.google.com/specimen/Inter) — paragraphs, lists, tables, captions, callout body, footer.
- **Mono:** JetBrains Mono — code blocks (carry over from current).

Source Serif 4 and Source Sans 3 are removed.

### 2.4 Layout system

- Max content width: `64rem` (slightly wider than current `60rem` to accommodate big quilt-block grids on the schedule and weekly-modules list).
- Header: full-bleed bone band, 2px ink border-bottom, with one large coral plus-sign element at top-left (a real CSS `+` made of two rectangles, slowly rotating), site title in Bricolage Grotesque, italic tagline in Inter.
- Nav: horizontal links with running-stitch underline-on-hover (see 2.5).
- Page wrap: bone background throughout (no white card surface). Calls-out get a white surface with a stitched border to "rise" off the page.
- Footer: ink-on-bone, with a coral stitched rule above as the closing seam.

### 2.5 Motion vocabulary

All animations honor `@media (prefers-reduced-motion: reduce)` — continuous loops and decorative rotations pause; underline-draws collapse to instant.

| Element | Behavior | Implementation note |
|---|---|---|
| Nav link underline | Coral running-stitch (`linear-gradient` dashed) draws left→right on hover/focus, ~380ms | Animated `width: 0 → 100%` on `::after`. |
| Section dividers | Ink-dashed rule that draws in on first paint | `width: 0 → 100%` keyframe; respects reduced-motion (snap to 100%). |
| Workshop callouts | White surface, ink body, with a continuously running stitched border in coral | SVG `<rect>` with `stroke-dasharray` and animated `stroke-dashoffset` (single CSS keyframe, ~18s loop). Pauses for reduced motion. |
| Plus-sign decoration | Mustard CSS `+` element in the header, slowly rotating (~14s/turn) | Pure CSS; pauses for reduced motion. |
| Week blocks (schedule grid) | Hover: lifts `translateY(-3px)` + hard offset shadow `4px 4px 0 var(--ink)` | No drop-shadow blur; matches the cut-paper / quilt-top aesthetic. |
| Page-load entry | `h1` fade+rise (`opacity 0→1`, `translateY(8px→0)`, ~480ms) | One element only; no staggered cascades (the workshop-faculty audience finds those distracting). |

### 2.6 Component inventory

These are the named CSS components the layout/includes/markdown will use:

- `.site-header` (full-bleed, plus-sign decoration, title block, nav)
- `.site-nav` + `.nav-link` (running-stitch underline)
- `.content-wrap` (max-width, padding)
- `.page-content` (typographic defaults: h1–h4, p, ul/ol, blockquote, code, pre, table, hr — all retuned)
- `.stitch-divider` (animated dashed rule; replaces some `<hr>` usages where appropriate)
- `.workshop-callout` (white card, animated stitched border via inline SVG include)
- `.async-callout` (bone card, dashed ink border, no animation — calmer counterpart)
- `.weeks-grid` (responsive grid of week blocks; coral/cobalt/mustard/plum rotation for workshop weeks; bone with ink border for async)
- `.tag`, `.tag-light`, `.tag-standard`, `.tag-deep` (pill tags, retuned to new palette)
- `.site-footer` (ink-on-bone, coral stitched rule above)

### 2.7 Schedule grid (the marquee element)

The week-by-week table on `index.md` becomes a quilt top:

- Render as a 2-column-wide responsive grid (4-up at desktop, 2-up at tablet, 1-up at mobile).
- Each week is a block with a thick 2px ink border, week number set huge in Bricolage Grotesque, theme line in Inter beneath.
- Workshop weeks (1, 3, 5, 7, 9, 11) get a saturated solid background (rotating coral / cobalt / mustard / plum / coral / cobalt).
- Async weeks (2, 4, 6, 8, 10, 12) are bone-with-ink-border ("muslin" blocks).
- Hover: hard offset shadow `4px 4px 0 var(--ink)` + small lift.
- The current Markdown table on `index.md` will be replaced with a Liquid `for` loop reading from a small `_data/weeks.yml` file so the grid is one source of truth and weeks pages stay simple. **This is the only data refactor in the redesign.**

`_data/weeks.yml` schema:

```yaml
- num: 1
  date: "May 11"
  kind: workshop          # workshop | async
  workshop_date: "Tue May 13"
  theme: "LLMs, models, harnesses, the higher-ed crisis"
  slug: week-01
- num: 2
  date: "May 18"
  kind: async
  theme: "LLM Fundamentals reinforcement"
  slug: week-02
# ...through week 12
```

The same data file powers the "Weekly Modules" link list lower on `index.md`, eliminating the duplicated 12-line list.

### 2.8 Accessibility

- Color contrast: every text-on-color combination ≥ WCAG AA (verified for coral/bone, cobalt/bone, mustard/ink, plum/bone — the weak link is mustard, where text must be `--ink`, never bone).
- All decorative SVGs (`stitch-frame`, plus-sign) carry `aria-hidden="true"`.
- Focus styles: every interactive element gets a visible ink outline (2px solid `--ink`, 2px offset) — does not depend on the stitched-underline animation.
- Reduced-motion: as 2.5.
- Skip link: add a `Skip to content` link as the first focusable element in `default.html` (currently absent).
- Nav landmark: existing `<nav aria-label="Main navigation">` stays.

### 2.9 Files changed

| File | Change |
|---|---|
| `_config.yml` | baseurl, permalink, plugins (add `jekyll-relative-links`), theme: null |
| `Gemfile` | new — github-pages gem + relative-links + webrick |
| `.gitignore` | new — `_site/`, caches, `Gemfile.lock`, `.superpowers/` |
| `_layouts/default.html` | rewritten — preconnect Bricolage+Inter, skip link, structure |
| `_includes/header.html` | rewritten — plus decoration, nav, title block |
| `_includes/footer.html` | rewritten — ink-on-bone, stitched rule above |
| `_includes/stitch-frame.svg` | new — reusable animated-border SVG for callouts |
| `_includes/weeks-grid.html` | new — Liquid loop over `_data/weeks.yml` |
| `_data/weeks.yml` | new — single source of truth for the 12 weeks |
| `assets/css/style.css` | rewritten end-to-end with the design system above |
| `index.md` | replace the Markdown schedule table and the Weekly Modules link list with `{% include weeks-grid.html %}`; everything else unchanged |
| `README.md` | small note: design system, how to preview, GH-Pages source setting |

`weeks/week-XX.md`, `readings.md`, `exercises.md` content bodies are **not** edited — only their styling changes.

### 2.10 Out of scope

- No JavaScript framework, no bundler, no build step beyond Jekyll.
- No dark mode (not requested; can be a follow-on).
- No search, no tag pages, no week-to-week prev/next nav (could be follow-on).
- No image assets in this pass — the visual interest comes from CSS and type.
- No content edits to readings/exercises/weeks beyond the `index.md` schedule replacement.

---

## Open question parked for implementation

The current README references a sibling repo at `../InterdisciplinaryTeaching-main/` and the readings page references several others (`HumanitiesAI-main`, `CriticalMaking2026-main`, etc.) by relative path. These won't resolve on the deployed site. **Implementation plan should flag these but not auto-fix them** — AS may want to point them at deployed URLs or strip them; that's a content call, not a design call.

## Acceptance

The redesign is done when:

1. `bundle exec jekyll serve` builds and serves locally on Windows without errors.
2. Pushing to `main` produces a working `https://amsucf.github.io/NEH_AI_DH/` deploy where every internal link resolves.
3. Header, schedule grid, week pages, readings, and exercises all visibly use the modern-quilt design system (palette, type, stitching motion, hard offset shadows).
4. Reduced-motion users get a still site.
5. Lighthouse a11y ≥ 95 on `index.md`.
