# Akram Odeh, portfolio

Personal portfolio built with Django. Content lives in one file: `prf/data.py`.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```
Open http://127.0.0.1:8000. Debug mode is on locally by default.

## Update the content
Edit `prf/data.py` (experience, skills, education, projects, links). Replace `prf/static/media/Resume.pdf` to update the resume.

## Publish for free (static site)
The site has no database, so it can be exported to plain HTML and hosted free.

1. Edit `prf/data.py`, then run `python build_static.py`. This creates the `dist/` folder.
2. Commit and push (`dist/` is part of the repo).
3. Host the `dist/` folder:
   - **Cloudflare Pages:** Workers & Pages, Create, Pages, connect the repo. Build command: *(leave empty)*. Build output directory: `dist`.
   - **Render Static Site:** New, Static Site. Build command: *(leave empty)*. Publish directory: `dist`.

Note: Cloudflare Pages allows files up to 25 MiB, so keep `demo.mp4` under that.

## Run as a Django server instead (optional)
Render Web Service: build `./build.sh`, start `gunicorn portfolio.wsgi`, set a `SECRET_KEY` environment variable. Free web services sleep after 15 idle minutes, so the static route is better.

## Structure
- `portfolio/`: Django settings and root URLs
- `prf/`: the app (views, content data, static CSS/JS/media)
- `templates/`: `base.html`, `index.html`, `projects.html`
- `build_static.py`: exports the site to `dist/` for static hosting
