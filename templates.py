# -*- coding: utf-8 -*-
"""Static HTML rendering: one base layout + one flexible content-block
renderer reused across every page type (home, standard, table, poster,
artist, map, glossary, faq). Content pages just supply a list of block
dicts; this module turns them into HTML.
"""

from content import nav

# Set to "" for a domain-root deploy (custom domain, or a <user>.github.io
# root Pages site). Set to "/<repo-name>" for a GitHub Pages *project* site
# (served at username.github.io/repo-name/), so every root-absolute link
# still resolves correctly under that sub-path.
BASE_PATH = "/go-have-tea"


def url(path):
    """Prefix an internal root-absolute path with BASE_PATH. External
    (http/https) links and in-page fragments pass through unchanged."""
    if path.startswith(("http://", "https://", "#")):
        return path
    return BASE_PATH + path


PLACEHOLDER_NOTE = {
    "en": "Image placeholder — pending final artwork files",
    "zh": "图片占位 — 待补充最终作品文件",
}
ALT_LABEL = {"en": "Description:", "zh": "描述："}
SKIP_LABEL = {"en": "Skip to main content", "zh": "跳至主要内容"}
LANG_SWITCH_LABEL = {"en": "中文", "zh": "English"}
MENU_LABEL = {"en": "Menu", "zh": "菜单"}
BACK_TOP = {"en": "Back to top", "zh": "回到顶部"}
PENDING_TAG = {"en": "pending organizer confirmation", "zh": "待主办方确认"}

TONE_CYCLE = ["green", "tan", "gold", "berry", "paper"]


def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _tone_for(key):
    return TONE_CYCLE[abs(hash(key)) % len(TONE_CYCLE)]


# ---------------------------------------------------------------------------
# Block renderers
# ---------------------------------------------------------------------------

def _btn(item):
    variant = item.get("variant", "primary")
    external = item.get("external")
    attrs = ' target="_blank" rel="noopener"' if external else ""
    return (
        f'<a class="btn btn-{esc(variant)}" href="{esc(url(item["href"]))}"{attrs}>'
        f'{item["label"]}</a>'
    )


def render_block(block, lang, page_key=""):
    t = block["type"]

    if t == "hero":
        buttons = "".join(_btn(b) for b in block.get("buttons", []))
        eyebrow = (
            f'<p class="hero-eyebrow">{block["eyebrow"]}</p>'
            if block.get("eyebrow")
            else ""
        )
        subtitle = (
            f'<p class="hero-subtitle">{block["subtitle"]}</p>'
            if block.get("subtitle")
            else ""
        )
        lead = f'<p class="hero-lead">{block["lead"]}</p>' if block.get("lead") else ""
        return f"""<section class="hero">
  {eyebrow}
  <h1>{block['title']}</h1>
  {subtitle}
  {lead}
  <div class="hero-buttons">{buttons}</div>
</section>"""

    if t == "heading":
        level = block.get("level", 2)
        cls = " class=\"section-kicker\"" if block.get("kicker") else ""
        return f"<h{level}{cls}>{block['text']}</h{level}>"

    if t == "para":
        cls = f' class="{block["class"]}"' if block.get("class") else ""
        return f"<p{cls}>{block['text']}</p>"

    if t == "list":
        tag = "ol" if block.get("ordered") else "ul"
        items = "".join(f"<li>{i}</li>" for i in block["items"])
        return f'<{tag} class="block-list">{items}</{tag}>'

    if t == "quote":
        cite = f"<cite>{block['attribution']}</cite>" if block.get("attribution") else ""
        return f'<blockquote class="pull-quote"><p>{block["text"]}</p>{cite}</blockquote>'

    if t == "note":
        style = block.get("style", "notice")
        label = block.get("label", "")
        label_html = f'<span class="note-label">{label}</span> ' if label else ""
        return f'<div class="note note-{style}">{label_html}{block["text"]}</div>'

    if t == "image":
        tone = block.get("tone") or _tone_for(block.get("caption", page_key))
        pending = (
            f'<span class="placeholder-pending">{PENDING_TAG[lang]}</span>'
            if block.get("pending")
            else ""
        )
        caption = f'<figcaption><span class="caption-text">{block.get("caption", "")}</span>'
        if block.get("alt"):
            caption += f' <span class="alt-inline"><span class="alt-inline-label">{ALT_LABEL[lang]}</span> {block["alt"]}</span>'
        caption += f"{pending}</figcaption>"
        return f"""<figure class="placeholder-panel tone-{tone}">
  <div class="placeholder-box" role="img" aria-label="{esc(block.get('alt', block.get('caption', '')))}">
    <span class="placeholder-tag">{PLACEHOLDER_NOTE[lang]}</span>
  </div>
  {caption}
</figure>"""

    if t == "keywords":
        items = "".join(f'<li>{i}</li>' for i in block["items"])
        return f'<ul class="keyword-tags">{items}</ul>'

    if t == "triad":
        items = "".join(
            f'<div class="triad-item"><span class="triad-label">{i["label"]}</span><p>{i["text"]}</p></div>'
            for i in block["items"]
        )
        return f'<div class="triad">{items}</div>'

    if t == "columns":
        cards = []
        for c in block["items"]:
            inner = f'<h3>{c["title"]}</h3><p>{c["text"]}</p>'
            if c.get("href"):
                cards.append(f'<a class="card card-link" href="{esc(url(c["href"]))}">{inner}</a>')
            else:
                cards.append(f'<div class="card">{inner}</div>')
        return f'<div class="card-grid">{"".join(cards)}</div>'

    if t == "buttons":
        return f'<div class="button-row">{"".join(_btn(b) for b in block["items"])}</div>'

    if t == "poster_meta":
        return f"""<div class="poster-meta">
  <p class="poster-chinese">{block['chinese']}</p>
  <p class="poster-translation">{block['translation']}</p>
</div>"""

    if t == "definition_list":
        rows = "".join(
            f'<div class="glossary-row"><dt>{i["term"]}</dt><dd>{i["def"]}</dd></div>'
            for i in block["items"]
        )
        return f'<dl class="glossary-list">{rows}</dl>'

    if t == "faq":
        items = "".join(
            f'<details class="faq-item"><summary>{i["q"]}</summary><p>{i["a"]}</p></details>'
            for i in block["items"]
        )
        return f'<div class="faq-list">{items}</div>'

    if t == "map_list":
        groups = []
        for g in block["groups"]:
            entries = "".join(
                f'<li><strong>{e["name"]}</strong><span class="map-entry-desc">{e["desc"]}</span></li>'
                for e in g["entries"]
            )
            groups.append(
                f'<section class="map-group"><h3>{g["title"]}</h3><ul>{entries}</ul></section>'
            )
        return f'<div class="map-groups">{"".join(groups)}</div>'

    if t == "gallery_grid":
        cards = []
        for i, item in enumerate(block["items"]):
            tone = TONE_CYCLE[i % len(TONE_CYCLE)]
            cards.append(
                f'<a class="gallery-card" href="{esc(url(item["href"]))}">'
                f'<span class="gallery-card-thumb tone-{tone}" aria-hidden="true"></span>'
                f'<span class="gallery-card-title">{item["title"]}</span>'
                f'{"<span class=\"gallery-card-sub\">" + item["sub"] + "</span>" if item.get("sub") else ""}'
                f"</a>"
            )
        return f'<div class="gallery-grid">{"".join(cards)}</div>'

    if t == "html":
        return block["value"]

    if t == "bubble_builder":
        return _bubble_builder(lang)

    raise ValueError(f"Unknown block type: {t}")


# ---------------------------------------------------------------------------
# Build-a-cup interactive widget (Bubble Tea table page only)
# ---------------------------------------------------------------------------

BUBBLE_UI = {
    "en": {
        "heading": "Build a cup",
        "intro": "Choose one option in each row. There is no single correct cup.",
        "groups": [
            ("base", "Tea base", [
                ("black", "Black tea", "#6b3b23"),
                ("green", "Green tea", "#8faa5c"),
                ("oolong", "Oolong tea", "#c08a3e"),
                ("fruit", "Fruit tea", "#c9536b"),
            ]),
            ("milk", "Milk", [
                ("whole", "Whole milk", None),
                ("oat", "Oat milk", None),
                ("creamer", "Creamer", None),
                ("none", "No milk", None),
            ]),
            ("sweet", "Sweetness", [
                ("100", "100%", None),
                ("50", "50%", None),
                ("25", "25%", None),
                ("0", "0%", None),
            ]),
            ("ice", "Ice", [
                ("full", "Full ice", None),
                ("less", "Less ice", None),
                ("none", "No ice", None),
            ]),
            ("topping", "Topping", [
                ("pearls", "Tapioca pearls", "pearls"),
                ("jelly", "Grass jelly", "jelly"),
                ("pudding", "Pudding", "jelly"),
                ("none", "No topping", "none"),
            ]),
            ("mood", "Mood", [
                ("focused", "Focused", None),
                ("social", "Social", None),
                ("homesick", "Homesick", None),
                ("curious", "Curious", None),
                ("celebrating", "Celebrating", None),
            ]),
        ],
        "summary_prefix": "Your cup:",
        "reflect": "Now look behind the cup: what labour, ingredients, transport, and technology made these choices possible?",
    },
    "zh": {
        "heading": "做一杯我的奶茶",
        "intro": "每一排选一项。没有唯一正确的答案。",
        "groups": [
            ("base", "茶底", [
                ("black", "红茶", "#6b3b23"),
                ("green", "绿茶", "#8faa5c"),
                ("oolong", "乌龙茶", "#c08a3e"),
                ("fruit", "果茶", "#c9536b"),
            ]),
            ("milk", "奶", [
                ("whole", "全脂牛奶", None),
                ("oat", "燕麦奶", None),
                ("creamer", "奶精", None),
                ("none", "不加奶", None),
            ]),
            ("sweet", "甜度", [
                ("100", "全糖", None),
                ("50", "半糖", None),
                ("25", "微糖", None),
                ("0", "无糖", None),
            ]),
            ("ice", "冰量", [
                ("full", "正常冰", None),
                ("less", "少冰", None),
                ("none", "去冰", None),
            ]),
            ("topping", "配料", [
                ("pearls", "珍珠", "pearls"),
                ("jelly", "仙草冻", "jelly"),
                ("pudding", "布丁", "jelly"),
                ("none", "不加配料", "none"),
            ]),
            ("mood", "心情", [
                ("focused", "专注", None),
                ("social", "社交", None),
                ("homesick", "想家", None),
                ("curious", "好奇", None),
                ("celebrating", "庆祝", None),
            ]),
        ],
        "summary_prefix": "我的奶茶：",
        "reflect": "现在想想杯子背后：是什么劳动、原料、运输与技术，让这些选择成为可能？",
    },
}


def _bubble_builder(lang):
    ui = BUBBLE_UI[lang]
    fieldsets = []
    for group_key, legend, options in ui["groups"]:
        labels = []
        for opt_id, opt_label, extra in options:
            data_attrs = f' data-color="{extra}"' if group_key == "base" else ""
            if group_key == "topping":
                data_attrs = f' data-pearls="{extra}"'
            input_id = f"cup-{group_key}-{opt_id}"
            checked = " checked" if opt_id == options[0][0] else ""
            labels.append(
                f'<label for="{input_id}"><input type="radio" id="{input_id}" '
                f'name="cup-{group_key}" value="{opt_label}"{data_attrs}{checked}>'
                f"<span>{opt_label}</span></label>"
            )
        fieldsets.append(
            f'<fieldset data-group="{group_key}"><legend>{legend}</legend>'
            f'<div class="option-row">{"".join(labels)}</div></fieldset>'
        )
    return f"""<div class="cup-builder" id="cup-builder">
  <div class="cup-visual" aria-hidden="false">
    <div class="cup-lid"></div>
    <div class="cup-shape">
      <div class="cup-fill" id="cup-fill"></div>
      <div class="cup-pearls" id="cup-pearls"></div>
    </div>
    <p class="cup-summary" id="cup-summary">{ui['summary_prefix']}</p>
  </div>
  <form class="cup-options" id="cup-options">
    <p>{ui['intro']}</p>
    {''.join(fieldsets)}
  </form>
</div>
<p class="cup-reflect">{ui['reflect']}</p>"""


def render_blocks(blocks, lang, page_key=""):
    return "\n".join(render_block(b, lang, page_key) for b in blocks)


# ---------------------------------------------------------------------------
# Base layout
# ---------------------------------------------------------------------------

def _nav_html(lang, current_key):
    items = []
    for entry in nav.NAV:
        key = entry["key"]
        slug, _kind = nav.PAGES[key]
        label = nav.NAV_LABELS[key][0 if lang == "en" else 1]
        href = url(f"/{lang}/{slug}")
        is_current = key == current_key
        current_attr = ' aria-current="page"' if is_current else ""
        if entry["children"]:
            sub_items = []
            for child_key in entry["children"]:
                c_slug, _ = nav.PAGES[child_key]
                c_label = nav.NAV_LABELS[child_key][0 if lang == "en" else 1]
                c_current = ' aria-current="page"' if child_key == current_key else ""
                sub_items.append(
                    f'<li><a href="{url(f"/{lang}/{c_slug}")}"{c_current}>{c_label}</a></li>'
                )
            items.append(
                f'<li class="nav-has-children">'
                f'<a href="{href}"{current_attr}>{label}</a>'
                f'<ul class="nav-submenu">{"".join(sub_items)}</ul>'
                f"</li>"
            )
        else:
            items.append(f'<li><a href="{href}"{current_attr}>{label}</a></li>')
    return "".join(items)


def base_layout(lang, page_key, title, description, main_html):
    site_name = nav.SITE_NAME[lang]
    slug, _kind = nav.PAGES[page_key]
    other_lang = "zh" if lang == "en" else "en"
    html_lang = "en-CA" if lang == "en" else "zh-Hans"

    nav_html = _nav_html(lang, page_key)

    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{esc(description)}">
<link rel="alternate" hreflang="en-CA" href="{url(f'/en/{slug}')}">
<link rel="alternate" hreflang="zh-Hans" href="{url(f'/zh/{slug}')}">
<link rel="stylesheet" href="{url('/assets/css/style.css')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;700&amp;family=Noto+Sans+SC:wght@400;500;700&amp;display=swap" rel="stylesheet">
</head>
<body>
<a class="skip-link" href="#main">{SKIP_LABEL[lang]}</a>
<header class="site-header">
  <div class="header-inner">
    <a class="site-brand" href="{url(f'/{lang}/')}">
      <span class="brand-mark" aria-hidden="true">茶</span>
      <span class="brand-name">{site_name}</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
      <span class="sr-only">{MENU_LABEL[lang]}</span>
    </button>
    <nav class="primary-nav" id="primary-nav" aria-label="Primary">
      <ul>{nav_html}</ul>
    </nav>
    <a class="lang-switch" href="{url(f'/{other_lang}/{slug}')}" lang="{'zh-Hans' if lang == 'en' else 'en-CA'}">
      {LANG_SWITCH_LABEL[lang]}
    </a>
  </div>
</header>
<main id="main" class="page-{_kind}">
{main_html}
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <p class="footer-credit">{FOOTER_CREDIT[lang]}</p>
    <p class="footer-meta">{FOOTER_META[lang]}</p>
    <a class="back-top" href="#top">{BACK_TOP[lang]}</a>
  </div>
</footer>
<script src="{url('/assets/js/main.js')}"></script>
{f'<script src="{url("/assets/js/bubble-tea.js")}"></script>' if page_key == 'table-bubble-tea' else ''}
</body>
</html>"""


FOOTER_CREDIT = {
    "en": "Go Have Tea — Tea Travels: Leaves, Care, and Everyday Invention. "
    "Curated by Junhong (Summer) Ma. Calligraphy by Ying (Joy) Wen. Paintings by Hui Yang.",
    "zh": "吃茶去 · 茶在路上：叶、照护与日常创造。策展：马俊虹（Summer）。书法：文莹。绘画：杨慧。",
}
FOOTER_META = {
    "en": "A three-table exhibition for the 2026 Edmonton Heritage Festival. "
    "Website content package prepared July 2026.",
    "zh": "2026年埃德蒙顿民俗节三桌小型展览。网站内容包于2026年7月编制。",
}
