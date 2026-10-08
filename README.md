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

## Deploy on Render
- **Build command:** `./build.sh`
- **Start command:** `gunicorn portfolio.wsgi`
- **Environment variable:** `SECRET_KEY` (any long random string)
- Optional: `ALLOWED_HOSTS` for a custom domain (comma-separated).

## Structure
- `portfolio/`: Django settings and root URLs
- `prf/`: the app (views, content data, static CSS/JS/media)
- `templates/`: `base.html`, `index.html`, `projects.html`
