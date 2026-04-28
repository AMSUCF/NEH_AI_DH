# NEH DH+AI Workshop Series

Course site for *Building a Digital Humanities Generative AI Learning Community*, a National Endowment for the Humanities-funded project at the University of Central Florida (Summer C 2026, May 12 – August 1).

This Jekyll site provides:

- **Overview & schedule** — `index.md`
- **Curated reading list** — `readings.md`
- **Exercise menu** — `exercises.md`
- **Twelve weekly modules** — `weeks/week-01.md` through `weeks/week-12.md`

Workshop weeks (1, 3, 5, 7, 9, 11) document the in-person session at CHDR. Asynchronous weeks (2, 4, 6, 8, 10, 12) provide an optional deep-dive menu of readings and exercises so faculty across disciplines can keep pace at their own depth.

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

## Audience

Primary: faculty across humanities disciplines participating in the NEH learning community, mixed technical comfort, no assumed coding background. Secondary: graduate students in the parallel ENG 6813 *Interdisciplinary Teaching* course who use the same materials inside their seminar.

## Contact

Dr. Anastasia Salter — anastasia at ucf.edu
