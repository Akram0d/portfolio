"""Export the site to plain HTML in ./dist so it can be hosted for free.

Usage:  python build_static.py
Then deploy the `dist` folder (Cloudflare Pages, Render Static Site, GitHub Pages...).
"""
import os
import shutil
from pathlib import Path

os.environ["DJANGO_SETTINGS_MODULE"] = "portfolio.settings"
os.environ["DJANGO_DEBUG"] = "1"  # plain /static/ URLs, no server-only hashing

import django

django.setup()
from django.test import Client  # noqa: E402

BASE = Path(__file__).resolve().parent
DIST = BASE / "dist"

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()

client = Client(HTTP_HOST="localhost")
pages = {"/": "index.html", "/projects/": "projects/index.html"}
for url, target in pages.items():
    response = client.get(url)
    assert response.status_code == 200, f"{url} returned {response.status_code}"
    out = DIST / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(response.content)

shutil.copytree(BASE / "prf" / "static", DIST / "static")
# Old capitalised URL keeps working (Cloudflare Pages / Netlify / Render use this file).
(DIST / "_redirects").write_text("/Projects/ /projects/ 301\n")

size = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file()) / 1e6
print(f"Built {len(pages)} pages into {DIST} ({size:.1f} MB)")
