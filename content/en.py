# -*- coding: utf-8 -*-
"""English page content for Go Have Tea.

v2.0 revision (2026-08-01): patched per the exhibition team's Master
Revision Brief — corrected names/credits, confirmed event info, removed
public placeholders and internal production notes, expanded Goji/
Osmanthus/Glossary, added Tea Tips + Further Reading, trimmed homepage
and table-page density. See /content-qa.md for items left on hold.
"""

PAGES = {}

# --------------------------------------------------------------------- home
PAGES["home"] = {
    "title": "Go Have Tea | Tea Travels in Edmonton",
    "meta": "Go Have Tea: a digital exhibition for the Chinese Pavilion at the 2026 Edmonton Heritage Festival (Aug 1–3, Hawrelak Park) — Chinese tea, Edmonton goji stories, bubble tea, calligraphy, and painting.",
    "blocks": [
        {"type": "hero", "eyebrow": "A digital exhibition from Edmonton", "title": "Go Have Tea",
         "lead": "Tea is more than a drink. In Edmonton, it carries stories of migration, hospitality, memory, labour, and everyday life.",
         "buttons": [
             {"label": "Explore the Three Tables", "href": "/en/tables/"},
             {"label": "Visit the Poster Gallery", "href": "/en/posters/", "variant": "secondary"},
         ]},
        {"type": "heading", "level": 2, "text": "Chinese Pavilion"},
        {"type": "para", "text": "Go Have Tea is presented as part of the Chinese Pavilion at the 2026 Edmonton Heritage Festival, supported by the Chinese Graduates Association of Alberta (CGAA), which has sponsored the pavilion since 1978."},
        {"type": "buttons", "items": [{"label": "Visit the CGAA website", "href": "https://www.cgaa.ab.ca/", "external": True}]},
        {"type": "para", "class": "event-strip", "text": "Edmonton Heritage Festival · Chinese Pavilion · Hawrelak Park · August 1–3, 2026"},
        {"type": "para", "text": "Created for the Chinese Pavilion at the 2026 Edmonton Heritage Festival, Go Have Tea brings together three exhibition tables: Chinese tea, wellness and Edmonton goji stories, and bubble tea. Painting, calligraphy, fieldwork photographs, posters, and familiar objects invite visitors to see how tea changes as it moves—and how people make new forms of home around it."},
        {"type": "image", "src": "home-hero.jpg",
         "alt": "Illustrated poster reading 喝茶，慢活 / Tea, at Edmonton's Pace, with a flowing gold ink ribbon over a watercolour view of the North Saskatchewan River Valley and the Edmonton skyline.",
         "caption": "Tea, at Edmonton’s pace — the open current of the North Saskatchewan River Valley."},
        {"type": "heading", "level": 2, "text": "Why “Go Have Tea”?"},
        {"type": "para", "text": "“Go have tea” is an everyday invitation, associated with Chan master Zhaozhou: slow down before judging, sit together before explaining. It is not a cure for conflict—just a modest practice of attention."},
        {"type": "buttons", "items": [{"label": "Read the full interpretation", "href": "/en/posters/go-have-tea/"}]},
        {"type": "heading", "level": 2, "text": "Three ways tea travels"},
        {"type": "columns", "items": [
            {"title": "One Leaf, Many Teas", "href": "/en/tables/chinese-tea/",
             "text": "See how one plant becomes many teas through local knowledge, tools, timing, and sensory judgment."},
            {"title": "Wellness & Goji Stories", "href": "/en/tables/wellness-goji/",
             "text": "Follow goji through Edmonton’s river valley, family gardens, community memory, and Yong Fei Guan’s Edmonton Goji Map."},
            {"title": "Build a Bubble Tea", "href": "/en/tables/bubble-tea/",
             "text": "Explore a drink that developed in Taiwan in the 1980s and became a global system of customization, franchising, and service work."},
        ]},
        {"type": "image", "src": "home-mountain.jpg",
         "alt": "Illustrated poster reading 喝茶，慢活 / Tea, at Edmonton's Pace, over a misty mountain landscape with two figures on a mountain path, captioned Mountain air · North Saskatchewan River Valley.",
         "caption": "Less rush. More room for tea."},
        {"type": "heading", "level": 2, "text": "Art in the exhibition"},
        {"type": "para", "text": "Calligraphy by Wen Ying and paintings by Yang Hui do not simply decorate the tables—they help the exhibition think, from 吃茶去 as an everyday action to 和而不同, harmony without sameness, as its ethical direction."},
        {"type": "image", "src": "home-go-have-tea-postcard.jpg",
         "alt": "A bold green and tan Go Have TEA poster pairing Wen Ying's 吃茶去 calligraphy with a lotus-pod illustration, credited to Ma Junhong (Summer), calligraphy and artwork by Wen Ying and Yang Hui, with help from CGAA volunteers.",
         "caption": "Go Have Tea — calligraphy by Wen Ying, artwork by Yang Hui."},
        {"type": "buttons", "items": [
            {"label": "Meet the artists", "href": "/en/artists/"},
            {"label": "View the poster gallery", "href": "/en/posters/", "variant": "secondary"},
        ]},
        {"type": "image", "src": "home-poster-preview.jpg",
         "alt": "Three poster mockups stacked together: Go Have Some Tea and A Cup for You, both featuring Wen Ying's 吃茶去 calligraphy and illustrated teaware, and Put Down Your Worries, featuring 放下烦恼 calligraphy beside a painted tiger.",
         "caption": "A preview of the poster series."},
        {"type": "heading", "level": 2, "text": "Before you leave"},
        {"type": "para", "text": "Take one question with you:"},
        {"type": "quote", "text": "Which plant, drink, object, or smell makes you think of home?"},
    ],
}

# -------------------------------------------------------------------- about
PAGES["about"] = {
    "title": "About | Go Have Tea",
    "meta": "About Go Have Tea: the exhibition, why it was created, curator Junhong (Summer) Ma, and community partner CGAA — presented at the 2026 Edmonton Heritage Festival, August 1–3, Hawrelak Park.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "About"},
        {"type": "heading", "level": 2, "text": "The Exhibition"},
        {"type": "para", "text": "Go Have Tea is a digital and in-person exhibition created for the Chinese Pavilion at the 2026 Edmonton Heritage Festival. It follows three exhibition tables—Chinese tea, wellness and Edmonton goji stories, and bubble tea—through craft, migration, care, business, and everyday invention. Painting, calligraphy, fieldwork photographs, and familiar objects show how tea changes as it moves, and how people build new forms of home around it in Edmonton."},
        {"type": "heading", "level": 2, "text": "Why It Was Created"},
        {"type": "para", "text": "Public conversations about Chinese tea often move to two extremes: a timeless national tradition, or a simple consumer choice. Both leave out the people and relationships that make tea possible. Go Have Tea follows movement instead—a leaf becoming many teas, a plant taking root in Edmonton, a Taiwanese drink entering shops, franchises, and youth culture—to make that labour and history visible."},
        {"type": "heading", "level": 2, "text": "Curator"},
        {"type": "para", "text": "Junhong (Summer) Ma is a cultural anthropologist whose work focuses on contemporary Chinese and East Asian tea culture, public anthropology, migration, service labour, and the movement of tea knowledge across places. She holds a PhD from the University of Alberta and is a postdoctoral researcher at Xiamen University."},
        {"type": "para", "text": "She created Go Have Tea to bring anthropological research into a public setting through objects, artworks, stories, and conversation. Rather than presenting Chinese tea as one timeless tradition, the exhibition follows how tea is made, carried, adapted, sold, remembered, and shared in everyday life."},
        {"type": "image", "src": "about-curator.jpg",
         "alt": "Curator Junhong (Summer) Ma smiling in a candid travel photo, hands together in a wai greeting.",
         "caption": "Curator Junhong (Summer) Ma."},
        {"type": "buttons", "items": [{"label": "Read the curator’s full statement", "href": "/en/curator/"}]},
        {"type": "heading", "level": 2, "text": "Community Partner"},
        {"type": "para", "text": "Go Have Tea is presented as part of the Chinese Pavilion at the 2026 Edmonton Heritage Festival. CGAA has supported and sponsored Edmonton’s Chinese Pavilion since 1978, bringing together performances, arts, crafts, food, volunteers, and community participation."},
        {"type": "buttons", "items": [{"label": "Visit the CGAA website", "href": "https://www.cgaa.ab.ca/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Event Details"},
        {"type": "list", "items": [
            "Edmonton Heritage Festival 2026 — August 1–3, Hawrelak Park, Edmonton",
            "Saturday, August 1: 12:00 pm–9:00 pm",
            "Sunday, August 2: 10:00 am–9:00 pm",
            "Monday, August 3: 10:00 am–8:00 pm",
            "Presented as part of the Chinese Pavilion, supported by CGAA",
        ]},
        {"type": "buttons", "items": [{"label": "Edmonton Heritage Festival 2026", "href": "https://www.heritagefest.ca/2026festival", "external": True}]},
        {"type": "para", "text": "Language: English website with a 中文 switch. Food and drink: display and educational activities only, unless a specific service is separately approved."},
    ],
}

# ------------------------------------------------------------- tables (all)
PAGES["tables"] = {
    "title": "Three Exhibition Tables | Go Have Tea",
    "meta": "The Go Have Tea exhibition is arranged as three tables — Chinese Tea, Wellness & Goji, and Bubble Tea — that tell one connected story.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Three Exhibition Tables"},
        {"type": "para", "text": "Three tables follow tea through craft, migration, care, business, and everyday invention. Start anywhere, then notice what changes from one table to the next."},
        {"type": "columns", "items": [
            {"title": "Chinese Tea — Transform", "href": "/en/tables/chinese-tea/", "text": "One plant, many processes, many traditions."},
            {"title": "Wellness & Goji — Take root", "href": "/en/tables/wellness-goji/", "text": "Plants, family knowledge, migration, and care in Edmonton."},
            {"title": "Bubble Tea — Remix", "href": "/en/tables/bubble-tea/", "text": "Taiwanese invention, global movement, customization, and labour."},
        ]},
    ],
}

# ------------------------------------------------------------ table pages
PAGES["table-chinese-tea"] = {
    "title": "Chinese Tea: One Plant, Many Teas | Go Have Tea",
    "meta": "Green, white, yellow, oolong, black, and dark teas can all begin with the same plant, Camellia sinensis — see how skilled makers transform one plant into many traditions.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Chinese Tea"},
        {"type": "heading", "level": 2, "text": "Quick View"},
        {"type": "para", "text": "Green tea, white tea, oolong, black tea, and dark tea can all begin with the same plant: Camellia sinensis. What makes them different is what people do with the fresh leaves after picking—how they rest, heat, roll, oxidize, dry, or continue to transform."},
        {"type": "para", "text": "You do not need to memorize every process. Look at the leaves, smell the tea, and compare colour and shape. One plant can become many teas because knowledge, tools, timing, and local practice shape it in different ways."},
        {"type": "heading", "level": 2, "text": "Skill, Not a Recipe"},
        {"type": "para", "text": "A process list can say “wither, roll, oxidize, dry,” but it cannot capture a maker’s judgment: how withered is “enough,” how the leaf should feel, when to add heat. These decisions come from the body, the season, and years of comparison—which is why this table avoids treating one method, or one serving style, as the only real Chinese tea. Gongfu-style preparation is one important practice among many; tea also lives in thermoses, office mugs, family kitchens, and gifts."},
        {"type": "heading", "level": 2, "text": "Historical Background"},
        {"type": "para", "text": "Physical evidence supports cautious claims about tea use more than two thousand years ago—not a single unbroken “five-thousand-year” history. UNESCO’s recognition of Chinese tea-processing techniques is useful because it links growing, picking, processing, and sharing, but heritage recognition should not freeze a living practice: technique keeps changing through research, climate, markets, and the people who make tea."},
        {"type": "heading", "level": 2, "text": "Hospitality and the Everyday"},
        {"type": "para", "text": "A cup can welcome a guest, mark a pause in work, or become a small performance of expertise—and none of that happens automatically. Someone buys the tea, heats the water, cleans the vessels, and notices whether a guest is comfortable. That labour is part of tea culture too."},
        {"type": "heading", "level": 2, "text": "Look Closer"},
        {"type": "triad", "items": [
            {"label": "LOOK", "text": "Find one visible change in the leaf."},
            {"label": "ASK", "text": "Which part of the process depends on skilled judgment?"},
            {"label": "REMEMBER", "text": "Tradition is not a frozen recipe. It lives through people, places, and repeated practice."},
        ]},
        {"type": "para", "text": "Deeper process terms — withering, oxidation, microbial transformation, and more — are explained in the Tea Glossary."},
        {"type": "keywords", "items": ["Camellia sinensis", "craft", "withering", "heat-fixing", "oxidation", "microbial transformation", "drying", "gongfu tea", "hospitality", "living tradition"]},
        {"type": "image", "src": "chinesetea-gohavetea-art.jpg",
         "alt": "Wen Ying's 吃茶去 (Go Have Tea) calligraphy beside a painted mountain landscape, from the exhibition's poster series.",
         "caption": "吃茶去 — calligraphy by Wen Ying, landscape by Yang Hui."},
        {"type": "image", "src": "chinesetea-beyondtea-art.jpg",
         "alt": "Wen Ying's 茶外有茶 (Beyond Tea) calligraphy over a watercolour view of the North Saskatchewan River Valley and Edmonton skyline, linked by a flowing gold and ink ribbon.",
         "caption": "茶外有茶 — Beyond Tea, from the exhibition's poster series."},
    ],
}

PAGES["table-wellness-goji"] = {
    "title": "Wellness & Goji Stories | Go Have Tea",
    "meta": "Goji shrubs have grown in Edmonton’s river valley and family gardens since Chinese migrants arrived in the 1890s — researched primarily by Yong Fei Guan (关咏霏), Edmonton Goji Map.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Wellness & Goji"},
        {"type": "heading", "level": 2, "text": "Quick View"},
        {"type": "para", "text": "Plants travel with people. Goji shrubs have grown in Edmonton since Chinese migrants arrived in the 1890s. Today they can be found in the river valley and in family gardens."},
        {"type": "para", "text": "Here, wellness is not a promise of cure. It is a story about migration, family knowledge, adaptation, trade, hospitality, and everyday care."},
        {"type": "note", "style": "notice", "label": "Primary research contributor", "text": "Yong Fei Guan (关咏霏). This section is based primarily on Guan’s research and public work on Edmonton goji. His Edmonton Goji Map follows the plant through the river valley, community histories, art, and changing ideas of home."},
        {"type": "buttons", "items": [{"label": "Explore the Edmonton Goji Map", "href": "https://edmonton-goji.github.io/Map/", "external": True}]},
        {"type": "image", "src": "goji-spread.jpg",
         "alt": "An illustrated panel titled Goji, Tisane, and Care in Edmonton, showing Wen Ying's 放下烦恼 calligraphy, painted teaware, goji, chrysanthemum, and dried citrus peel, and a watercolour Edmonton river-valley skyline with a bowl of goji berries.",
         "caption": "Goji, tisane, and care in Edmonton."},
        {"type": "heading", "level": 2, "text": "A Plant on the Move"},
        {"type": "para", "text": "Artist-researcher Yong Fei Guan’s Living History of Gojis in Edmonton and Edmonton Goji Map bring together plant life, Chinese Canadian history, family gardens, neighbourhood knowledge, and public art. In Edmonton, goji can be a river-valley shrub, a backyard plant, a gift between neighbours, a memory of an older family member, or a subject of contemporary art—not just a packaged “superfood.”"},
        {"type": "heading", "level": 2, "text": "Plants Take Root Twice"},
        {"type": "para", "text": "A plant takes root in soil, but also in memory. Migrants carry seeds, tastes, names, and expectations into a new climate that changes what survives and how it is used—neighbours exchange cuttings, and a child may recognize a packaged berry before the shrub itself. The Edmonton goji story is not a simple “preservation” story: the plant adapts, people adapt, and meaning changes, without losing its longer route here."},
        {"type": "heading", "level": 2, "text": "Care, Not Cure"},
        {"type": "para", "text": "The table also introduces floral and herbal infusions and Canadian-grown American ginseng, showing that movement runs in both directions between North America and Asia. The exhibition does not rank family knowledge against professional or scientific knowledge—it asks how different kinds of authority meet in an everyday cup, and where a real health question belongs with a healthcare professional instead."},
        {"type": "note", "style": "notice", "label": "Educational notice", "text": "This page shares cultural histories and community practices. It does not provide medical advice or recommend treatment."},
        {"type": "heading", "level": 2, "text": "Osmanthus: A Fragrance of the Season"},
        {"type": "para", "text": "Osmanthus has long been an important seasonal ingredient in Jiangnan, the lower Yangtze region of China. Its small flowers are gathered for their distinctive fragrance and used in tea, sweet osmanthus preserved with sugar, desserts, and seasonal drinks."},
        {"type": "para", "text": "“Osmanthus tea” can mean tea leaves scented or blended with osmanthus, or an infusion made mainly from the flowers. Everyday names do not always follow strict botanical categories. At the exhibition table, visitors can see dried osmanthus and an osmanthus tea display, then consider how fragrance carries memories of season and place."},
        {"type": "quote", "text": "桂子月中落，天香云外飘。", "attribution": "Traditionally attributed to Song Zhiwen, “Lingyin Temple” (Tang dynasty)"},
        {"type": "heading", "level": 2, "text": "Exhibition Table"},
        {"type": "para", "text": "At the physical table, the goji branch, dried berries, map, floral infusions, and community practice cards connect local plants with memories and routes. Some cups contain true tea from Camellia sinensis; others are more precisely herbal infusions or tisanes—everyday Chinese speech may still call both “tea.”"},
        {"type": "image", "src": "goji-edmonton.jpg",
         "alt": "A watercolour spread of dried goji berries and Edmonton's river valley, with a small map and community story cards linking the plant to migration, gardens, memory, and care.",
         "caption": "Goji, Edmonton's river valley, and the routes that connect them."},
        {"type": "image", "src": "goji-river-vessels.jpg",
         "alt": "Illustrated poster reading 喝茶，慢活 / Tea, at Edmonton's Pace, titled River Vessels, showing painted teaware — a mug, a gaiwan, a French press, and a teacup — over a soft river-valley background.",
         "caption": "River vessels — everyday teaware, Edmonton style."},
        {"type": "heading", "level": 2, "text": "Look Closer"},
        {"type": "triad", "items": [
            {"label": "TRACE", "text": "Follow goji into Edmonton."},
            {"label": "ASK", "text": "Which plant makes you think of home?"},
            {"label": "REMEMBER", "text": "Care is a practice and a relationship, not a universal cure claim."},
        ]},
        {"type": "keywords", "items": ["goji", "migration", "take root", "home", "care", "herbal infusion", "tisane", "osmanthus", "American ginseng", "Yong Fei Guan"]},
    ],
}

PAGES["table-bubble-tea"] = {
    "title": "Bubble Tea: Build a Cup | Go Have Tea",
    "meta": "Pearl milk tea developed in Taiwan in the 1980s and travelled fast — build a cup, then look behind it at customization, franchising, and service labour.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Bubble Tea"},
        {"type": "heading", "level": 2, "text": "Quick View"},
        {"type": "para", "text": "Bubble tea is a drink, a customizable menu, a service system, and a social space. Developed in Taiwan in the 1980s, it has travelled through shops, franchises, digital ordering, migration, and youth culture. This table looks beyond the finished cup to the choices, ingredients, equipment, and labour that make it possible."},
        {"type": "image", "src": "bubbletea-spread.jpg",
         "alt": "An illustrated panel titled Bubble Tea in Edmonton, showing Wen Ying's 和而不同 calligraphy, an illustrated bubble tea cup and teaware, icons for tea base, sweetness, and toppings, and an Edmonton skyline silhouette.",
         "caption": "Bubble tea in Edmonton — table 3 of the exhibition."},
        {"type": "heading", "level": 2, "text": "Build a Cup"},
        {"type": "bubble_builder"},
        {"type": "heading", "level": 2, "text": "Invention and Disagreement"},
        {"type": "para", "text": "It is safest to say that pearl milk tea developed in Taiwan in the 1980s—Hanlin Tea Room and Chun Shui Tang both tell origin stories, and the exhibition does not resolve the dispute in favour of one company. That uncertainty is itself historical: invention is often narrated only after a product becomes valuable, and brand stories, legal disputes, and national promotion all help turn a drink into an icon."},
        {"type": "heading", "level": 2, "text": "Why Bubble Tea Travels So Well"},
        {"type": "para", "text": "Bubble tea can be shaken, photographed, branded, franchised, and adjusted to local taste—its modular form lets shops vary tea base, milk, sugar, toppings, and ordering technology while keeping the drink recognizable. The same modularity connects “slow” tea shops built for sitting and talking with faster small-format counters built for portability; neither is simply more authentic, each just organizes time and labour differently."},
        {"type": "heading", "level": 2, "text": "Behind the Cup"},
        {"type": "para", "text": "Customization depends on standardization. Someone develops recipes, sources tea and toppings, manages cold storage, trains workers, maintains machines, and keeps service friendly under time pressure—labour that a bright menu and a cheerful cup can make easy to forget."},
        {"type": "heading", "level": 2, "text": "Bubble Tea in Edmonton"},
        {"type": "para", "text": "In Edmonton, bubble tea connects with migration, student life, shopping centres, Chinatown and suburban commercial areas, family entrepreneurship, global chains, independent shops, and social media—a Taiwanese drink becoming local in different neighbourhoods."},
        {"type": "heading", "level": 2, "text": "Make and Reflect"},
        {"type": "triad", "items": [
            {"label": "MAKE", "text": "Build a cup above."},
            {"label": "ASK", "text": "Which choice feels most like you, and why?"},
            {"label": "LOOK BEHIND THE CUP", "text": "What labour, ingredients, transport, and technology made your choices possible?"},
        ]},
        {"type": "keywords", "items": ["pearl milk tea", "Taiwan", "shaken tea", "customization", "modular menu", "franchising", "supply chain", "service labour", "diaspora", "social media"]},
    ],
}

# ------------------------------------------------------------------ posters
PAGES["posters"] = {
    "title": "Poster Gallery | Go Have Tea",
    "meta": "Calligraphy, painting, poetry, objects, and Edmonton landscapes carry the exhibition’s central questions across thirteen posters.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Poster Gallery"},
        {"type": "para", "text": "Created around the three Heritage Festival tables, this poster series brings the exhibition’s ideas into images, calligraphy, and short texts."},
        {"type": "gallery_grid", "items": [
            {"title": "Beyond Tea", "href": "/en/posters/beyond-tea/", "sub": "Beyond the drink: the people, labour, and histories tea carries."},
            {"title": "Pause. Sip. Be Here.", "href": "/en/posters/pause-sip-be-here/", "sub": "Chan and tea share one taste."},
            {"title": "Go Have Tea", "href": "/en/posters/go-have-tea/", "sub": "Go have some tea."},
            {"title": "Harmony, Not Sameness", "href": "/en/posters/harmony-not-sameness/", "sub": "Harmony without sameness."},
            {"title": "A Cup for the City", "href": "/en/posters/a-cup-for-the-city/", "sub": "Send this bowl to someone who loves tea."},
            {"title": "Slow Down, Edmonton", "href": "/en/posters/slow-down-edmonton/", "sub": "With less, one gains; with more, one is bewildered."},
            {"title": "Be Still. Be Here.", "href": "/en/posters/be-still-be-here/", "sub": "Reach utmost openness; hold firmly to stillness."},
            {"title": "Many Names. One Edmonton.", "href": "/en/posters/many-names-one-edmonton/", "sub": "Different words. Distinct histories. A shared cup."},
            {"title": "Tea Travels Here", "href": "/en/posters/tea-travels-here/", "sub": "Across homes, neighbourhoods, generations."},
            {"title": "A World of Tea", "href": "/en/posters/a-world-of-tea/", "sub": "Many ways to share."},
            {"title": "Many Words for Tea", "href": "/en/posters/many-words-for-tea/", "sub": "Different names. Different routes."},
            {"title": "Edmonton Community Tea Poster Series", "href": "/en/posters/edmonton-community-series/", "sub": "Five posters that make Edmonton part of the story."},
            {"title": "Osmanthus Infusion", "href": "/en/posters/osmanthus-infusion/", "sub": "A small flower, a lingering fragrance."},
        ]},
    ],
}

PAGES["poster-beyond-tea"] = {
    "title": "Beyond Tea | Poster | Go Have Tea",
    "meta": "Poster: Beyond Tea / 茶外有茶 — the people, labour, and histories tea carries.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Beyond Tea"},
        {"type": "poster_meta", "chinese": "茶外有茶", "translation": "Beyond the drink: the people, labour, and histories tea carries."},
        {"type": "image", "src": "poster-beyond-tea.jpg",
         "alt": "Beyond Tea poster: black title text on orange, Wen Ying's 茶外有茶 calligraphy, a Jiaoran couplet, and a painted white lotus, credited to Ma Junhong (Summer), Wen Ying, and Yang Hui, with the CGAA logo.",
         "caption": "Beyond Tea — calligraphy by Wen Ying, artwork by Yang Hui."},
        {"type": "image", "src": "poster-beyond-tea-series.jpg",
         "alt": "Three poster designs shown together: Beyond Tea in orange, and two colour variants of Pause. Sip. Be Here. — one with white roses, one with a pink lotus.",
         "caption": "Beyond Tea alongside the Pause. Sip. Be Here. poster series."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Created for this exhibition, 茶外有茶 looks beyond tea as a drink to how it is grown, made, circulated, and shared—and to the people, labour, and histories involved."},
        {"type": "quote", "text": "Most people turn to wine; who understands the fragrance tea can bring?", "attribution": "Jiaoran, “Drinking Tea with Lu Yu on the Ninth Day” (Tang dynasty)"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Jiaoran’s poem is associated with the Double Ninth Festival, when drinking wine was customary. The lines contrast that convention with the shared appreciation of tea. They do not declare tea morally superior in every setting; they describe recognition between people who understand a particular fragrance and practice."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "“Beyond Tea” names the method of the whole exhibition. A cup contains more than a beverage: plants, land, skill, labour, transport, branding, service, memory, and relationships. The phrase asks visitors to look through the object without looking past the people who made it."},
        {"type": "heading", "level": 2, "text": "Artwork note"},
        {"type": "para", "text": "Uses an approved work or detail by Yang Hui and approved calligraphy by Wen Ying where present. The exact source image is credited beside the poster rather than one general credit for the entire gallery."},
    ],
}

PAGES["poster-pause-sip-be-here"] = {
    "title": "Pause. Sip. Be Here. | Poster | Go Have Tea",
    "meta": "Poster: Pause. Sip. Be Here. / 禅茶一味 — Chan and tea share one taste.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Pause. Sip. Be Here."},
        {"type": "poster_meta", "chinese": "禅茶一味", "translation": "Chan and tea share one taste."},
        {"type": "image", "src": "poster-pause-sip-be-here.jpg",
         "alt": "Pause. Sip. Be Here. poster: Wen Ying's 禅茶一味 calligraphy beside a couplet on spring tea and bamboo, a teacup, and a glass vase of trailing greenery.",
         "caption": "Pause. Sip. Be Here. — calligraphy by Wen Ying."},
        {"type": "image", "src": "poster-pause-sip-be-here-alt.jpg",
         "alt": "An alternate colour variant of the Pause. Sip. Be Here. poster, with green title text and a spray of white roses beside Wen Ying's 禅茶一味 calligraphy.",
         "caption": "An alternate colourway of Pause. Sip. Be Here."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Slow down. Let one cup change your pace."},
        {"type": "para", "text": "禅茶一味 is a widely used expression in tea culture. It links tea with the attentiveness of Chan practice. “One taste” does not mean that tea and Buddhism are identical. It suggests that an everyday act—making and sharing tea—can become a practice of presence."},
        {"type": "quote", "text": "Spring is gathered in the mountains; fragrant tea is best brewed among bamboo.",
         "attribution": "春共山中採，香宜竹裡煎 — anonymous tea-shop couplet, date unknown; appears at least as early as the 1928 Shanghai edition of Fenlei Zhonghua Yinglian Daquan."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The exhibition treats 禅茶一味 as a later cultural formulation rather than a single ancient doctrine. Tea and Buddhist institutions have long histories of contact, but a modern slogan should not be projected unchanged into every earlier period."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The poster offers a pause inside the festival’s rush. Presence is not withdrawal from the world. It is a way to notice the cup, the people around it, and the conditions of an encounter."},
    ],
}

PAGES["poster-go-have-tea"] = {
    "title": "Go Have Tea | Poster | Go Have Tea",
    "meta": "Poster: Go Have Tea / 吃茶去 — associated with Chan master Zhaozhou, an invitation to return to the present moment.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Go Have Tea"},
        {"type": "poster_meta", "chinese": "吃茶去", "translation": "Go have some tea."},
        {"type": "image", "src": "poster-go-have-tea.jpg",
         "alt": "Go Have Tea poster: Wen Ying's 吃茶去 calligraphy beside a painted mountain landscape with a waterfall and flowering trees.",
         "caption": "吃茶去 — calligraphy by Wen Ying, landscape by Yang Hui."},
        {"type": "image", "src": "poster-go-have-tea-alt.jpg",
         "alt": "A Cup for You poster: Wen Ying's 吃茶去 calligraphy beside a painted horse, with four illustrated tea vessels below, credited to Ma Junhong (Summer), Wen Ying, and Yang Hui.",
         "caption": "A Cup for You — a related design using the same 吃茶去 calligraphy."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Preserved in later Chan encounter literature and associated with Chan master Zhaozhou Congshen (778–897), this everyday invitation is often read as a call to return to the present moment."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The phrase reaches us through later recorded encounter literature. The website says “associated with” Zhaozhou rather than presenting the poster’s wording as a securely transcribed statement from the moment itself."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "In this exhibition, 吃茶去 is neither an escape from difficult conversation nor a mystical answer. It is an invitation to slow classification down. Before explaining ourselves, we sit. Before reducing another person to a category, we share time. Tea does not erase difference; it can help create the conditions in which difference is met with attention."},
        {"type": "heading", "level": 2, "text": "Artwork information"},
        {"type": "para", "text": "Wen Ying, 吃茶去 / Go Have Tea, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton."},
    ],
}

PAGES["poster-harmony-not-sameness"] = {
    "title": "Harmony, Not Sameness | Poster | Go Have Tea",
    "meta": "Poster: Harmony, Not Sameness / 和而不同 — coexistence does not require assimilation.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Harmony, Not Sameness"},
        {"type": "poster_meta", "chinese": "和而不同", "translation": "Harmony without sameness."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Living together without becoming the same. Different words. Distinct histories. Shared attention."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The classical phrase is well known from the Analects: “The exemplary person seeks harmony but not sameness.” The exhibition does not use it to romanticize consensus. Harmony requires work, and differences of power do not disappear because people share a table."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "This phrase gives the exhibition an ethical horizon. Coexistence does not require assimilation. Difference should not be converted too quickly into hierarchy, suspicion, or stereotype. A shared cup is meaningful only when the people around it are allowed to remain different."},
        {"type": "heading", "level": 2, "text": "Artwork information"},
        {"type": "para", "text": "Wen Ying, 和而不同 / Harmony Without Sameness, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton."},
    ],
}

PAGES["poster-a-cup-for-the-city"] = {
    "title": "A Cup for the City | Poster | Go Have Tea",
    "meta": "Poster: A Cup for the City — from Bai Juyi’s wish to send tea to someone who loves it, to Edmonton’s neighbourhoods and newcomers.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "A Cup for the City"},
        {"type": "quote", "text": "If only I could send this bowl to someone who loves tea.", "attribution": "無由持一碗，寄與愛茶人 — Bai Juyi, “Brewing Tea at a Mountain Spring” (Tang dynasty)"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The line is from Bai Juyi’s Tang-dynasty poem “Brewing Tea at a Mountain Spring.” The poem begins with the physical acts of drawing water and watching tea brew, then turns an absent companion into the imagined recipient of a bowl."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "A cup can be small and still make room for a city. The poster connects an old wish to send tea with Edmonton’s distances, neighbourhoods, newcomers, and relationships. Hospitality is not only receiving someone already present; it can also be an act of remembering someone elsewhere."},
        {"type": "heading", "level": 2, "text": "Artwork note"},
        {"type": "para", "text": "Uses Yang Hui’s approved mountain landscape as the central image; the features needed to recognize the original work are not cropped away."},
    ],
}

PAGES["poster-slow-down-edmonton"] = {
    "title": "Slow Down, Edmonton | Poster | Go Have Tea",
    "meta": "Poster: Slow Down, Edmonton — Daodejing chapter 22, “with less, one gains; with more, one is bewildered.”",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Slow Down, Edmonton"},
        {"type": "quote", "text": "With less, one gains; with more, one is bewildered.", "attribution": "少则得，多则惑 — Daodejing, chapter 22"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The line appears in a passage of the Daodejing that questions accumulation and fixed self-assertion. It should not be reduced to a modern productivity slogan or an instruction to own less."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "At a crowded festival, “less” can mean making enough room to notice. The poster does not ask visitors to reject the city’s energy. It invites a different rhythm within it: fewer rushed conclusions, more attention to the leaf, cup, artwork, and person nearby."},
    ],
}

PAGES["poster-be-still-be-here"] = {
    "title": "Be Still. Be Here. | Poster | Go Have Tea",
    "meta": "Poster: Be Still. Be Here. — Daodejing chapter 16, “reach utmost openness; hold firmly to stillness.”",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Be Still. Be Here."},
        {"type": "quote", "text": "Reach utmost openness; hold firmly to stillness.", "attribution": "致虚極，守静筤 — Daodejing, chapter 16"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The line is often read as an invitation to observe change without immediately forcing or controlling it. Stillness here is not passivity and does not require leaving social life."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The poster places stillness inside Edmonton’s movement and weather. To be here is to notice where one is standing, who else is present, and how quickly difference can be judged. Attention becomes a quiet form of responsibility."},
    ],
}

PAGES["poster-many-names-one-edmonton"] = {
    "title": "Many Names. One Edmonton. | Poster | Go Have Tea",
    "meta": "Poster: Many Names. One Edmonton. — words for tea across languages, held beside one another without one origin story.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Many Names. One Edmonton."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Different words. Distinct histories. A shared cup."},
        {"type": "para", "text": "茶 · tea · thé · çay · شاي · चाय · 차 · お茶 · chai · чай"},
        {"type": "para", "text": "Selected common forms; pronunciation and usage vary by region."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Words such as cha, tea, and chai are often used to sketch routes of language and trade. They are useful clues, not a complete map. Similar words can move along different routes, change meanings, and enter languages more than once."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "Edmonton speaks tea in many languages. The poster does not collapse those languages into one origin story. It holds distinct histories beside one another and asks what sharing can mean without erasing difference."},
    ],
}

PAGES["poster-tea-travels-here"] = {
    "title": "Tea Travels Here | Poster | Go Have Tea",
    "meta": "Poster: Tea Travels Here — eight illustrated tea vessels form a neighbourhood portrait of Edmonton.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Tea Travels Here"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Across homes · neighbourhoods · generations."},
        {"type": "para", "text": "Many ways to make tea. Many ways to make Edmonton home."},
        {"type": "para", "text": "Movement does not erase difference; it creates new relations."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The illustrated cups and vessels refuse a single visual definition of tea. A porcelain cup, gaiwan, metal filter, mate gourd, fruit infusion, and teapot point toward different practices that meet in one city. The poster is not a taxonomy. It is a neighbourhood portrait made through objects."},
    ],
}

PAGES["poster-a-world-of-tea"] = {
    "title": "A World of Tea | Poster | Go Have Tea",
    "meta": "Poster: A World of Tea / Many Ways to Share — a portable postcard adaptation of the multilingual poster series.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "A World of Tea"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "A world of tea. Many ways to share."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "This horizontal postcard adapts the multilingual poster series to a portable object. Visitors can take it away, mail it, or use it as a small teaching prompt. Its portability continues the exhibition’s question: what changes when an image, word, or cup travels?"},
    ],
}

PAGES["poster-many-words-for-tea"] = {
    "title": "Many Words for Tea | Poster | Go Have Tea",
    "meta": "Poster: Many Words for Tea / 一叶多声 — Wen Ying’s Harmony Without Sameness calligraphy at the centre of tea words from ten languages.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Many Words for Tea"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Different names. Different routes. Many ways of sharing tea."},
        {"type": "para", "text": "One leaf · many languages · open encounters."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Tea words can suggest histories of maritime and overland exchange, but language does not prove a single route by itself. The poster therefore uses dotted paths as an invitation to inquire, not as a definitive trade map."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "Wen Ying’s 和而不同 calligraphy sits at the centre. The many names around it do not become one word, just as Edmonton’s communities do not need to become one culture. The shared table is meaningful because difference remains visible."},
    ],
}

PAGES["poster-edmonton-community-series"] = {
    "title": "Edmonton Community Tea Poster Series | Go Have Tea",
    "meta": "A five-poster series layering river-valley colours, map fragments, calligraphy, flowers, teaware, and mountain painting.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Edmonton Community Tea Poster Series"},
        {"type": "heading", "level": 2, "text": "Works in the series"},
        {"type": "list", "items": [
            "Many Names. One Edmonton.", "Tea Travels Here.", "Harmony, Not Sameness.", "Slow Down, Edmonton.", "A Cup for the City.",
        ]},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "This series makes Edmonton more than a background. River-valley colours, map fragments, winter light, neighbourhood language, calligraphy, flowers, teaware, and mountain painting are layered together. The result is not a claim that Edmonton and a classical Chinese landscape are the same. It is a visual study of how images acquire new relations when they travel."},
    ],
}

PAGES["poster-osmanthus-infusion"] = {
    "title": "Osmanthus Infusion | Poster | Go Have Tea",
    "meta": "Poster: Osmanthus Infusion — a small flower, a lingering fragrance, and the boundary between tea and floral infusion.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Osmanthus Infusion"},
        {"type": "para", "text": "A small flower, a lingering fragrance."},
        {"type": "image", "src": "poster-osmanthus-infusion.jpg",
         "alt": "Osmanthus Infusion poster: a Song Zhiwen couplet about osmanthus and moonlight, beside a photograph of dried osmanthus in a glass jar and a cup of osmanthus tea, over a watercolour river landscape.",
         "caption": "A small flower, a lingering fragrance."},
        {"type": "quote", "text": "Osmanthus falls from the moon; its heavenly fragrance drifts beyond the clouds.",
         "attribution": "桂子月中落，天香云外飘 — Tang dynasty; traditionally attributed to Song Zhiwen, “Lingyin Temple”"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Dried osmanthus can be infused on its own or paired with green, oolong, or black tea. Without tea leaves, it is more precisely a floral infusion—a tisane—though everyday Chinese still commonly calls it guihua cha."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The poster begins with a small material and opens into landscape, memory, and naming. Smell can cross time quickly. The visitor prompt—“Where does this fragrance take you?”—invites a personal response without turning it into a medical claim."},
        {"type": "note", "style": "notice", "label": "Educational notice", "text": "For cultural learning and discussion; not medical advice."},
    ],
}

# ------------------------------------------------------------------ artists
PAGES["artists"] = {
    "title": "Artists | Go Have Tea",
    "meta": "The paintings of Yang Hui and the calligraphy of Wen Ying shape how the exhibition can be read.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Artists"},
        {"type": "para", "text": "The exhibition was developed through a conversation among research, painting, calligraphy, graphic composition, and public interpretation. The artworks are not generic signs of “Chinese tradition.” Each one changes how the exhibition can be read."},
        {"type": "para", "text": "Yang Hui’s paintings bring mountains, vessels, flowers, animals, and material attention into the project. Wen Ying’s calligraphy gives visual weight to short phrases that organize the exhibition’s ethics and rhythm."},
        {"type": "gallery_grid", "items": [
            {"title": "Yang Hui", "href": "/en/artists/yang-hui/", "sub": "Painter"},
            {"title": "Wen Ying", "href": "/en/artists/wen-ying/", "sub": "Calligrapher"},
        ]},
    ],
}

PAGES["artist-yang-hui"] = {
    "title": "Yang Hui | Artist | Go Have Tea",
    "meta": "Painter Yang Hui brings mountains, vessels, flowers, and material attention into the Go Have Tea exhibition.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Yang Hui"},
        {"type": "image", "src": "artist-yang-hui.jpg",
         "alt": "Painter Yang Hui smiling outdoors, holding a large moose antler, with snow-capped mountains behind her.",
         "caption": "Yang Hui, painter."},
        {"type": "para", "text": "Yang Hui contributes painting to Go Have Tea. Her landscapes, teaware, and floral works bring movement, place, and material attention into the exhibition. Rather than serving as a decorative sign of “tradition,” each painting should be encountered as an individual artwork with its own title, date, medium, dimensions, and visual rhythm."},
        {"type": "para", "text": "In After Wang Meng’s Ge Zhichuan Moving His Dwelling, a classical composition is re-situated through a work made in Edmonton. The image of a family moving through mountains can be read not simply as retreat, but as reorientation: a search for rhythm, shelter, dignity, and renewed relation in a changing environment."},
        {"type": "heading", "level": 2, "text": "Featured Work"},
        {"type": "quote", "text": "Yang Hui, After Wang Meng’s Ge Zhichuan Moving His Dwelling / 仿王蒙《葛稚川移居图》, 2022, acrylic on canvas, 24 × 60 in., Edmonton."},
    ],
}

PAGES["artist-wen-ying"] = {
    "title": "Wen Ying | Calligrapher | Go Have Tea",
    "meta": "Calligrapher Wen Ying created the works 吃茶去 and 和而不同 that give the exhibition its central visual language.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Wen Ying"},
        {"type": "image", "src": "artist-wen-ying.jpg",
         "alt": "Calligrapher Wen Ying outdoors on a sunny street, wearing sunglasses and a patterned sun hat.",
         "caption": "Wen Ying, calligrapher."},
        {"type": "para", "text": "Wen Ying contributes calligraphy to Go Have Tea. Her works Go Have Tea and Harmony, Not Sameness give the exhibition’s central phrases weight, spacing, gesture, and pace. The website should show the complete calligraphy before using any detail or crop."},
        {"type": "para", "text": "Calligraphy is not decorative proof of cultural authenticity here. The shape, pressure, spacing, and rhythm of the brush make short phrases feel bodily and present—吃茶去 turns the exhibition’s central idea into an action, and 和而不同 makes coexistence without assimilation visible as a vertical sequence of inked characters."},
        {"type": "heading", "level": 2, "text": "Featured Works"},
        {"type": "list", "items": [
            "Wen Ying, 吃茶去 / Go Have Tea, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton.",
            "Wen Ying, 和而不同 / Harmony Without Sameness, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton.",
        ]},
    ],
}

# ------------------------------------------------------------------ curator
PAGES["curator"] = {
    "title": "Junhong (Summer) Ma | Curator | Go Have Tea",
    "meta": "Curator Junhong (Summer) Ma, cultural anthropologist and postdoctoral researcher at Xiamen University, on why she created Go Have Tea.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Curator"},
        {"type": "heading", "level": 2, "text": "Short biography"},
        {"type": "para", "text": "Junhong (Summer) Ma is a cultural anthropologist and postdoctoral researcher at Xiamen University. Her research examines contemporary Chinese and East Asian tea culture, tea industries, cultural authority, service labour, branding, education, migration, and the movement of tea knowledge between Taiwan, mainland China, and Canada. She holds a PhD from the University of Alberta."},
        {"type": "heading", "level": 2, "text": "Curator’s statement"},
        {"type": "para", "text": "I created this exhibition because public conversations about Chinese tea often move in two unhelpful directions. Tea is either compressed into a timeless national tradition or reduced to a consumer choice. Both approaches miss the people and relationships that make tea possible."},
        {"type": "para", "text": "The three tables begin instead with movement. A leaf moves through skilled hands and becomes many teas. A plant moves with migrants and takes root in Edmonton. A drink developed in Taiwan moves through shops, franchises, digital menus, and young people’s social worlds."},
        {"type": "para", "text": "“Go Have Tea” became the central invitation because it is ordinary. It does not promise that a cup will solve disagreement. It asks whether we can create enough time and space for a different kind of encounter. The Daoist resonance lies in rhythm rather than doctrine: less coercion, less hurry to classify, more softness, listening, and room for relations to change."},
        {"type": "para", "text": "For me, this is what public anthropology can do at a festival. It can begin with something familiar, make hidden labour and history visible, and leave visitors with a question rather than a completed cultural definition."},
        {"type": "quote", "text": "Junhong (Summer) Ma", "attribution": "Curator and cultural anthropologist"},
        {"type": "buttons", "items": [
            {"label": "About the Exhibition", "href": "/en/about/"},
            {"label": "Credits", "href": "/en/sources-credits/", "variant": "secondary"},
        ]},
    ],
}

# ------------------------------------------------------------------- map
PAGES["edmonton-tea-map"] = {
    "title": "Edmonton Stories | Go Have Tea",
    "meta": "Tea in Edmonton lives in river-valley plants, family gardens, Chinatown histories, and shared tables — Edmonton Goji, the Chinese Pavilion, and the stories that connect them.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Edmonton Stories"},
        {"type": "para", "text": "Tea in Edmonton lives in more than tea shops. It appears in river-valley plants, family gardens, Chinatown histories, community events, grocery shelves, bubble tea counters, restaurants, student routines, thermoses, art projects, and shared tables."},
        {"type": "para", "text": "This is not a ranking or a complete business directory. It is an exhibition layer connecting places with the stories in the three tables."},
        {"type": "heading", "level": 2, "text": "Edmonton Goji"},
        {"type": "para", "text": "This module is built primarily on Yong Fei Guan (关咏霏)’s research and the Edmonton Goji Map, which follows the plant through the river valley, community histories, art, and changing ideas of home."},
        {"type": "buttons", "items": [{"label": "Explore the Edmonton Goji Map", "href": "https://edmonton-goji.github.io/Map/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Chinese Pavilion"},
        {"type": "para", "text": "Go Have Tea is presented as part of the Chinese Pavilion at the 2026 Edmonton Heritage Festival, supported by the Chinese Graduates Association of Alberta (CGAA), which has sponsored the pavilion since 1978."},
        {"type": "buttons", "items": [{"label": "Visit the CGAA website", "href": "https://www.cgaa.ab.ca/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Tea in Everyday Edmonton"},
        {"type": "para", "text": "Fieldwork photographs and neighbourhood stories will appear here as they are gathered and cleared for public use."},
        {"type": "heading", "level": 2, "text": "Map and List View"},
        {"type": "para", "text": "This map is not the only way in—every point below also appears as a plain-text list. Categories are never colour-only, and private home addresses or precise plant locations are never published without explicit permission."},
        {"type": "map_list", "groups": [
            {"title": "Plants and migration", "entries": [
                {"name": "Edmonton Goji Map", "desc": "Project-wide link to Yong Fei Guan’s map and bilingual eBook."},
            ]},
            {"title": "Chinese Canadian history", "entries": [
                {"name": "Goji Berry Teahouse, Fort Edmonton Park", "desc": "Archive entry for the 2023 project and its reflection on Chinese history, local goji, and home."},
                {"name": "Edmonton Chinatown / Boyle Street–McCauley", "desc": "Historical context area; no invented business genealogy."},
            ]},
            {"title": "The exhibition", "entries": [
                {"name": "2026 Heritage Festival — Chinese Pavilion", "desc": "Hawrelak Park, August 1–3, 2026."},
            ]},
        ]},
        {"type": "heading", "level": 2, "text": "Share a Story — Future"},
        {"type": "para", "text": "Community-submitted stories will open once a clear process for consent, credit, and withdrawal is in place. This is not yet available."},
        {"type": "heading", "level": 2, "text": "Where does tea live in your Edmonton?"},
    ],
}

# --------------------------------------------------------------- learning
PAGES["learning"] = {
    "title": "Learning Resources | Go Have Tea",
    "meta": "Guides for visitors, teachers, families, and community organizations to continue the Go Have Tea exhibition through observation, comparison, and discussion.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Learning Resources"},
        {"type": "para", "text": "These resources help visitors, teachers, families, and community organizations continue the exhibition. They are designed around observation, comparison, storytelling, and ethical discussion—not around memorizing one correct definition of tea culture."},

        {"type": "heading", "level": 2, "text": "One-Minute Exhibition Guide"},
        {"type": "para", "text": "Tea travels as leaf, plant, drink, skill, memory, and work. At the Chinese Tea table, look for how one plant becomes many teas. At the Wellness table, follow goji into Edmonton’s river valley and family gardens. At the Bubble Tea table, build a cup and then ask what labour and systems made your choices possible. In the poster gallery, notice how calligraphy, paintings, poems, and city landscapes change one another. There is no single correct route. Begin with what catches your attention."},

        {"type": "heading", "level": 2, "text": "Tea Travels Passport"},
        {"type": "para", "text": "Front: BUILD YOUR TEA TRAVELS PASSPORT"},
        {"type": "list", "items": ["Discover a craft.", "Build a milk tea.", "Find Edmonton goji."]},
        {"type": "para", "text": "Collect or place one sticker at each stop. There is no single correct cup."},
        {"type": "para", "text": "Back: What travels when tea travels? skill · memory · plants · labour · care · something else: ______. Which plant, cup, smell, or word makes you think of home?"},

        {"type": "heading", "level": 2, "text": "Teacher Guide"},
        {"type": "para", "text": "Suggested level: Grades 4–12, adaptable. Length: 45–60 minutes. Learning goals:"},
        {"type": "list", "items": [
            "Distinguish an object from the social relationships that produce it.",
            "Compare preservation, adaptation, invention, and commercialization without treating them as opposites.",
            "Identify how migration can change plants, tastes, words, and practices.",
            "Discuss sources, claims, and uncertainty.",
        ]},
        {"type": "para", "text": "Before viewing: Ask students to draw or describe a drink that matters in their family or everyday life. Who prepares it? Where do the ingredients come from? When is it served?"},
        {"type": "para", "text": "During viewing: Choose one table and one poster. Record three things you can see and three relationships that are not immediately visible."},
        {"type": "para", "text": "After viewing: Discuss when a changing tradition remains a tradition, who gets to call something authentic, how a menu organizes choice, and what responsibilities arise when health, heritage, or community stories are presented publicly."},
        {"type": "para", "text": "Activity: Create a “travelling object” card. Trace one ingredient, tool, word, or image across at least three places or people. Mark what changes and what stays recognizable."},

        {"type": "heading", "level": 2, "text": "Family Looking Guide"},
        {"type": "para", "text": "Find:"},
        {"type": "list", "items": [
            "one leaf with an unexpected shape",
            "one cup you have used before",
            "one word for tea you recognize",
            "one artwork that makes you slow down",
            "one sign of Edmonton",
            "one kind of work hidden behind a drink",
        ]},
        {"type": "para", "text": "Talk together: If you could send one cup to someone, who would receive it?"},

        {"type": "heading", "level": 2, "text": "Community Conversation Kit"},
        {"type": "para", "text": "Length: 45–75 minutes. Open with the phrase harmony without sameness. Invite each participant to name a drink or plant connected with care. Discuss what is gained and lost when a community practice becomes a product, festival display, health trend, or heritage symbol. Close by identifying one way to share a story without claiming to speak for everyone."},

        {"type": "heading", "level": 2, "text": "Accessible Text Pack"},
        {"type": "para", "text": "Contents: all main table texts in at least 18-point type; full poster transcripts; image descriptions; glossary; short URLs; educational notice."},

        {"type": "note", "style": "notice", "label": "Resource rights note", "text": "Downloadable files may include only images, fonts, maps, and artworks licensed for redistribution. A page that may legally display an embedded image does not automatically have permission to package it in a downloadable PDF."},
    ],
}

# --------------------------------------------------------------- glossary
PAGES["glossary"] = {
    "title": "Tea Glossary | Go Have Tea",
    "meta": "Basic vocabulary, tea processing, tea culture, and plants and drinks — key terms from the Go Have Tea exhibition, explained.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Tea Glossary"},
        {"type": "para", "text": "Forty terms in four groups, each with a short public explanation and one common point of confusion. Water-temperature and brewing guidance lives on the Tea Tips page instead."},

        {"type": "heading", "level": 2, "text": "Basic Vocabulary"},
        {"type": "definition_list", "items": [
            {"term": "Tea plant / Camellia sinensis", "def": "The single plant species behind green, white, yellow, oolong, black, and dark tea. People sometimes assume different tea types come from different plants; in fact almost all of them come from the same species, transformed differently after picking."},
            {"term": "Tea leaf", "def": "The picked leaf of Camellia sinensis, before or after processing. In everyday speech “tea leaf” can mean the raw leaf on the plant or the finished, dried product in a jar—context usually makes the difference clear."},
            {"term": "Brewed tea", "def": "The liquid produced once tea leaves meet water. English sometimes uses “tea” for both the leaves and the drink; this exhibition tries to say “brewed tea” or “tea leaves” specifically when the distinction matters."},
            {"term": "Loose-leaf tea", "def": "Whole or broken tea leaves sold without a bag, typically offering more room for the leaf to unfurl and a wider range of aroma and strength across multiple infusions than a standard tea bag."},
            {"term": "Tea bag", "def": "A small permeable pouch, usually holding broken or finely cut leaf (“fannings” or “dust”), designed for a single fast infusion. Convenient, but the smaller leaf pieces generally give less nuance than loose leaf."},
            {"term": "Teaware", "def": "The vessels used to make and serve tea: pots, cups, trays, and tools. Teaware is functional, not merely decorative—its shape and material genuinely change how a tea tastes and how a gathering unfolds."},
            {"term": "Gaiwan", "def": "A lidded bowl used to steep and serve tea, common across many Chinese tea traditions. It is one option among many, not the single “correct” Chinese teaware—large mugs and thermoses are just as common in daily life."},
            {"term": "Kettle", "def": "A vessel for heating water for tea. Different teas favour different temperatures (see Tea Tips), so a kettle that lets you control temperature is more useful than one that only boils."},
            {"term": "Infusion / steep", "def": "The act of letting tea (or another plant) sit in hot water so its flavour and aroma transfer into the liquid. “Infusion” is also used as a noun for the resulting drink, especially for non-tea plants."},
            {"term": "Tisane / herbal infusion", "def": "A drink made by steeping a plant other than Camellia sinensis—osmanthus or goji, for example. Botanically it is not “tea,” though everyday Chinese and English speech often still calls it tea."},
        ]},

        {"type": "heading", "level": 2, "text": "Tea Processing"},
        {"type": "definition_list", "items": [
            {"term": "Plucking", "def": "Picking fresh leaves and buds from the tea plant. Which leaves are chosen—one bud, two leaves, a coarser plucking—shapes the character and grade of the finished tea before any processing even begins."},
            {"term": "Withering", "def": "A controlled rest after plucking that lets leaves lose some moisture and soften. It sounds passive, but timing withering correctly is a skilled judgment call, not a fixed number of hours."},
            {"term": "Fixation / kill-green (杀青)", "def": "A heating step (dry-heat or steam) that halts the enzyme activity responsible for oxidation. It “fixes” a tea’s colour and character at that point, which is why green tea stays green while black tea does not."},
            {"term": "Rolling / shaping", "def": "Working the withered leaf by hand or machine to bruise cell walls, release aromatic compounds, and give the tea its final shape—curled, twisted, balled, or flat—which also affects how it later infuses."},
            {"term": "Oxidation", "def": "A chemical reaction between leaf compounds and oxygen, controlled by rolling, time, and humidity, that changes colour and flavour. It is a different process from microbial fermentation, though the two are often confused."},
            {"term": "Drying", "def": "The final moisture-removal step that stabilizes tea for storage and transport. Drying method and heat level affect aroma; done incorrectly, it can also mask or damage the work of every earlier step."},
            {"term": "Roasting", "def": "An additional heat treatment, sometimes applied after drying, that develops deeper, toastier, or fruitier notes—common in some oolongs. It is a finishing choice, not a step every tea receives."},
            {"term": "Scenting", "def": "Blending or layering tea with a fragrant flower or other aromatic, as with osmanthus- or jasmine-scented tea. Scenting can happen through repeated contact with fresh flowers or through blending with dried petals."},
            {"term": "Microbial transformation / fermentation", "def": "Change driven by microorganisms over time, important in some dark teas and other aged or piled processes. It is often loosely called “fermentation,” but it is chemically distinct from the oxidation used to make black tea."},
            {"term": "Ageing", "def": "Continued, usually slow change in a tea after processing is complete, sometimes intentional (as with some dark teas and pu’er) and sometimes simply a matter of storage. Not every tea benefits from ageing—many are meant to be drunk fresh."},
        ]},

        {"type": "heading", "level": 2, "text": "Tea Culture"},
        {"type": "definition_list", "items": [
            {"term": "Gongfu tea / 工夫茶", "def": "A preparation style emphasizing skill, attention, and repeated short infusions in small vessels, with specific regional and social histories. It is an important Chinese tea practice, not the only correct one."},
            {"term": "Hospitality", "def": "The social work of welcoming someone with tea: buying it, heating water, cleaning vessels, serving, and noticing whether a guest is comfortable. Hospitality is a practice, not something that simply happens on its own."},
            {"term": "Everyday care", "def": "Repeated small acts—serving tea, remembering a preference, checking in on someone—through which people look after each other day to day. It overlaps with wellness language but is not the same as medical treatment."},
            {"term": "Living tradition", "def": "Knowledge and practice that people keep renewing rather than freezing in place. Calling something a “living tradition” is a reminder that today’s tea makers are still actively shaping it, not just repeating the past."},
            {"term": "Authenticity", "def": "A claim that a practice, object, or flavour represents the “real” or “original” version of something. This exhibition treats authenticity as a question to investigate—who gets to decide, and why—rather than a label it hands out."},
            {"term": "Service labour", "def": "The work of preparing, explaining, cleaning, scheduling, and serving that keeps a cup of tea (or bubble tea) moving from ingredients to customer. It is often invisible precisely because it is done well."},
            {"term": "Customization", "def": "A system that lets a customer choose components—tea base, sugar, ice, toppings—rather than receiving one fixed drink. Customization depends on standardized ingredients and processes behind the counter, even though it feels personal up front."},
            {"term": "Public anthropology", "def": "Anthropological work made for dialogue with a wider public, not only academic readers—through exhibitions, writing, teaching, or art. This website and the exhibition it documents are both examples of the approach."},
            {"term": "Curatorial interpretation", "def": "The curator’s own reading of an object, artwork, or theme, offered as one informed perspective rather than a final, neutral fact. This exhibition labels curatorial interpretation clearly so visitors can tell it apart from historical record."},
            {"term": "Harmony without sameness / 和而不同", "def": "A classical phrase (from the Analects) used here to mean that people can share a table, a city, or a culture without becoming identical. It does not mean disagreement or difference should be smoothed over."},
        ]},

        {"type": "heading", "level": 2, "text": "Plants and Drinks"},
        {"type": "definition_list", "items": [
            {"term": "Goji / 枸杞", "def": "A fruit-bearing shrub with long histories of use across Asia, and a significant, still-living history in Edmonton’s river valley and family gardens since the 1890s. It is a plant and a set of relationships, not just a packaged “superfood.”"},
            {"term": "Osmanthus / 桂花", "def": "A small, intensely fragrant flower, an important seasonal ingredient in Jiangnan (the lower Yangtze region). Used to scent tea, or infused on its own—see “osmanthus tea” below for that distinction."},
            {"term": "Osmanthus tea / 桂花茶", "def": "An everyday name that can mean either tea leaves scented with osmanthus, or an infusion made mainly from the flowers themselves without any tea leaf. The name does not tell you which one you have—ask, or check the ingredients."},
            {"term": "Sweet osmanthus / 糖桂花", "def": "Osmanthus flowers preserved in sugar or syrup, used in desserts, drinks, and cooking across Jiangnan cuisine. It is a pantry ingredient as much as a tea-adjacent one."},
            {"term": "Bubble tea / pearl milk tea / 珍珠奶茶", "def": "A drink developed in Taiwan in the 1980s, typically combining tea, milk or creamer, sweetness, ice, and tapioca pearls or other toppings. Its exact origin is contested between two Taiwanese teahouses; this exhibition does not settle that dispute."},
            {"term": "Tea base", "def": "The tea component of a customized drink—black, green, oolong, or fruit tea, for example—chosen before milk, sweetness, and toppings are added. It is the one part of a bubble tea order that is actually tea in the botanical sense."},
            {"term": "Topping", "def": "An added ingredient in a customized drink—tapioca pearls, jelly, pudding—that changes texture as much as flavour. Toppings are prepared separately and require their own timing, storage, and labour behind the counter."},
            {"term": "Sweetness level", "def": "A menu option, usually shown as a percentage (0–100%), that lets a customer choose how much sugar syrup goes into a drink. It is a system built to make a wide range of tastes feel simple to order."},
            {"term": "Ice level", "def": "A menu option controlling how much ice goes into a cold drink, independent of sweetness or tea strength—choosing “less ice” usually means a stronger-tasting, less diluted drink, not just a colder or warmer one."},
            {"term": "Tapioca pearls / 珍珠", "def": "Chewy balls made from tapioca starch, the topping that gives pearl milk tea its name. They must be cooked, kept warm, and used within hours, which is part of the hidden labour behind a “simple” drink."},
        ]},
    ],
}

# ---------------------------------------------------------- sources-credits
PAGES["sources-credits"] = {
    "title": "Credits | Go Have Tea",
    "meta": "Curatorial, artist, and research credits for Go Have Tea, plus the exhibition’s selected public sources.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Credits"},
        {"type": "heading", "level": 2, "text": "Curator"},
        {"type": "para", "text": "Junhong (Summer) Ma / 马俊红"},
        {"type": "heading", "level": 2, "text": "Painting"},
        {"type": "para", "text": "Yang Hui / 杨慧"},
        {"type": "heading", "level": 2, "text": "Calligraphy"},
        {"type": "para", "text": "Wen Ying / 温颖"},
        {"type": "heading", "level": 2, "text": "Edmonton Goji Story and Primary Research Contribution"},
        {"type": "para", "text": "Yong Fei Guan (关咏霏), Edmonton Goji Map"},
        {"type": "buttons", "items": [{"label": "Edmonton Goji Map", "href": "https://edmonton-goji.github.io/Map/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Community Partner"},
        {"type": "para", "text": "Chinese Graduates Association of Alberta (CGAA). Presented as part of the Chinese Pavilion at the 2026 Edmonton Heritage Festival."},
        {"type": "buttons", "items": [{"label": "CGAA website", "href": "https://www.cgaa.ab.ca/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Materials and Generous Support"},
        {"type": "para", "text": "Yvonne Ho · Tabitha Lian"},

        {"type": "heading", "level": 2, "text": "Selected Exhibition Sources"},
        {"type": "list", "items": [
            '<a href="https://ich.unesco.org/en/RL/traditional-tea-processing-techniques-and-associated-social-practices-in-china-01884">UNESCO, “Traditional tea processing techniques and associated social practices in China”</a>',
            '<a href="https://www.nature.com/articles/srep18955">Lu et al., “Earliest tea as evidence for one branch of the Silk Road across the Tibetan Plateau,” Scientific Reports 6 (2016)</a>',
            '<a href="https://news.immigration.gov.tw/NewsSection/Detail/8dcaf253-faf4-42c8-87ef-e27eeb7ccee8?lang=EN">Taiwan National Immigration Agency, “The origins of bubble tea, one of Taiwan’s most beloved beverages”</a>',
            '<a href="https://www.edmontonarts.ca/blog/i-am-yeg-arts-yong-fei-guan">Edmonton Arts Council, “I Am YEG Arts: Yong Fei Guan”</a>',
            '<a href="https://edmonton-goji.github.io/Map/">Edmonton Goji Map</a>',
            '<a href="https://www.fortedmontonpark.ca/learn/blog/post/goji-berries-tearoom">Fort Edmonton Park, “Goji Berry Teahouse”</a>',
            '<a href="https://www.heritagefest.ca/2026festival">Edmonton Heritage Festival 2026</a>',
            '<a href="https://www.cgaa.ab.ca/">Chinese Graduates Association of Alberta (CGAA)</a>',
            '<a href="https://www.cgaa.ab.ca/projects/chinese-pavilion">CGAA — Chinese Pavilion</a>',
            '<a href="https://www.w3.org/TR/WCAG22/">W3C, Web Content Accessibility Guidelines (WCAG) 2.2</a>',
        ]},

        {"type": "heading", "level": 2, "text": "Primary Project Materials"},
        {"type": "list", "items": [
            "Edmonton Heritage Festival Tea Exhibit Research 2026.",
            "Go Have Tea: Tea, Landscape, and the Quiet Work of Anti-Racism, by Yang Hui, Wen Ying, and Junhong Ma.",
            "Final bilingual poster and postcard texts developed for the exhibition.",
            "Approved poster designs, artwork photographs, exhibition labels, curator notes, and educational materials.",
        ]},

        {"type": "heading", "level": 2, "text": "Image and Quotation Policy"},
        {"type": "para", "text": "Every image carries a nearby credit. Long quotations, community stories, portraits, recordings, maps, and photographs are reproduced only within their permissions. External links do not imply permission to copy material."},
        {"type": "heading", "level": 2, "text": "Educational and Research Notice"},
        {"type": "para", "text": "The wellness material shares cultural histories and community practices; it does not offer medical advice. Anonymous festival responses are not automatically research data. Any later academic use of identifiable visitor material requires a separate ethical and consent process."},
    ],
}

# -------------------------------------------------------------------- faq
PAGES["faq"] = {
    "title": "FAQ | Go Have Tea",
    "meta": "Frequently asked questions about the Go Have Tea exhibition: authenticity, herbal tea, bubble tea’s origins, and more.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "FAQ"},
        {"type": "faq", "items": [
            {"q": "Is there one authentic Chinese tea tradition?", "a": "No. The exhibition shows many regional, social, commercial, and everyday traditions. Authenticity is a question to investigate, not a label the exhibition awards to one method."},
            {"q": "Are herbal drinks really tea?", "a": "In botanical terms, tea comes from Camellia sinensis. Drinks made from other plants are more precisely herbal infusions or tisanes. Everyday language often uses “tea” more broadly."},
            {"q": "Who invented bubble tea?", "a": "Pearl milk tea developed in Taiwan in the 1980s. Hanlin Tea Room and Chun Shui Tang both claim invention, so the exact origin remains contested."},
            {"q": "Does goji cure illness?", "a": "This exhibition makes no medical claims. It focuses on migration, gardens, memory, trade, and practices of care."},
            {"q": "Why are paintings and calligraphy included?", "a": "They do interpretive work. The artworks shape how visitors think about movement, dwelling, attention, difference, and the material life of tea."},
            {"q": "What does “harmony without sameness” mean here?", "a": "Living together does not require everyone to become the same. Difference should not be turned automatically into hierarchy or suspicion."},
            {"q": "May I photograph the exhibition?", "a": "You may photograph the display unless a label says otherwise. Ask permission before photographing visitors, volunteers, artists, or community contributors."},
            {"q": "Why might there be no tasting?", "a": "Festival food and beverage service requires approved procedures. The exhibition’s core experience is designed to work through looking, smelling sealed samples where permitted, making, reading, and conversation."},
        ]},
    ],
}

# -------------------------------------------------------------------- tips
PAGES["tea-tips"] = {
    "title": "Tea Tips | Go Have Tea",
    "meta": "Friendly beginner tea-brewing tips: a simple method, water temperature by tea type, and what to do without a thermometer.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Tea Tips"},
        {"type": "para", "text": "Start simple. You need tea, water, a cup or pot, and a little attention. The suggestions below are starting points, not rules. Follow the package instructions when available, then adjust for your own taste."},
        {"type": "heading", "level": 2, "text": "A Simple Method"},
        {"type": "list", "ordered": True, "items": [
            "Warm your cup or pot with hot water if you like.",
            "Begin with about one teaspoon of loose tea for a 250 ml cup. Large, light leaves may need more space rather than more weight.",
            "Add water at a temperature suited to the tea.",
            "Taste after one to three minutes. If it is too strong, shorten the next infusion; if it is too light, add time or leaf.",
            "Many loose-leaf teas can be infused more than once. Add a little time with each round and notice what changes.",
        ]},
        {"type": "heading", "level": 2, "text": "Water Temperature — Friendly Starting Points"},
        {"type": "list", "items": [
            "Green tea: 75–85°C",
            "White tea: 80–90°C",
            "Oolong tea: 85–95°C",
            "Black tea: 90–100°C",
            "Dark tea and many pu’er teas: 95–100°C",
            "Herbal or floral infusions: follow the ingredient or package guidance",
        ]},
        {"type": "note", "style": "notice", "text": "No thermometer? Let fully boiled water rest briefly for delicate green or white tea. If a tea tastes harsh, try cooler water or less time before deciding that you dislike it."},
        {"type": "para", "text": "These are general brewing suggestions, not medical or dietary advice."},
        {"type": "buttons", "items": [{"label": "See the Tea Glossary", "href": "/en/glossary/"}]},
    ],
}

# ---------------------------------------------------------- further-reading
PAGES["further-reading"] = {
    "title": "Further Reading | Go Have Tea",
    "meta": "Six annotated books for readers who want to go further into tea history, science, and culture, chosen to match the exhibition’s central question.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Further Reading"},
        {"type": "para", "text": "Six books for readers who want to go further, chosen to match this exhibition’s central question: what travels when tea travels?"},

        {"type": "heading", "level": 2, "text": "Victor H. Mair and Erling Hoh, The True History of Tea"},
        {"type": "para", "text": "A broad, readable history that follows tea across regions, languages, trade routes, and political change. It is a useful starting point for the exhibition’s central question—what travels when tea travels—while more specialized studies can add detail and debate."},
        {"type": "buttons", "items": [{"label": "View at Thames & Hudson", "href": "https://www.thamesandhudsonusa.com/books/the-true-history-of-tea-softcover", "variant": "secondary", "external": True}]},

        {"type": "heading", "level": 2, "text": "Kevin Gascoyne, François Marchand, Jasmin Desharnais, and Hugo Américi, Tea: History, Terroirs, Varieties"},
        {"type": "para", "text": "Created by the Camellia Sinensis tea team, this illustrated introduction connects tea regions, processing, tasting, and brewing. It works especially well for visitors who want practical knowledge after seeing “One Plant, Many Teas.”"},
        {"type": "buttons", "items": [{"label": "View bibliographic record", "href": "https://books.google.com/books/about/Tea.html?id=VBzwtgAACAAJ", "variant": "secondary", "external": True}]},

        {"type": "heading", "level": 2, "text": "James A. Benn, Tea in China: A Religious and Cultural History"},
        {"type": "para", "text": "Benn examines tea in relation to Buddhism, ritual, medicine, material practice, and cultural history in China. It offers helpful depth for reading the exhibition’s Chan references without turning a later slogan into a timeless, single tradition."},
        {"type": "buttons", "items": [{"label": "View at University of Hawai‘i Press", "href": "https://uhpress.hawaii.edu/title/tea-in-china-a-religious-and-cultural-history/", "variant": "secondary", "external": True}]},

        {"type": "heading", "level": 2, "text": "陆羽《茶经》 — Lu Yu, Classic of Tea"},
        {"type": "para", "text": "Lu Yu’s Classic of Tea is a foundational Tang-dynasty text on tea materials, tools, preparation, and judgement. Read it as a work from a specific historical world, not as a timeless manual for every Chinese tea practice."},
        {"type": "buttons", "items": [{"label": "Read at Chinese Text Project", "href": "https://ctext.org/wiki.pl?if=gb&res=584531", "variant": "secondary", "external": True}]},

        {"type": "heading", "level": 2, "text": "陈宗懋、杨亚军主编《中国茶经》（修订版）"},
        {"type": "para", "text": "This large reference work brings together tea history, science, production, categories, culture, and contemporary industry in China. It is best used selectively as a reference rather than read as a single narrative from beginning to end."},
        {"type": "buttons", "items": [{"label": "View bibliographic record", "href": "https://book.douban.com/subject/7006696/", "variant": "secondary", "external": True}]},

        {"type": "heading", "level": 2, "text": "吴觉农《茶经述评》"},
        {"type": "para", "text": "Wu Juenong’s commentary places the Classic of Tea in dialogue with modern tea scholarship and production knowledge. It shows how a classic text can be re-read through later historical questions rather than simply repeated."},
        {"type": "buttons", "items": [{"label": "View bibliographic record", "href": "https://book.douban.com/subject/1648347/", "variant": "secondary", "external": True}]},

        {"type": "note", "style": "notice", "text": "Each title links to its publisher or an authoritative bibliographic record, not a retailer."},
    ],
}
