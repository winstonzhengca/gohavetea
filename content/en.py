# -*- coding: utf-8 -*-
"""English page content for Go Have Tea, transcribed from the 2026 Edmonton
Heritage Festival website content package (Part I)."""

PAGES = {}

# --------------------------------------------------------------------- home
PAGES["home"] = {
    "title": "Go Have Tea | Tea Travels in Edmonton",
    "meta": "Explore the tea exhibition created for the 2026 Edmonton Heritage Festival: Chinese tea-making, Edmonton goji stories, bubble tea, calligraphy, painting, and everyday practices of care.",
    "blocks": [
        {"type": "hero", "eyebrow": "GO HAVE TEA", "title": "Tea Travels: Leaves, Care, and Everyday Invention",
         "subtitle": "A three-table exhibition for the 2026 Edmonton Heritage Festival",
         "lead": "What travels when tea travels? Follow three paths: one leaf becoming many teas; pearl milk tea developing in Taiwan and moving through the world; and goji plants taking root in Edmonton. Along the way, meet the skills, memories, labour, landscapes, and relationships gathered around a cup.",
         "buttons": [
             {"label": "Start with Chinese Tea", "href": "/en/tables/chinese-tea/"},
             {"label": "Follow the Goji Story", "href": "/en/tables/wellness-goji/", "variant": "secondary"},
             {"label": "Build a Bubble Tea", "href": "/en/tables/bubble-tea/", "variant": "secondary"},
             {"label": "Enter the Poster Gallery", "href": "/en/posters/", "variant": "secondary"},
         ]},
        {"type": "image", "tone": "green",
         "caption": "Hero image: calligraphy and landscape detail",
         "alt": "Black-brush calligraphy reading 吃茶去, ‘Go Have Tea,’ beside a detail from Hui Yang’s mountain landscape, used as the visual invitation to an Edmonton tea exhibition.",
         "pending": True},
        {"type": "heading", "level": 2, "text": "A 30-second welcome"},
        {"type": "para", "text": "Tea is never only a drink. Leaves become different teas through skilled hands. Plants move with people and take root in new cities. Milk tea turns taste into a language of choice and customization. This exhibition follows tea as craft, care, work, memory, and everyday invention."},
        {"type": "para", "text": "Choose any table. Look closely. Make something. Then ask: what travels when tea travels?"},
        {"type": "heading", "level": 2, "text": "Why “Go Have Tea”?"},
        {"type": "para", "text": "“Go have tea” sounds ordinary, and that is its strength. Associated with later Chan encounter literature and the master Zhaozhou, the phrase 吃茶去 is often read as a return to the present moment. In this exhibition it also becomes a public invitation: slow down before judging, sit together before explaining, and make room for conversation across difference."},
        {"type": "para", "text": "Tea is not offered as a cure for conflict or as a decorative symbol of “Chinese culture.” It is a modest practice of attention. A shared cup does not erase difference; it can create time to meet difference without turning it immediately into stereotype."},
        {"type": "buttons", "items": [{"label": "Read the curator’s interpretation", "href": "/en/posters/go-have-tea/"}]},
        {"type": "heading", "level": 2, "text": "Three ways tea travels"},
        {"type": "columns", "items": [
            {"title": "One Leaf, Many Teas", "href": "/en/tables/chinese-tea/",
             "text": "See how one plant becomes many teas through local knowledge, tools, timing, and sensory judgment."},
            {"title": "Wellness & Goji Stories", "href": "/en/tables/wellness-goji/",
             "text": "Follow goji through Edmonton’s river valley, family gardens, community memory, and artist-researcher Yong Fei Guan’s Edmonton Goji Map."},
            {"title": "Build a Bubble Tea", "href": "/en/tables/bubble-tea/",
             "text": "Explore a drink that developed in Taiwan in the 1980s and became a global system of taste, customization, franchising, and service work."},
        ]},
        {"type": "heading", "level": 2, "text": "Art in the exhibition"},
        {"type": "para", "text": "Calligraphy by Ying (Joy) Wen and paintings by Hui Yang do not simply decorate the tables. They help the exhibition think. 吃茶去 turns an idea into an everyday action. 和而不同 — harmony without sameness — gives the project an ethical direction. Yang’s landscapes and studies of teaware connect movement, dwelling, objects, and memory."},
        {"type": "buttons", "items": [
            {"label": "Meet the artists", "href": "/en/artists/"},
            {"label": "View the poster gallery", "href": "/en/posters/", "variant": "secondary"},
        ]},
        {"type": "image", "tone": "tan", "pending": True,
         "caption": "Objects from the physical exhibition tables, photographed in Edmonton",
         "alt": "Three photographed objects from the Chinese Tea, Wellness & Goji, and Bubble Tea tables."},
        {"type": "heading", "level": 2, "text": "Before you leave"},
        {"type": "para", "text": "Take one question with you:"},
        {"type": "quote", "text": "Which plant, drink, object, or smell makes you think of home?"},
    ],
}

# -------------------------------------------------------------------- about
PAGES["about"] = {
    "title": "About the Exhibition | Go Have Tea",
    "meta": "Why this Edmonton Heritage Festival exhibition brings together Chinese tea, goji, bubble tea, calligraphy, painting, migration, labour, and everyday care.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "About the Exhibition"},
        {"type": "para", "text": "This exhibition was created for the Edmonton Heritage Festival as a small, mobile work of public anthropology. It begins with familiar things—tea leaves, cups, goji berries, milk tea menus, stickers, paintings, and calligraphy—and asks what larger histories they carry."},
        {"type": "para", "text": "The exhibition does not claim to summarize Chinese tea culture. Instead, it follows three concrete routes. The first asks how skilled makers transform one plant into many teas. The second follows plants and practices of care, with Edmonton goji at its centre. The third traces pearl milk tea from 1980s Taiwan into diaspora life, global franchising, social media, and local youth culture."},
        {"type": "para", "text": "Together the tables show that culture is not a sealed inheritance. It is made and remade through movement, labour, adaptation, disagreement, and ordinary acts of sharing."},
        {"type": "heading", "level": 2, "text": "Why Edmonton?"},
        {"type": "para", "text": "Edmonton is not simply the location where an imported story is displayed. It is part of the story. Goji shrubs have grown in the city’s river valley and family gardens for generations. Tea shops and bubble tea counters translate tastes across languages and neighbourhoods. Long winters, bright summers, migration, study, work, and family life all change when, where, and how people make a cup."},
        {"type": "para", "text": "The exhibition therefore treats Edmonton as a place where Chinese and East Asian tea practices are not merely preserved but actively remade."},
        {"type": "heading", "level": 2, "text": "Public anthropology at a festival"},
        {"type": "para", "text": "Public anthropology asks how research can become a form of conversation rather than a one-way explanation. At a festival, visitors may stay for ten seconds or ten minutes. The exhibition is built for both. A short title opens a question; an object or activity holds attention; a QR-linked page lets visitors continue later."},
        {"type": "para", "text": "The aim is not to test visitors on correct facts. It is to help them notice relationships: between leaf and labour, plant and migration, menu and service work, artwork and memory, difference and hospitality."},
        {"type": "heading", "level": 2, "text": "One exhibition, three entry points"},
        {"type": "para", "text": "Visitors can begin anywhere:"},
        {"type": "list", "items": [
            "Transform: How can one plant become many teas?",
            "Take root: How do plants become part of a new city and its memories?",
            "Remix: How did a Taiwanese drink become a global language of choice?",
        ]},
        {"type": "para", "text": "Every path returns to the same question: what travels when tea travels?"},
        {"type": "heading", "level": 2, "text": "On words, evidence, and care"},
        {"type": "para", "text": "The exhibition separates legends, commercial claims, community knowledge, research findings, and curatorial interpretation. It names Taiwan clearly in the history of pearl milk tea. It does not describe one practice as the only “authentic” tea. It does not turn wellness into a promise of cure. It credits community projects and artists beside the material they created."},
        {"type": "heading", "level": 2, "text": "Visitor information"},
        {"type": "note", "style": "pending", "label": "Pending organizer confirmation",
         "text": "2026 Edmonton Heritage Festival. Location: pavilion and site to be confirmed. Dates and hours: to be confirmed with the organizer before publication. Access: current festival accessibility and transportation link to be inserted."},
        {"type": "para", "text": "Language: English website with a clearly visible 中文 switch."},
        {"type": "para", "text": "Food and drink: display and educational activities only, unless the exact service has written festival and health approval."},
        {"type": "image", "tone": "green", "pending": True,
         "caption": "All three installed exhibition tables", "alt": "Wide photograph of the three installed exhibition tables at the festival pavilion."},
        {"type": "image", "tone": "paper", "pending": True,
         "caption": "Diagram of the three entry points",
         "alt": "Simple top-down diagram showing the three entry points: Transform, Take root, Remix."},
    ],
}

# ------------------------------------------------------------- tables (all)
PAGES["tables"] = {
    "title": "Three Exhibition Tables | Go Have Tea",
    "meta": "The Go Have Tea exhibition is arranged as three tables — Chinese Tea, Wellness & Goji, and Bubble Tea — that tell one connected story.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Three Tables"},
        {"type": "para", "text": "The exhibition is arranged as three tables, but it tells one connected story. Each table begins with an action—transform, take root, or remix—and shows tea culture being made in practice."},
        {"type": "para", "text": "There is no required order. Begin with the leaf, the plant, or the cup that interests you."},
        {"type": "columns", "items": [
            {"title": "Chinese Tea — Transform", "href": "/en/tables/chinese-tea/", "text": "One plant, many processes, many traditions."},
            {"title": "Wellness & Goji — Take root", "href": "/en/tables/wellness-goji/", "text": "Plants, family knowledge, migration, and care in Edmonton."},
            {"title": "Bubble Tea — Remix", "href": "/en/tables/bubble-tea/", "text": "Taiwanese invention, global movement, customization, and labour."},
        ]},
    ],
}

# ------------------------------------------------------------ table pages
PAGES["table-chinese-tea"] = {
    "title": "One Leaf, Many Teas | Go Have Tea",
    "meta": "Green, white, yellow, oolong, black, and dark teas can all begin with Camellia sinensis — see how skilled makers transform one plant into many traditions.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Chinese Tea: One Leaf, Many Teas"},
        {"type": "note", "style": "notice", "label": "QR label", "text": "LOOK AT THE LEAF"},
        {"type": "heading", "level": 2, "text": "30-second view"},
        {"type": "para", "text": "Green, white, yellow, oolong, black, and dark teas can all begin with Camellia sinensis. Their differences are not simply “inside the leaf.” Makers create them through sequences of withering, heating, rolling, oxidation, microbial transformation, roasting, and drying."},
        {"type": "para", "text": "The point is not to memorize six boxes. It is to see tradition as living knowledge."},
        {"type": "heading", "level": 2, "text": "What you are seeing on the table"},
        {"type": "para", "text": "The jars, leaves, cups, and process cards make one idea visible: a tea is produced through relationships among plant variety, landscape, weather, tools, timing, sensory judgment, markets, and ways of serving."},
        {"type": "para", "text": "Look for differences in colour, shape, size, and aroma. Then ask what cannot be seen in the finished leaf: who made it, what decisions they took, what the weather was like, and what kind of drinker or market they imagined."},
        {"type": "heading", "level": 2, "text": "A five-minute story: skill is not a recipe"},
        {"type": "para", "text": "A process list can say “wither, roll, oxidize, dry,” but it cannot fully contain a maker’s knowledge. When is a leaf withered enough? How does it feel in the hand? What changes when the air is humid? When should heat be applied? Such decisions are learned through bodies, tools, environments, teachers, repetition, and comparison."},
        {"type": "para", "text": "That is why this table avoids presenting one method as universal or one serving style as the only authentic Chinese tea. China contains many tea-producing regions, histories, classes of consumers, commercial systems, and everyday habits. Formal gongfu-style preparation is one important practice, but tea also appears in thermoses, large mugs, workplaces, restaurants, family kitchens, travel flasks, and gifts."},
        {"type": "para", "text": "The phrase “one leaf, many teas” therefore carries two meanings. One plant can be transformed in many ways, and one tradition can live in many social settings."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Physical evidence supports cautious claims about tea use more than two thousand years ago; it does not justify repeating every origin legend as archaeological fact. The exhibition therefore avoids the convenient slogan that tea possesses one continuous, unchanged five-thousand-year history."},
        {"type": "para", "text": "UNESCO’s description of traditional tea-processing techniques and associated social practices in China is useful because it links cultivation, picking, processing, drinking, and sharing. Yet heritage recognition should not freeze living knowledge. Techniques continue to change through research, machinery, markets, climate, tourism, branding, education, and the work of tea makers."},
        {"type": "heading", "level": 2, "text": "Hospitality and the everyday"},
        {"type": "para", "text": "A cup can welcome a guest, mark a pause in work, support study, carry a gift relationship, or become a performance of expertise. Hospitality is never automatic: someone buys the tea, heats the water, cleans the vessels, learns the sequence, serves, explains, and notices other people’s comfort."},
        {"type": "para", "text": "This labour is part of tea culture. The table asks visitors to see not only beautiful objects but also the work that makes a shared cup possible."},
        {"type": "heading", "level": 2, "text": "Look closely"},
        {"type": "triad", "items": [
            {"label": "LOOK", "text": "Find one visible change in the leaf."},
            {"label": "ASK", "text": "Which part of the process depends on skilled judgment?"},
            {"label": "REMEMBER", "text": "Tradition is not a frozen recipe. It lives through people, places, and repeated practice."},
        ]},
        {"type": "keywords", "items": ["Camellia sinensis", "craft", "withering", "heat-fixing", "oxidation", "microbial transformation", "drying", "gongfu tea", "hospitality", "living tradition"]},
        {"type": "image", "tone": "green", "pending": True, "caption": "Six approved leaf samples on the exhibition tray",
         "alt": "Six small containers hold teas with different colours and leaf shapes, showing how one tea plant can be transformed through different local processes."},
        {"type": "image", "tone": "tan", "pending": True, "caption": "Original process diagram (not a generic tea-factory infographic)",
         "alt": "Original diagram showing withering, heat-fixing, rolling, oxidation, and drying as connected decisions rather than a fixed assembly line."},
        {"type": "image", "tone": "gold", "pending": True, "caption": "Hui Yang’s teaware studies, or a photograph of the Edmonton exhibition table",
         "alt": "Painted studies of teaware, or a photograph of the physical Chinese Tea table in Edmonton."},
        {"type": "note", "style": "notice", "label": "Optional audio", "text": "A 45-second recording of a maker or curator describing one sensory decision, with a full transcript, may appear here."},
    ],
}

PAGES["table-wellness-goji"] = {
    "title": "Wellness and Goji Stories | Go Have Tea",
    "meta": "Goji shrubs have grown in Edmonton’s river valley and family gardens since Chinese migrants arrived in the 1890s — a story of migration, family knowledge, and everyday care.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Wellness & Goji Stories"},
        {"type": "note", "style": "notice", "label": "QR label", "text": "FOLLOW THE GOJI"},
        {"type": "heading", "level": 2, "text": "30-second view"},
        {"type": "para", "text": "Plants travel with people. Goji shrubs have grown in Edmonton since Chinese migrants arrived in the 1890s. Today they can be found in the river valley and in family gardens."},
        {"type": "para", "text": "Here, wellness is not a promise of cure. It is a story about migration, family knowledge, adaptation, trade, hospitality, and everyday care."},
        {"type": "heading", "level": 2, "text": "What you are seeing on the table"},
        {"type": "para", "text": "The goji branch, dried berries, map, floral infusions, and community practice cards connect local plants with memories and routes. Some cups contain true tea from Camellia sinensis. Others are more precisely called herbal infusions or tisanes. Everyday Chinese speech may still call both kinds “tea.”"},
        {"type": "para", "text": "This difference in naming is not a correction of community language. It helps visitors notice how botanical, commercial, medical, and everyday categories overlap without being identical."},
        {"type": "heading", "level": 2, "text": "Edmonton goji"},
        {"type": "para", "text": "Artist-researcher Yong Fei Guan’s Living History of Gojis in Edmonton and Edmonton Goji Map bring together plant life, Chinese Canadian history, family gardens, neighbourhood knowledge, and public art. The project asks us to see goji not merely as a packaged “superfood,” but as a companion of migration."},
        {"type": "para", "text": "In Edmonton, goji can be a river-valley shrub, a backyard plant, an ingredient in soup or an infusion, a gift between neighbours, a memory of an older family member, or a subject of contemporary art. One plant connects many scales of life."},
        {"type": "buttons", "items": [{"label": "Open the Edmonton Goji Map", "href": "https://edmonton-goji.github.io/Map/", "external": True}]},
        {"type": "heading", "level": 2, "text": "A five-minute story: plants take root twice"},
        {"type": "para", "text": "A plant takes root in soil, but it can also take root in memory. Migrants carry seeds, tastes, names, techniques, and expectations. A new climate changes what survives and how it is used. Neighbours exchange cuttings. Children may recognize a packaged berry before they recognize the shrub. A health-food label may describe the same plant differently from a grandparent or gardener."},
        {"type": "para", "text": "The Edmonton goji story makes migration visible without reducing it to a simple story of cultural preservation. Plants adapt. People adapt. Meanings change. The plant becomes local without losing its longer routes."},
        {"type": "heading", "level": 2, "text": "Other routes of care"},
        {"type": "para", "text": "The table also introduces floral and herbal infusions and Canadian-grown American ginseng as secondary cross-Pacific stories. These materials show that movement does not go in only one direction. Plants, products, knowledge, and value travel between North America and Asia through trade, families, professional practice, and popular wellness culture."},
        {"type": "para", "text": "The exhibition does not rank family knowledge against professional knowledge or modern science. It asks how different forms of authority meet in an everyday cup—and where responsible limits are needed."},
        {"type": "heading", "level": 2, "text": "Osmanthus: a small flower, a long fragrance"},
        {"type": "para", "text": "Dried osmanthus may be infused alone or paired with green, oolong, or black tea. Without tea leaves, it is more precisely a floral infusion, though it is commonly called guihua cha in Chinese."},
        {"type": "quote", "text": "桂子月中落，天香云外飘。", "attribution": "Traditionally attributed to Song Zhiwen, “Lingyin Temple” (Tang dynasty)"},
        {"type": "para", "text": "The poster’s couplet imagines fragrance moving among moonlight, a mountain temple, and clouds. In Edmonton, the question becomes personal: where does this fragrance take you?"},
        {"type": "note", "style": "notice", "label": "Educational notice", "text": "This page shares cultural histories and community practices. It does not provide medical advice or recommend treatment. Herbs and foods can cause allergies or interact with medicines. For individual health questions, consult a qualified healthcare professional."},
        {"type": "heading", "level": 2, "text": "Look closely"},
        {"type": "triad", "items": [
            {"label": "TRACE", "text": "Follow goji into Edmonton."},
            {"label": "ASK", "text": "Which plant makes you think of home?"},
            {"label": "REMEMBER", "text": "Care is a practice and a relationship, not a universal cure claim."},
        ]},
        {"type": "keywords", "items": ["goji", "migration", "take root", "home", "care", "herbal infusion", "tisane", "osmanthus", "American ginseng", "community knowledge"]},
        {"type": "image", "tone": "green", "pending": True, "caption": "Edmonton goji photograph, or the physical exhibition table",
         "alt": "A goji branch and dried red berries sit beside an Edmonton map and community story cards, linking a plant to migration, gardens, memory, and care."},
        {"type": "note", "style": "pending", "label": "Community images and garden addresses", "text": "Publish only with documented permission; private home locations are never exposed."},
    ],
}

PAGES["table-bubble-tea"] = {
    "title": "Build a Bubble Tea | Go Have Tea",
    "meta": "Pearl milk tea developed in Taiwan in the 1980s and travelled fast — build a cup, then look behind it at customization, franchising, and service labour.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Bubble Tea: Build a Cup"},
        {"type": "note", "style": "notice", "label": "QR label", "text": "BUILD A CUP"},
        {"type": "heading", "level": 2, "text": "30-second view"},
        {"type": "para", "text": "Pearl milk tea developed in Taiwan in the 1980s, although two teahouses claim its invention. It travelled quickly because tea, milk, sweetness, ice, and toppings could be separated, recombined, and customized."},
        {"type": "para", "text": "Build a cup, then look behind it."},
        {"type": "heading", "level": 2, "text": "What you are seeing on the table"},
        {"type": "para", "text": "The cup template and stickers turn a menu into a small design system. Visitors choose a base, milk, sweetness, ice, toppings, and mood. There is no single correct cup."},
        {"type": "para", "text": "The activity is playful, but it also reveals how choice is organized. A modern milk tea menu makes hundreds of possible combinations feel clear and repeatable."},
        {"type": "heading", "level": 2, "text": "Build a cup"},
        {"type": "bubble_builder"},
        {"type": "heading", "level": 2, "text": "A five-minute story: invention and disagreement"},
        {"type": "para", "text": "It is safest to say that pearl milk tea developed in Taiwan in the 1980s. Hanlin Tea Room and Chun Shui Tang both tell origin stories, and the exact claim remains contested. The exhibition does not resolve the dispute in favour of one company."},
        {"type": "para", "text": "This uncertainty is part of the history. Invention is often narrated after a product becomes valuable. Brand stories, court disputes, public memory, and national cultural promotion all help turn a drink into an icon."},
        {"type": "heading", "level": 2, "text": "Why bubble tea travels so well"},
        {"type": "para", "text": "Bubble tea can be shaken, photographed, branded, franchised, and adjusted to local tastes. Its modular form allows shops to change tea bases, milk options, sugar levels, toppings, seasonal flavours, cup graphics, and ordering technologies while keeping the drink recognizable."},
        {"type": "para", "text": "The same modularity connects “slow” and “quick” tea worlds. Early Taiwanese tea shops offered places to sit, eat, talk, and spend time. Later small-format counters and chains increased speed, portability, and repetition. Neither form is simply more authentic. Each organizes time, space, labour, and social life differently."},
        {"type": "heading", "level": 2, "text": "Behind the cup"},
        {"type": "para", "text": "Customization depends on standardization. Someone develops recipes, sources tea and toppings, manages cold storage, prints cups, trains workers, maintains machines, handles digital orders, and performs friendly service under time pressure."},
        {"type": "para", "text": "The bright menu and cheerful cup can hide this labour. The exhibition asks visitors to enjoy choice while also noticing the systems that make choice possible."},
        {"type": "heading", "level": 2, "text": "Bubble tea in Edmonton"},
        {"type": "para", "text": "In Edmonton, bubble tea is connected with migration, student life, shopping centres, Chinatown and suburban commercial areas, family entrepreneurship, global chains, independent shops, and social media. The map does not rank stores. It uses public, permission-appropriate stories to ask how a Taiwanese drink becomes local in different neighbourhoods."},
        {"type": "heading", "level": 2, "text": "Make and reflect"},
        {"type": "triad", "items": [
            {"label": "MAKE", "text": "Build a cup with stickers."},
            {"label": "ASK", "text": "Which choice feels most like you, and why?"},
            {"label": "LOOK BEHIND THE CUP", "text": "What labour, ingredients, transport, and technology made your choices possible?"},
        ]},
        {"type": "keywords", "items": ["pearl milk tea", "Taiwan", "shaken tea", "customization", "modular menu", "franchising", "supply chain", "service labour", "diaspora", "social media"]},
        {"type": "image", "tone": "tan", "pending": True, "caption": "Completed visitor cup cards, photographed without names or faces",
         "alt": "A paper bubble-tea cup is covered with stickers for tea base, sweetness, ice, toppings, and mood, turning menu choices into an activity about mobility and labour."},
        {"type": "image", "tone": "gold", "pending": True, "caption": "History timeline: 1980s Taiwan; diaspora shops; franchising; platform ordering and social media — with “adaptation” nodes rather than a one-way diffusion arrow",
         "alt": "Restrained timeline of bubble tea's spread, shown as adaptation nodes rather than a single diffusion arrow."},
        {"type": "image", "tone": "green", "pending": True, "caption": "Tools, sealing film, cup labels, menu modules, and cleaned work surfaces",
         "alt": "Close photographs of bubble tea shop tools and surfaces; worker photography requires separate permission."},
    ],
}

# ------------------------------------------------------------------ posters
PAGES["posters"] = {
    "title": "Poster Gallery | Go Have Tea",
    "meta": "Calligraphy, painting, poetry, objects, and Edmonton landscapes carry the exhibition’s central questions across thirteen posters.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Poster Gallery"},
        {"type": "para", "text": "These posters are part of the exhibition, not advertisements added after it. They carry its central questions through calligraphy, painting, poetry, objects, and Edmonton landscapes."},
        {"type": "para", "text": "The gallery brings together three related groups:"},
        {"type": "list", "items": [
            "Go Have Tea: Words for Attention — curatorial phrases, classical lines, Chan and Daoist resonances.",
            "Tea in Many Tongues: Edmonton as a Shared Table — words, routes, neighbourhoods, and coexistence without sameness.",
            "Plants Travel: Osmanthus and Goji — fragrance, plant movement, memory, and the boundary between tea and infusion.",
        ]},
        {"type": "para", "text": "Each poster page provides a high-resolution image, a full text transcript, historical context, artwork information, the curator’s interpretation, alt text, and an approved download where rights allow."},
        {"type": "note", "style": "pending", "label": "Gallery publication note", "text": "The online gallery includes only approved final posters and clearly identified final variants. Drafts containing incomplete calligraphy, incorrect citations, non-approved decorative elements, or artwork not made by the credited artists stay in the internal design archive."},
        {"type": "gallery_grid", "items": [
            {"title": "Beyond Tea", "href": "/en/posters/beyond-tea/", "sub": "There is more to tea than tea."},
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
    "meta": "Poster: Beyond Tea / 茶外有茶 — there is more to tea than tea.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Beyond Tea"},
        {"type": "poster_meta", "chinese": "茶外有茶", "translation": "There is more to tea than tea."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Created for this exhibition, 茶外有茶 looks beyond tea as a drink to how it is grown, made, circulated, and shared—and to the people, labour, and histories involved."},
        {"type": "quote", "text": "Most people turn to wine; who understands the fragrance tea can bring?", "attribution": "Jiaoran, “Drinking Tea with Lu Yu on the Ninth Day” (Tang dynasty)"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Jiaoran’s poem is associated with the Double Ninth Festival, when drinking wine was customary. The lines contrast that convention with the shared appreciation of tea. They do not declare tea morally superior in every setting; they describe recognition between people who understand a particular fragrance and practice."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "“Beyond Tea” names the method of the whole exhibition. A cup contains more than a beverage: plants, land, skill, labour, transport, branding, service, memory, and relationships. The phrase asks visitors to look through the object without looking past the people who made it."},
        {"type": "heading", "level": 2, "text": "Artwork note"},
        {"type": "para", "text": "Uses an approved work or detail by Hui Yang and approved calligraphy by Ying (Joy) Wen where present. The exact source image is credited beside the poster rather than one general credit for the entire gallery."},
        {"type": "image", "tone": "berry", "pending": True, "caption": "Beyond Tea poster",
         "alt": "Warm-toned poster combining the phrase Beyond Tea, Chinese calligraphy, a painted landscape or floral detail, and a text panel explaining the people, labour, and histories gathered around tea."},
    ],
}

PAGES["poster-pause-sip-be-here"] = {
    "title": "Pause. Sip. Be Here. | Poster | Go Have Tea",
    "meta": "Poster: Pause. Sip. Be Here. / 禅茶一味 — Chan and tea share one taste.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Pause. Sip. Be Here."},
        {"type": "poster_meta", "chinese": "禅茶一味", "translation": "Chan and tea share one taste."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Slow down. Let one cup change your pace."},
        {"type": "para", "text": "禅茶一味 is a widely used expression in tea culture. It links tea with the attentiveness of Chan practice. “One taste” does not mean that tea and Buddhism are identical. It suggests that an everyday act—making and sharing tea—can become a practice of presence."},
        {"type": "quote", "text": "Spring is gathered in the mountains; fragrant tea is best brewed among bamboo.",
         "attribution": "春共山中採，香宜竹裡煎 — anonymous tea-shop couplet, date unknown; appears at least as early as the 1928 Shanghai edition of Fenlei Zhonghua Yinglian Daquan."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The exhibition treats 禅茶一味 as a later cultural formulation rather than a single ancient doctrine. Tea and Buddhist institutions have long histories of contact, but a modern slogan should not be projected unchanged into every earlier period."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The poster offers a pause inside the festival’s rush. Presence is not withdrawal from the world. It is a way to notice the cup, the people around it, and the conditions of an encounter."},
        {"type": "image", "tone": "paper", "pending": True, "caption": "Pause. Sip. Be Here. poster",
         "alt": "A calm poster with white flowers, a tea cup, Chinese calligraphy, and the title Pause. Sip. Be Here, linking everyday tea with attentive presence."},
    ],
}

PAGES["poster-go-have-tea"] = {
    "title": "Go Have Tea | Poster | Go Have Tea",
    "meta": "Poster: Go Have Tea / 吃茶去 — associated with Chan master Zhaozhou, an invitation to return to the present moment.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Go Have Tea"},
        {"type": "poster_meta", "chinese": "吃茶去", "translation": "Go have some tea."},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Preserved in later Chan encounter literature and associated with Chan master Zhaozhou Congshen (778–897), this everyday invitation is often read as a call to return to the present moment."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The phrase reaches us through later recorded encounter literature. The website says “associated with” Zhaozhou rather than presenting the poster’s wording as a securely transcribed statement from the moment itself."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "In this exhibition, 吃茶去 is neither an escape from difficult conversation nor a mystical answer. It is an invitation to slow classification down. Before explaining ourselves, we sit. Before reducing another person to a category, we share time. Tea does not erase difference; it can help create the conditions in which difference is met with attention."},
        {"type": "heading", "level": 2, "text": "Artwork information"},
        {"type": "para", "text": "Ying Wen, 吃茶去 / Go Have Tea, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton."},
        {"type": "note", "style": "pending", "label": "Production check", "text": "Confirm final date and display credit against the artist’s approved label before launch."},
        {"type": "image", "tone": "green", "pending": True, "caption": "Go Have Tea poster",
         "alt": "Vertical black calligraphy reading 吃茶去 beside a mountainous painting, with an English text panel explaining ‘Go Have Tea’ as an invitation to pause and return to everyday practice."},
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
        {"type": "para", "text": "Ying Wen, 和而不同 / Harmony Without Sameness, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton."},
        {"type": "note", "style": "pending", "label": "Production check", "text": "Confirm final date against the approved artist label."},
        {"type": "image", "tone": "tan", "pending": True, "caption": "Harmony, Not Sameness poster",
         "alt": "A framed vertical calligraphy work reading 和而不同 appears beside a small framed painting, with the words Harmony, Not Sameness and an Edmonton map-like background."},
    ],
}

PAGES["poster-a-cup-for-the-city"] = {
    "title": "A Cup for the City | Poster | Go Have Tea",
    "meta": "Poster: A Cup for the City — from Bai Juyi’s wish to send tea to someone who loves it, to Edmonton’s neighbourhoods and newcomers.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "A Cup for the City"},
        {"type": "quote", "text": "If only I could send this bowl to someone who loves tea.", "attribution": "無由持一磑，寄與愛茶人 — Bai Juyi, “Brewing Tea at a Mountain Spring” (Tang dynasty)"},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "The line is from Bai Juyi’s Tang-dynasty poem “Brewing Tea at a Mountain Spring.” The poem begins with the physical acts of drawing water and watching tea brew, then turns an absent companion into the imagined recipient of a bowl."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "A cup can be small and still make room for a city. The poster connects an old wish to send tea with Edmonton’s distances, neighbourhoods, newcomers, and relationships. Hospitality is not only receiving someone already present; it can also be an act of remembering someone elsewhere."},
        {"type": "heading", "level": 2, "text": "Artwork note"},
        {"type": "para", "text": "Uses Hui Yang’s approved mountain landscape as the central image; the features needed to recognize the original work are not cropped away."},
        {"type": "image", "tone": "gold", "pending": True, "caption": "A Cup for the City poster",
         "alt": "A vertical mountain painting appears beside Bai Juyi’s line about sending a bowl to someone who loves tea, over a soft Edmonton river-valley collage."},
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
        {"type": "note", "style": "correction", "label": "Production correction", "text": "Some draft artwork mislabels the chapter. The public website and final download must use Daodejing chapter 22."},
        {"type": "image", "tone": "paper", "pending": True, "caption": "Slow Down, Edmonton poster",
         "alt": "White flowers in a rectangular glass vase sit against a pale winter Edmonton landscape under the title Slow Down, Edmonton and a line from the Daodejing."},
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
        {"type": "image", "tone": "green", "pending": True, "caption": "Be Still. Be Here. poster",
         "alt": "A quiet floral still life is paired with the title Be Still. Be Here and a line from chapter 16 of the Daodejing."},
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
        {"type": "image", "tone": "tan", "pending": True, "caption": "Many Names. One Edmonton. poster",
         "alt": "A vase of white flowers stands over a layered Edmonton river scene, surrounded by selected words for tea in several scripts."},
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
        {"type": "image", "tone": "gold", "pending": True, "caption": "Tea Travels Here poster",
         "alt": "Eight illustrated tea vessels are set over a colourful Edmonton map, surrounded by words for tea in several languages."},
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
        {"type": "image", "tone": "paper", "pending": True, "caption": "A World of Tea postcard",
         "alt": "A horizontal pale-green postcard shows eight illustrated tea vessels surrounded by selected words for tea in multiple scripts."},
    ],
}

PAGES["poster-many-words-for-tea"] = {
    "title": "Many Words for Tea | Poster | Go Have Tea",
    "meta": "Poster: Many Words for Tea / 一叶多声 — Joy Wen’s Harmony Without Sameness calligraphy at the centre of tea words from ten languages.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Many Words for Tea"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Different names. Different routes. Many ways of sharing tea."},
        {"type": "para", "text": "One leaf · many languages · open encounters."},
        {"type": "heading", "level": 2, "text": "Historical background"},
        {"type": "para", "text": "Tea words can suggest histories of maritime and overland exchange, but language does not prove a single route by itself. The poster therefore uses dotted paths as an invitation to inquire, not as a definitive trade map."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "Joy’s 和而不同 calligraphy sits at the centre. The many names around it do not become one word, just as Edmonton’s communities do not need to become one culture. The shared table is meaningful because difference remains visible."},
        {"type": "image", "tone": "berry", "pending": True, "caption": "Many Words for Tea poster",
         "alt": "A colourful layered-paper poster places 和而不同 calligraphy in the centre, surrounded by selected words for tea in Chinese, English, Korean, Arabic, French, Japanese, Swahili, Hindi, Turkish, and Russian, with four painted tea vessels below."},
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
        {"type": "image", "tone": "green", "pending": True, "caption": "The five-poster Edmonton Community Tea series",
         "alt": "Five coordinated vertical posters combine Edmonton maps and river-valley scenes with tea vessels, calligraphy, flowers, and mountain painting."},
    ],
}

PAGES["poster-osmanthus-infusion"] = {
    "title": "Osmanthus Infusion | Poster | Go Have Tea",
    "meta": "Poster: Osmanthus Infusion — a small flower, a lingering fragrance, and the boundary between tea and floral infusion.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Osmanthus Infusion"},
        {"type": "para", "text": "A small flower, a lingering fragrance."},
        {"type": "quote", "text": "Osmanthus falls from the moon; its heavenly fragrance drifts beyond the clouds.",
         "attribution": "桂子月中落，天香云外飘 — Tang dynasty; traditionally attributed to Song Zhiwen, “Lingyin Temple”"},
        {"type": "heading", "level": 2, "text": "Poster transcript"},
        {"type": "para", "text": "Dried osmanthus can be infused on its own or paired with green, oolong, or black tea. Without tea leaves, it is more precisely a floral infusion—a tisane—though everyday Chinese still commonly calls it guihua cha."},
        {"type": "heading", "level": 2, "text": "Curator’s interpretation"},
        {"type": "para", "text": "The poster begins with a small material and opens into landscape, memory, and naming. Smell can cross time quickly. The visitor prompt—“Where does this fragrance take you?”—invites a personal response without turning it into a medical claim."},
        {"type": "note", "style": "notice", "label": "Educational notice", "text": "For cultural learning and discussion; not medical advice."},
        {"type": "image", "tone": "gold", "pending": True, "caption": "Osmanthus Infusion poster",
         "alt": "A pale poster shows dried golden osmanthus in a glass jar and a cream cup, with a painted river landscape and a classical couplet about fragrance."},
    ],
}

# ------------------------------------------------------------------ artists
PAGES["artists"] = {
    "title": "Artists | Go Have Tea",
    "meta": "The paintings of Hui Yang and the calligraphy of Ying (Joy) Wen shape how the exhibition can be read.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Artists"},
        {"type": "para", "text": "The exhibition was developed through a conversation among research, painting, calligraphy, graphic composition, and public interpretation. The artworks are not generic signs of “Chinese tradition.” Each one changes how the exhibition can be read."},
        {"type": "para", "text": "Hui Yang’s paintings bring mountains, vessels, flowers, animals, and material attention into the project. Ying (Joy) Wen’s calligraphy gives visual weight to short phrases that organize the exhibition’s ethics and rhythm."},
        {"type": "heading", "level": 2, "text": "Credit principle"},
        {"type": "para", "text": "Every artwork is credited beside the image in which it appears. Cropped details still name the artist and original work. Graphic backgrounds, generated elements, and design composition are never credited as original artwork by Yang or Wen."},
        {"type": "gallery_grid", "items": [
            {"title": "Hui Yang", "href": "/en/artists/hui-yang/", "sub": "Painter"},
            {"title": "Ying (Joy) Wen", "href": "/en/artists/ying-joy-wen/", "sub": "Calligrapher"},
        ]},
    ],
}

PAGES["artist-hui-yang"] = {
    "title": "Hui Yang | Artist | Go Have Tea",
    "meta": "Painter Hui Yang brings mountains, vessels, flowers, and material attention into the Go Have Tea exhibition.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Hui Yang"},
        {"type": "para", "text": "Hui Yang is the painter whose works provide many of the exhibition’s visual anchors. Her mountain landscape, teaware studies, floral still lifes, and other approved paintings bring attention to material form, movement, and dwelling."},
        {"type": "para", "text": "In After Wang Meng’s Ge Zhichuan Moving His Dwelling, a classical composition is re-situated through a work made in Edmonton. The image of a family moving through mountains can be read not simply as retreat, but as reorientation: a search for rhythm, shelter, dignity, and renewed relation in a changing environment."},
        {"type": "para", "text": "Within this exhibition, Yang’s work helps connect landscape with migration without claiming that one image can represent all immigrant experience. Her paintings also slow the viewer down. A cup, branch, flower, or rock becomes worthy of sustained looking."},
        {"type": "heading", "level": 2, "text": "Featured work"},
        {"type": "quote", "text": "Hui Yang, After Wang Meng’s Ge Zhichuan Moving His Dwelling / 仿王蒙《葛稚川移居图》, 2022, acrylic on canvas, 24 × 60 in., Edmonton."},
        {"type": "image", "tone": "green", "pending": True, "caption": "Full, uncropped artwork",
         "alt": "A tall mountain landscape depicts travellers moving through layered rocks, trees, and paths, reworking a composition associated with the Yuan painter Wang Meng."},
        {"type": "image", "tone": "tan", "pending": True, "caption": "Detail: brushwork", "alt": "Close detail of brushwork from Hui Yang’s mountain landscape."},
        {"type": "image", "tone": "gold", "pending": True, "caption": "Detail: figures", "alt": "Close detail of travelling figures from Hui Yang’s mountain landscape."},
        {"type": "note", "style": "pending", "text": "An optional artist statement or audio recording will appear here only after Hui Yang approves the text and recording."},
    ],
}

PAGES["artist-ying-joy-wen"] = {
    "title": "Ying (Joy) Wen | Calligrapher | Go Have Tea",
    "meta": "Calligrapher Ying (Joy) Wen created the works 吃茶去 and 和而不同 that give the exhibition its central visual language.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Ying (Joy) Wen"},
        {"type": "para", "text": "Ying (Joy) Wen created the calligraphy that gives the exhibition its central visual language. Her works 吃茶去 and 和而不同 appear as original artworks and recur across selected posters and postcards."},
        {"type": "para", "text": "Calligraphy is not used here as decorative proof of cultural authenticity. The shape, pressure, spacing, and rhythm of the brush make short phrases feel bodily and present. 吃茶去 turns the exhibition’s central idea into an action. 和而不同 makes coexistence without assimilation visible as a vertical sequence of inked characters."},
        {"type": "para", "text": "The website reproduces the complete works whenever possible. Crops may be used for responsive layouts, but they do not remove characters or distort the spacing between them."},
        {"type": "heading", "level": 2, "text": "Featured works"},
        {"type": "list", "items": [
            "Ying Wen, 吃茶去 / Go Have Tea, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton.",
            "Ying Wen, 和而不同 / Harmony Without Sameness, calligraphy, 13 3/4 × 27 1/2 in., 2026, Edmonton.",
        ]},
        {"type": "note", "style": "pending", "label": "Production check", "text": "Confirm dates and preferred English name order with the artist before publication."},
        {"type": "image", "tone": "paper", "pending": True, "caption": "吃茶去, calligraphy by Ying (Joy) Wen",
         "alt": "Four large black-brush characters, 吃茶去, are written vertically on pale paper, with red seals near the lower edge."},
    ],
}

# ------------------------------------------------------------------ curator
PAGES["curator"] = {
    "title": "Junhong (Summer) Ma | Curator | Go Have Tea",
    "meta": "Curator Junhong (Summer) Ma, cultural anthropologist and postdoctoral researcher at Xiamen University, on why she created Go Have Tea.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Curator"},
        {"type": "heading", "level": 2, "text": "Short biography"},
        {"type": "para", "text": "Junhong (Summer) Ma is a cultural anthropologist and postdoctoral researcher at Xiamen University. Her research examines contemporary Chinese and East Asian tea culture, tea industries, cultural authority, service labour, branding, education, migration, and the movement of tea knowledge between Taiwan, mainland China, and Canada."},
        {"type": "image", "tone": "tan", "pending": True, "caption": "The curator installing or discussing the exhibition table",
         "alt": "The curator working at the exhibition table, or an approved portrait."},
        {"type": "heading", "level": 2, "text": "Curator’s statement"},
        {"type": "para", "text": "I created this exhibition because public conversations about Chinese tea often move in two unhelpful directions. Tea is either compressed into a timeless national tradition or reduced to a consumer choice. Both approaches miss the people and relationships that make tea possible."},
        {"type": "para", "text": "The three tables begin instead with movement. A leaf moves through skilled hands and becomes many teas. A plant moves with migrants and takes root in Edmonton. A drink developed in Taiwan moves through shops, franchises, digital menus, and young people’s social worlds."},
        {"type": "para", "text": "“Go Have Tea” became the central invitation because it is ordinary. It does not promise that a cup will solve disagreement. It asks whether we can create enough time and space for a different kind of encounter. The Daoist resonance lies in rhythm rather than doctrine: less coercion, less hurry to classify, more softness, listening, and room for relations to change."},
        {"type": "para", "text": "For me, this is what public anthropology can do at a festival. It can begin with something familiar, make hidden labour and history visible, and leave visitors with a question rather than a completed cultural definition."},
        {"type": "quote", "text": "Junhong (Summer) Ma", "attribution": "Curator and cultural anthropologist"},
        {"type": "buttons", "items": [
            {"label": "About the Exhibition", "href": "/en/about/"},
            {"label": "Sources & Credits", "href": "/en/sources-credits/", "variant": "secondary"},
        ]},
    ],
}

# ------------------------------------------------------------------- map
PAGES["edmonton-tea-map"] = {
    "title": "Edmonton Tea Map | Go Have Tea",
    "meta": "Tea in Edmonton lives in river-valley plants, family gardens, Chinatown histories, and shared tables — a restrained map layer, not a business directory.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Edmonton Tea Map"},
        {"type": "para", "text": "Tea in Edmonton lives in more than tea shops. It appears in river-valley plants, family gardens, Chinatown histories, community events, grocery shelves, bubble tea counters, restaurants, student routines, thermoses, art projects, and shared tables."},
        {"type": "para", "text": "This map is not a ranking or a complete business directory. It is an exhibition layer that connects places with stories represented in the three tables."},
        {"type": "heading", "level": 2, "text": "Map layers"},
        {"type": "list", "items": [
            "Plants and migration — begin with the Edmonton Goji Map and the public history of goji in the river valley and family gardens. Private residential locations are never republished without explicit permission.",
            "Chinese Canadian history — area-level historical context for Chinatown, Boyle Street, and McCauley, linking to reliable public history rather than inventing a single “first tea shop” narrative.",
            "Tea spaces — tea houses, shops, restaurants, community organizations, and temporary events, added only when an entry has a verifiable public address and a clear connection to an exhibition story.",
            "Bubble tea and youth culture — selected clusters or permission-based stories rather than an attempt to list every business.",
            "The exhibition — the Heritage Festival pavilion during the event, with dates and opening hours confirmed by the organizer.",
        ]},
        {"type": "heading", "level": 2, "text": "Public entries"},
        {"type": "map_list", "groups": [
            {"title": "Plants and migration", "entries": [
                {"name": "Edmonton Goji Map", "desc": "Project-wide link to Yong Fei Guan’s map and bilingual eBook."},
            ]},
            {"title": "Chinese Canadian history", "entries": [
                {"name": "Goji Berry Teahouse, Fort Edmonton Park", "desc": "Archive entry for the 2023 project and its reflection on Chinese history, local goji, and home."},
                {"name": "Edmonton Chinatown / Boyle Street–McCauley", "desc": "Historical context area; no invented business genealogy."},
            ]},
            {"title": "The exhibition", "entries": [
                {"name": "2026 Heritage Festival exhibition", "desc": "Temporary event marker, added once logistics are confirmed by the organizer."},
            ]},
        ]},
        {"type": "buttons", "items": [{"label": "Open the Edmonton Goji Map", "href": "https://edmonton-goji.github.io/Map/", "external": True}]},
        {"type": "heading", "level": 2, "text": "Where does tea live in your Edmonton?"},
        {"type": "note", "style": "pending", "text": "This first release deliberately keeps the map to a restrained list view: no colour-only categories, and no private home addresses or precise plant locations. Community-submitted stories, an expanded business directory, and any future audio stories will be added only after permissions, consent, transcripts, and a withdrawal process are in place."},
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
        {"type": "note", "style": "pending", "label": "go-have-tea-one-minute-guide-en.pdf", "text": "Downloadable PDF coming soon — full text is below."},
        {"type": "para", "text": "Tea travels as leaf, plant, drink, skill, memory, and work. At the Chinese Tea table, look for how one plant becomes many teas. At the Wellness table, follow goji into Edmonton’s river valley and family gardens. At the Bubble Tea table, build a cup and then ask what labour and systems made your choices possible. In the poster gallery, notice how calligraphy, paintings, poems, and city landscapes change one another. There is no single correct route. Begin with what catches your attention."},

        {"type": "heading", "level": 2, "text": "Tea Travels Passport"},
        {"type": "note", "style": "pending", "label": "tea-travels-passport-en.pdf", "text": "Downloadable PDF coming soon — full text is below."},
        {"type": "para", "text": "Front: BUILD YOUR TEA TRAVELS PASSPORT"},
        {"type": "list", "items": ["Discover a craft.", "Build a milk tea.", "Find Edmonton goji."]},
        {"type": "para", "text": "Collect or place one sticker at each stop. There is no single correct cup."},
        {"type": "para", "text": "Back: What travels when tea travels? skill · memory · plants · labour · care · something else: ______. Which plant, cup, smell, or word makes you think of home?"},

        {"type": "heading", "level": 2, "text": "Teacher Guide"},
        {"type": "note", "style": "pending", "label": "go-have-tea-teacher-guide-en.pdf", "text": "Downloadable PDF coming soon. Suggested level: Grades 4–12, adaptable. Length: 45–60 minutes."},
        {"type": "para", "text": "Learning goals:"},
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
        {"type": "note", "style": "pending", "label": "go-have-tea-family-guide-en.pdf", "text": "Downloadable PDF coming soon — full text is below."},
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
        {"type": "note", "style": "pending", "label": "go-have-tea-community-conversation-en.pdf", "text": "Downloadable PDF coming soon. Length: 45–75 minutes."},
        {"type": "para", "text": "Open with the phrase harmony without sameness. Invite each participant to name a drink or plant connected with care. Discuss what is gained and lost when a community practice becomes a product, festival display, health trend, or heritage symbol. Close by identifying one way to share a story without claiming to speak for everyone."},

        {"type": "heading", "level": 2, "text": "Accessible Text Pack"},
        {"type": "note", "style": "pending", "label": "go-have-tea-large-print-and-poster-transcripts-en.pdf", "text": "Downloadable PDF coming soon."},
        {"type": "para", "text": "Contents: all main table texts in at least 18-point type; full poster transcripts; image descriptions; glossary; short URLs; educational notice."},

        {"type": "note", "style": "notice", "label": "Resource rights note", "text": "Downloadable files may include only images, fonts, maps, and artworks licensed for redistribution. A page that may legally display an embedded image does not automatically have permission to package it in a downloadable PDF."},
    ],
}

# --------------------------------------------------------------- glossary
PAGES["glossary"] = {
    "title": "Glossary | Go Have Tea",
    "meta": "Key terms from the Go Have Tea exhibition, from Camellia sinensis to public anthropology.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Glossary"},
        {"type": "definition_list", "items": [
            {"term": "Camellia sinensis", "def": "The plant species from which green, white, yellow, oolong, black, and dark teas are made."},
            {"term": "Tea / cha / 茶", "def": "A plant, processed leaf, prepared drink, commodity, and social practice. Context matters."},
            {"term": "Herbal infusion / tisane", "def": "A drink made by steeping plants other than Camellia sinensis. Everyday speech may still call it “tea.”"},
            {"term": "Gongfu tea / 工夫茶", "def": "Tea preparation emphasizing skill, attention, repeated infusions, and particular regional and social histories. It is not the only Chinese way to make tea."},
            {"term": "Withering", "def": "Controlled loss of moisture after leaves are picked."},
            {"term": "Heat-fixing / 杀青", "def": "Heating used to slow enzyme activity and shape later transformation."},
            {"term": "Oxidation", "def": "Chemical change that affects colour, aroma, and flavour; it is not identical to microbial fermentation."},
            {"term": "Microbial transformation / fermentation", "def": "Changes involving microorganisms, important in some dark teas and other processes."},
            {"term": "Pearl milk tea / 珍珠奶茶", "def": "A drink developed in Taiwan in the 1980s, commonly combining tea, milk or creamer, sweetness, ice, and tapioca pearls or other toppings."},
            {"term": "Customization", "def": "A system that lets customers select components such as base, sugar, ice, and toppings."},
            {"term": "Service labour", "def": "The work of preparing, explaining, cleaning, scheduling, serving, and managing customer interactions."},
            {"term": "Goji / 枸杞", "def": "A fruit-bearing shrub with long histories in Asia and a significant living history in Edmonton’s river valley and family gardens."},
            {"term": "Everyday care", "def": "Repeated practices of feeding, serving, remembering, checking on, and making time for others. It is not the same as medical treatment."},
            {"term": "Living tradition", "def": "Knowledge and practice renewed by people rather than preserved unchanged."},
            {"term": "Public anthropology", "def": "Anthropological work created for dialogue with wider publics, often through exhibitions, writing, teaching, art, or community collaboration."},
        ]},
    ],
}

# ---------------------------------------------------------- sources-credits
PAGES["sources-credits"] = {
    "title": "Sources & Credits | Go Have Tea",
    "meta": "Curatorial, artist, and research credits for Go Have Tea, plus the exhibition’s selected public sources.",
    "blocks": [
        {"type": "heading", "level": 1, "text": "Sources & Credits"},
        {"type": "heading", "level": 2, "text": "Credit line"},
        {"type": "para", "text": "Curated by Junhong (Summer) Ma. Original calligraphy by Ying (Joy) Wen. Original paintings and artwork by Hui Yang. Edmonton goji research and map by Yong Fei Guan / Edmonton Goji Map, used or linked with permission where applicable. Presented with CGAA volunteers and exhibition partners."},
        {"type": "note", "style": "pending", "text": "Final graphic-design, photography, object-loan, community-contributor, and pavilion credits are added before launch."},
        {"type": "heading", "level": 2, "text": "Selected exhibition sources"},
        {"type": "list", "items": [
            "UNESCO, “Traditional tea processing techniques and associated social practices in China.” ich.unesco.org",
            "Lu et al., “Earliest tea as evidence for one branch of the Silk Road across the Tibetan Plateau,” Scientific Reports 6 (2016). nature.com",
            "Taiwan National Immigration Agency, “The origins of bubble tea, one of Taiwan’s most beloved beverages.” news.immigration.gov.tw",
            "Edmonton Arts Council, “I Am YEG Arts: Yong Fei Guan.” edmontonarts.ca",
            "Edmonton Goji Map. edmonton-goji.github.io/Map/",
            "Fort Edmonton Park, “Goji Berry Teahouse.” fortedmontonpark.ca",
            "W3C, Web Content Accessibility Guidelines (WCAG) 2.2. w3.org/TR/WCAG22/",
        ]},
        {"type": "heading", "level": 2, "text": "Primary project materials"},
        {"type": "list", "items": [
            "Edmonton Heritage Festival Tea Exhibit Research 2026.",
            "Go Have Tea: Tea, Landscape, and the Quiet Work of Anti-Racism, by Hui Yang, Ying Wen, and Junhong Ma.",
            "Final bilingual poster and postcard texts developed for the exhibition.",
            "Approved poster designs, artwork photographs, exhibition labels, curator notes, and educational materials.",
        ]},
        {"type": "heading", "level": 2, "text": "Image and quotation policy"},
        {"type": "para", "text": "Every image carries a nearby credit. Long quotations, community stories, portraits, recordings, maps, and photographs are reproduced only within their permissions. External links do not imply permission to copy material."},
        {"type": "heading", "level": 2, "text": "Educational and research notice"},
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
