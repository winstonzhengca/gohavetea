# -*- coding: utf-8 -*-
"""Generates the static site into ./docs from content/en.py + content/zh.py.
Output goes to docs/ so it can be served directly by GitHub Pages
(Settings -> Pages -> Deploy from branch -> /docs) with no extra build step.

Usage:  python build.py
Serve:  python -m http.server 8000 --directory docs
"""
import os
import shutil

from content import nav, en as en_content, zh as zh_content
import templates

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(ROOT, "docs")

LANGS = {"en": en_content, "zh": zh_content}


def write_file(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def build():
    # Wipe generated page directories but keep assets (written separately).
    for lang in LANGS:
        lang_dir = os.path.join(SITE_DIR, lang)
        if os.path.isdir(lang_dir):
            shutil.rmtree(lang_dir)

    missing = []
    for lang, module in LANGS.items():
        pages = module.PAGES
        for key in nav.PAGES:
            if key not in pages:
                missing.append(f"{lang}:{key}")
    if missing:
        raise SystemExit(
            "Missing content entries for keys: " + ", ".join(missing)
        )

    count = 0
    for lang, module in LANGS.items():
        for key, (slug, _kind) in nav.PAGES.items():
            page_data = module.PAGES[key]
            main_html = templates.render_blocks(page_data["blocks"], lang, key)
            html = templates.base_layout(
                lang, key, page_data["title"], page_data["meta"], main_html
            )
            out_path = os.path.join(SITE_DIR, lang, slug, "index.html")
            write_file(out_path, html)
            count += 1

    write_file(os.path.join(SITE_DIR, "index.html"), root_chooser())
    write_file(os.path.join(SITE_DIR, "sitemap.xml"), sitemap_xml())
    write_file(os.path.join(SITE_DIR, "robots.txt"), robots_txt())
    write_file(os.path.join(SITE_DIR, "404.html"), not_found_page())
    print(f"Built {count} pages into {SITE_DIR}")


def sitemap_xml():
    urls = []
    for key, (slug, _kind) in nav.PAGES.items():
        en_loc = templates.abs_url(f"/en/{slug}")
        zh_loc = templates.abs_url(f"/zh/{slug}")
        for loc, alt in ((en_loc, zh_loc), (zh_loc, en_loc)):
            urls.append(
                f'  <url>\n'
                f'    <loc>{loc}</loc>\n'
                f'    <xhtml:link rel="alternate" hreflang="en-CA" href="{en_loc}" />\n'
                f'    <xhtml:link rel="alternate" hreflang="zh-Hans" href="{zh_loc}" />\n'
                f'  </url>'
            )
    body = "\n".join(urls)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{body}\n"
        "</urlset>"
    )


def robots_txt():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {templates.abs_url('/sitemap.xml')}\n"
    )


def not_found_page():
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page Not Found | Go Have Tea / 吃茶去</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="{templates.url('/assets/css/style.css')}">
</head>
<body>
<main class="chooser">
  <h1>Page not found</h1>
  <p lang="zh-Hans">找不到该页面</p>
  <div class="button-row">
    <a class="btn btn-primary" href="{templates.url('/en/')}">Go to homepage (English)</a>
    <a class="btn btn-primary" href="{templates.url('/zh/')}" lang="zh-Hans">前往首页（中文）</a>
  </div>
</main>
</body>
</html>"""


def root_chooser():
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Go Have Tea | 吃茶去</title>
<meta http-equiv="refresh" content="0; url={templates.url('/en/')}">
<link rel="stylesheet" href="{templates.url('/assets/css/style.css')}">
</head>
<body>
<main class="chooser">
  <h1><span lang="zh-Hans">吃茶去</span> · Go Have Tea</h1>
  <p>A three-table exhibition for the 2026 Edmonton Heritage Festival.</p>
  <div class="button-row">
    <a class="btn btn-primary" href="{templates.url('/en/')}">English</a>
    <a class="btn btn-primary" href="{templates.url('/zh/')}" lang="zh-Hans">中文</a>
  </div>
</main>
</body>
</html>"""


if __name__ == "__main__":
    build()
