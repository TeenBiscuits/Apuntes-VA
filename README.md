# Apuntes VA `/uβˈea/`

> [!TIP]
> Puedes ver los apuntes interactivos publicados en este enlace [uvea.pablopl.dev](https://uvea.pablopl.dev)

Apuntes interactivos para la asignatura Visión Artificial del Grao en Enxeñería Informática da FIC (Universidade da Coruña). Creado con [marimo-book](https://github.com/ljchang/marimo-book).

## Local development

```bash
# Synchronize the project environment once (uv run also does this automatically).
uv sync

# Open marimo's notebook browser for content/
uv run edit

# Open one notebook directly
uv run edit content/example.py

# Live-reload dev server (browse at http://127.0.0.1:8000/)
uv run dev

# Strict local build (emits ./_site/)
uv run build

# Validate book.yml + content without building
uv run check

# Remove build artifacts
uv run clean

# Clean, strict production build
uv run release
```

All commands use the versions declared in `pyproject.toml` and locked in
`uv.lock`; no global marimo or marimo-book installation is required.

The local commands use `book.dev.yml`, which skips social-card rendering and
external URL checks. `uv run release` uses `book.yml` and enables both checks
for publication.

On macOS, the `social` extra also needs the native Cairo and Pango libraries:

```bash
brew install cairo pango
```

## Layout

- `book.yml` — TOC, theme, branding, launch-button config
- `book.dev.yml` — local build configuration without network/image checks
- `content/` — your `.md` and marimo `.py` chapters
- `.github/workflows/deploy.yml` — builds and publishes to GitHub Pages
  on every push to `main` (edit or delete as needed)

## License

The content of this project itself is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](LICENSE-CONTENT.md), and the underlying source code used to format and display that content is licensed under the [MIT license](LICENSE.md).
