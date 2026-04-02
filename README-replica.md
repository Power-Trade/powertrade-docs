# PowerTrade Docs — GitBook Replica

Static HTML replica of the PowerTrade GitBook documentation site.

## Features

- **Pixel-perfect dark theme** matching the GitBook layout
- **3-column layout**: left nav sidebar, main content, right TOC sidebar
- **Single `index.html`** — zero external dependencies (except Google Fonts)
- **SPA navigation** — all pages load instantly via show/hide
- **Search** — Ctrl+K opens search modal with fuzzy filtering
- **External link tooltips** — hover to see destination URL
- **Code blocks** with syntax highlighting and accent bar
- **Responsive** — collapses sidebars on smaller screens
- **Previous/Next navigation** on every page
- **"Was this helpful?"** emoji reactions in right sidebar

## Deployment

### GitHub Pages

1. Push `index.html` to a branch (e.g. `gitbook-replica`)
2. In repo Settings → Pages, set source to that branch
3. Site will be live at `https://<org>.github.io/powertrade-docs/`

### Local Preview

```bash
# Any static file server works:
python3 -m http.server 8000
# Then open http://localhost:8000
```

## Content

All content is embedded from the `docs/` markdown files in the powertrade-docs repo.
Pages with "Content coming soon..." will be populated as documentation is written.

## Tech

- Pure HTML/CSS/JS — no build step, no frameworks
- Inter font from Google Fonts
- CSS custom properties for theming
- ~78KB total file size
