# -*- coding: utf-8 -*-
"""Shared site structure: page keys, URL slugs, and navigation labels.

Every page lives at the SAME slug under /en/ and /zh/, which is what makes
the language switch and hreflang links trivial: given a page key, build.py
can look up the slug once and just prefix /en/ or /zh/.
"""

POSTER_KEYS = [
    "beyond-tea",
    "pause-sip-be-here",
    "go-have-tea",
    "harmony-not-sameness",
    "a-cup-for-the-city",
    "slow-down-edmonton",
    "be-still-be-here",
    "many-names-one-edmonton",
    "tea-travels-here",
    "a-world-of-tea",
    "many-words-for-tea",
    "edmonton-community-series",
    "osmanthus-infusion",
]

TABLE_KEYS = ["chinese-tea", "wellness-goji", "bubble-tea"]
ARTIST_KEYS = ["hui-yang", "ying-joy-wen"]

# key -> (slug, kind)
# kind drives small layout differences in templates.py (poster meta box,
# table look-closely triad, etc.) — content itself still comes from blocks.
PAGES = {
    "home": ("", "home"),
    "about": ("about/", "standard"),
    "tables": ("tables/", "standard"),
    "posters": ("posters/", "standard"),
    "artists": ("artists/", "standard"),
    "curator": ("curator/", "standard"),
    "edmonton-tea-map": ("edmonton-tea-map/", "map"),
    "learning": ("learning/", "standard"),
    "glossary": ("glossary/", "glossary"),
    "sources-credits": ("sources-credits/", "standard"),
    "faq": ("faq/", "faq"),
}
for _k in TABLE_KEYS:
    PAGES[f"table-{_k}"] = (f"tables/{_k}/", "table")
for _k in POSTER_KEYS:
    PAGES[f"poster-{_k}"] = (f"posters/{_k}/", "poster")
for _k in ARTIST_KEYS:
    PAGES[f"artist-{_k}"] = (f"artists/{_k}/", "artist")

# Subpage key -> landing-page key, used to render a "back to ..." link on
# every table/poster/artist detail page.
PARENT_OF = {}
for _k in TABLE_KEYS:
    PARENT_OF[f"table-{_k}"] = "tables"
for _k in POSTER_KEYS:
    PARENT_OF[f"poster-{_k}"] = "posters"
for _k in ARTIST_KEYS:
    PARENT_OF[f"artist-{_k}"] = "artists"

# Main navigation, in display order. Each entry is either a direct page
# link (children=None) or a dropdown whose own key is also a landing page.
NAV = [
    {"key": "home", "children": None},
    {"key": "about", "children": None},
    {"key": "tables", "children": [f"table-{k}" for k in TABLE_KEYS]},
    {"key": "posters", "children": None},
    {"key": "artists", "children": [f"artist-{k}" for k in ARTIST_KEYS]},
    {"key": "curator", "children": None},
    {"key": "edmonton-tea-map", "children": None},
    {"key": "learning", "children": None},
    {"key": "glossary", "children": None},
    {"key": "sources-credits", "children": None},
    {"key": "faq", "children": None},
]

NAV_LABELS = {
    "home": ("Home", "首页"),
    "about": ("About the Exhibition", "关于展览"),
    "tables": ("Three Tables", "三张展桌"),
    "table-chinese-tea": ("Chinese Tea", "中国茶"),
    "table-wellness-goji": ("Wellness & Goji", "养生与枸杞"),
    "table-bubble-tea": ("Bubble Tea", "珍珠奶茶"),
    "posters": ("Poster Gallery", "海报馆"),
    "artists": ("Artists", "艺术家"),
    "artist-hui-yang": ("Hui Yang", "杨慧"),
    "artist-ying-joy-wen": ("Ying (Joy) Wen", "文莹"),
    "curator": ("Curator", "策展人"),
    "edmonton-tea-map": ("Edmonton Tea Map", "埃德蒙顿茶地图"),
    "learning": ("Learning Resources", "学习资源"),
    "glossary": ("Glossary", "词汇表"),
    "sources-credits": ("Sources & Credits", "资料来源与致谢"),
    "faq": ("FAQ", "常见问题"),
}

for _k in POSTER_KEYS:
    PAGES.setdefault(f"poster-{_k}", (f"posters/{_k}/", "poster"))

SITE_NAME = {"en": "Go Have Tea", "zh": "吃茶去"}
