# Content QA / Hold List

Internal tracking only — **not published** (lives at repo root, outside `docs/`).
Logs every item the v2.0 revision brief's stop-conditions (§19) required us to
leave out of public pages rather than guess. Update this file, don't restore
"pending"-style text to the site.

## Event / logistics

- **Booth / table number within the Chinese Pavilion** — unconfirmed. Not
  mentioned anywhere on the public site (About, homepage). Add once the
  organizer confirms.
- Festival dates/hours/location (Aug 1–3, Hawrelak Park, daily hours) are
  confirmed and live per the brief §4.3 — no action needed there.

## Artists

- **Yang Hui's featured work** ("After Wang Meng's Ge Zhichuan Moving His
  Dwelling") and **Wen Ying's two calligraphy works** — year (2026 placeholder
  used consistently), exact dimensions, and preferred English name order are
  still not independently reconfirmed by the artists themselves. The brief's
  own production-check notes asking for this were removed from public pages
  per the "no visible internal notes" rule, but the underlying confirmation
  still needs to happen before final launch.
- No portrait/statement/audio from either artist — none published, none
  requested without their approval.

## Assets (Phase 3 — deferred, no folder provided this round)

- **Go Have Tea Website Assets/** (posters, fieldwork photos, paintings,
  calligraphy scans, Goji Berry images) — not provided. All `image` blocks
  were removed sitewide per the brief's P0 rule ("no public placeholder
  without an approved image"). Site is text-first until assets arrive.
- **CGAA logo** — not provided. Community Partner sections (About, Credits,
  Edmonton Stories) currently use text + link only, no logo image.
- **《海报文字整理.txt》** (poster master text/citation file) — not provided.
  All 13 poster transcripts and citations currently rely on the original
  content package, which — spot-checked against every specific correction
  named in the brief (Daodejing ch. 22, 無由持一碗, 致虚极，守静笃, artist
  names) — already matched. Re-check against the master file once available,
  in case it differs from the original package anywhere not called out in
  the brief.

## Further Reading — link quality

Brief §21 named exact links for 3 of the 6 books (Thames & Hudson, Camellia
Sinensis's own team, University of Hawai'i Press); I used those exactly. For
the other 3:

- *Tea: History, Terroirs, Varieties* — linked to a Google Books bibliographic
  record; couldn't confirm a dedicated page on the Camellia Sinensis tea
  company's own site.
- 陈宗懋、杨亚军主编《中国茶经》（修订版） and 吴觉农《茶经述评》 — linked to
  Douban bibliographic records (a legitimate Chinese cataloguing site, not a
  retailer) rather than a publisher or library page, since I couldn't
  confidently verify a better authoritative source. Upgrade these to a
  publisher/national-library page if one is confirmed.

## Community Partner

- Found `https://www.cgaa.ab.ca/2026-chinese-pavilion` (a 2026-specific
  Chinese Pavilion page) during research but have **not** added it to
  Credits/Sources yet — only confirmed it exists via a page-content fetch,
  haven't fully vetted its content for accuracy the way the general CGAA
  site and Chinese Pavilion project page were checked. Add once reviewed.

## Edmonton Stories

- "Tea in Everyday Edmonton" module currently states that fieldwork
  photographs and neighbourhood stories will appear once gathered/cleared —
  none exist yet.
- "Share a Story" is explicitly not open — no consent/credit/withdrawal
  process exists yet, per the brief's own instruction not to open this
  until one does.

## Technical

- No `og:image` on Open Graph tags — no approved image asset to use yet.
- Full 360/390/768/1024/1440px screenshot QA and keyboard-navigation testing
  (brief §16.2/§18 Phase 4) were **not** performed — this environment has no
  browser automation tool. Responsive CSS breakpoints (860/700/600px) exist
  and were verified at the code level only. Recommend a manual pass before
  calling this fully launch-ready.
- Artist detail URLs were renamed (`/artists/hui-yang/` → `/artists/yang-hui/`,
  `/artists/ying-joy-wen/` → `/artists/wen-ying/`) per your approval. The old
  URLs now 404 — fine since nothing (QR codes, print material) currently
  points at individual artist pages, only at table/poster/gallery pages.
