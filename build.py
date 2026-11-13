#!/usr/bin/env python3
"""BookAtlas web sitesini üretir.

Kullanım:
    python3 build.py

CONFIG içindeki değerleri doldurup betiği yeniden çalıştırmak, bütün
sayfalardaki ilgili alanları günceller. Değeri None olan alanlar sayfada sarı
işaretli yer tutucu olarak görünür; bunlar doldurulmadan site yayımlanmamalıdır.
"""

from __future__ import annotations

import html
from pathlib import Path

import legal_en
import legal_tr

ROOT = Path(__file__).resolve().parent

CONFIG = {
    # Hukuki metinler bir hukukçu tarafından onaylanana kadar True kalmalı:
    # sayfaların üstünde "taslak" şeridi gösterir.
    "draft": False,
    # Veri sorumlusu (şirket unvanı ya da şahıs adı) ve tebligat adresi.
    "controller": "Furkan Oruçoğlu",
    # Tebligat adresi isteğe bağlıdır; boş bırakılırsa metinlerde adres satırı
    # yer almaz ve başvurular e-posta üzerinden alınır.
    "address": "",
    # Destek ve KVKK başvuru e-postası.
    "email": "destek@bookatlas.info",
    # Mağaza ve sosyal medya bağlantıları.
    # İngilizce sayfa ülkeden bağımsız adresi kullanır; App Store ziyaretçiyi
    # kendi ülkesinin mağazasına yönlendirir.
    "app_store_url": "https://apps.apple.com/app/bookatlas/id6760548958",
    "app_store_url_tr": "https://apps.apple.com/tr/app/bookatlas/id6760548958?l=tr",
    # Uygulama henüz Google Play'de değil: boş kaldıkça "Yakında" rozeti görünür.
    "google_play_url": "",
    "instagram_url": "https://www.instagram.com/bookatlasapp/",
    "tiktok_url": "https://www.tiktok.com/@bookatlasapp",
    # Supabase projesinin bulunduğu ülke (Supabase paneli > Project Settings).
    "supabase_region_tr": "ABD",
    "supabase_region_en": "USA",
    # İnternet sitesinin barındırıldığı hizmet.
    "hosting": "GitHub Pages (GitHub, Inc., ABD)",
    # İstanbul yetkisi mevcut Kullanım Koşulları'ndan alınmıştır.
    "court_tr": "İstanbul Mahkemeleri ve İcra Daireleri",
    "court_en": "the courts and enforcement offices of Istanbul",
    "updated_tr": "13.11.2026",
    "updated_en": "13 November 2026",
}


def todo(label: str) -> str:
    return f'<mark class="todo">[{html.escape(label)}]</mark>'


def value(key: str, label: str) -> str:
    current = CONFIG.get(key)
    return html.escape(current) if current else todo(label)


def email_link(label: str) -> str:
    current = CONFIG.get("email")
    if not current:
        return todo(label)
    safe = html.escape(current)
    return f'<a href="mailto:{safe}">{safe}</a>'


def address_line(tr: bool) -> str:
    address = CONFIG.get("address")
    if address is None:
        return f"<strong>{'Adres' if tr else 'Address'}:</strong> {todo('Adres' if tr else 'Address')}<br>"
    if not address:
        return ""
    return f"<strong>{'Adres' if tr else 'Address'}:</strong> {html.escape(address)}<br>"


def written_route(tr: bool) -> str:
    address = CONFIG.get("address")
    if not address:
        return ""
    safe = html.escape(address)
    return f"{safe} adresine yazılı olarak, " if tr else f"in writing to {safe}, or "


def fill(text: str, lang: str) -> str:
    tr = lang == "tr"
    replacements = {
        "{{CONTROLLER}}": value(
            "controller", "Veri sorumlusunun adı / unvanı" if tr else "Name of the data controller"
        ),
        "{{ADDRESS_LINE}}": address_line(tr),
        "{{WRITTEN_ROUTE}}": written_route(tr),
        "{{COURT}}": html.escape(CONFIG["court_tr" if tr else "court_en"]),
        "{{EMAIL}}": email_link("e-posta adresi" if tr else "email address"),
        "{{SUPABASE_REGION}}": value("supabase_region_tr", "Supabase sunucu ülkesi"),
        "{{SUPABASE_REGION_EN}}": value("supabase_region_en", "Supabase server country"),
        "{{HOSTING}}": html.escape(CONFIG["hosting"]),
    }
    for token, replacement in replacements.items():
        text = text.replace(token, replacement)
    assert "{{" not in text, text[text.index("{{") : text.index("{{") + 40]
    return text


# ── Harita görseli ───────────────────────────────────────────────────────────

# Kaba bir dünya haritası: her satır için kara parçalarının sütun aralıkları.
# Sütun = 7,5° boylam (0 = 180°B), satır = 7° enlem (0 = 72°K).
LAND = {
    0: [(10, 15), (18, 21), (34, 42)],
    1: [(2, 15), (18, 20), (26, 46)],
    2: [(3, 4), (7, 11), (14, 15), (23, 23), (25, 44)],
    3: [(7, 16), (23, 43)],
    4: [(7, 15), (23, 28), (30, 42), (44, 44)],
    5: [(8, 14), (23, 23), (25, 41), (43, 43)],
    6: [(9, 13), (22, 40)],
    7: [(10, 11), (13, 13), (22, 31), (34, 35), (37, 40)],
    8: [(11, 12), (22, 28), (30, 30), (34, 34), (37, 38), (40, 40)],
    9: [(12, 12), (14, 16), (22, 30), (34, 34), (37, 37), (40, 40)],
    10: [(14, 17), (25, 29), (37, 39)],
    11: [(14, 19), (25, 29), (38, 43)],
    12: [(14, 19), (26, 29), (30, 30), (41, 42)],
    13: [(15, 18), (26, 28), (30, 30), (39, 43)],
    14: [(15, 17), (26, 28), (39, 44)],
    15: [(15, 16), (26, 27), (40, 44)],
    16: [(15, 16), (43, 43), (46, 47)],
    17: [(15, 15), (46, 46)],
    18: [(15, 15)],
}

# "Okunmuş" olarak boyanan örnek bölgeler: (satır, ilk sütun, son sütun).
READ = [
    (5, 28, 29), (2, 30, 36), (3, 30, 35), (4, 44, 44), (5, 43, 43),
    (11, 15, 18), (12, 15, 18), (3, 23, 23), (9, 24, 25), (7, 34, 35),
    (8, 34, 34), (15, 15, 16), (16, 15, 16), (7, 10, 11), (4, 23, 25),
    (13, 40, 42), (14, 40, 43), (6, 26, 27),
]
SELECTED = [(9, 14, 16), (10, 14, 15)]


def map_svg() -> str:
    def cells(spans):
        return {(row, col) for row, start, end in spans for col in range(start, end + 1)}

    read, selected = cells(READ), cells(SELECTED)
    step, radius = 10, 3.6
    dots = []
    for row, spans in LAND.items():
        for start, end in spans:
            for col in range(start, end + 1):
                if (row, col) in selected:
                    fill_color, opacity = "#e8c66a", "1"
                elif (row, col) in read:
                    fill_color, opacity = "#8dc29e", "1"
                else:
                    fill_color, opacity = "#ffffff", "0.16"
                dots.append(
                    f'<circle cx="{col * step + 5}" cy="{row * step + 5}" r="{radius}" '
                    f'fill="{fill_color}" fill-opacity="{opacity}"/>'
                )
    return (
        '<svg viewBox="0 0 480 190" role="img" aria-hidden="true" focusable="false">'
        + "".join(dots)
        + "</svg>"
    )


# ── Ortak sayfa iskeleti ─────────────────────────────────────────────────────

STRINGS = {
    "en": {
        "skip": "Skip to content",
        "features": "Features",
        "discover": "Discovery",
        "premium": "Premium",
        "faq": "FAQ",
        "draft": "Draft — these pages are awaiting legal review and are not yet in force.",
        "legal": "Legal",
        "contact": "Contact",
        "product": "BookAtlas",
        "tagline": "A reading tracker that turns your books into a map of the world.",
        "rights": "All rights reserved.",
        "updated": "Last updated",
        "other_lang": "TR",
        "other_lang_label": "Türkçe",
        "instagram": "Instagram",
    },
    "tr": {
        "skip": "İçeriğe geç",
        "features": "Özellikler",
        "discover": "Keşif",
        "premium": "Premium",
        "faq": "Sorular",
        "draft": "Taslak — bu sayfalar hukuki inceleme aşamasındadır, henüz yürürlükte değildir.",
        "legal": "Hukuki",
        "contact": "İletişim",
        "product": "BookAtlas",
        "tagline": "Okuduğun kitapları dünya haritasına dönüştüren okuma takip uygulaması.",
        "rights": "Tüm hakları saklıdır.",
        "updated": "Son güncelleme",
        "other_lang": "EN",
        "other_lang_label": "English",
        "instagram": "Instagram",
    },
}

FOOTER_LEGAL = {
    "en": [
        ("terms_of_use.html", "Terms of Use"),
        ("privacy_policy.html", "Privacy Policy"),
        ("account_deletion.html", "Account Deletion"),
        ("tr/aydinlatma-metni-uyeler.html", "KVKK Aydınlatma Metni"),
    ],
    "tr": [
        ("tr/kullanici-sozlesmesi.html", "Kullanıcı Sözleşmesi"),
        ("tr/aydinlatma-metni-uyeler.html", "Üyelere İlişkin Aydınlatma Metni"),
        ("tr/aydinlatma-metni-misafirler.html", "Misafirlere İlişkin Aydınlatma Metni"),
        ("tr/acik-riza-beyani.html", "Açık Rıza Beyanı"),
        ("tr/hesap-silme.html", "Hesap Silme"),
    ],
}


def layout(*, lang, path, title, description, main, other_lang_href, home_sections=True,
           head_extra="", show_draft=False):
    """path: sitenin köküne göre dosya yolu (ör. "tr/index.html")."""
    s = STRINGS[lang]
    base = "../" * path.count("/")
    home = base + ("tr/" if lang == "tr" else "")
    home_href = home or "./"
    anchors = home_href if not home_sections else ""

    nav_links = "".join(
        f'<a href="{anchors}#{anchor}">{s[key]}</a>'
        for anchor, key in (("features", "features"), ("discover", "discover"),
                            ("premium", "premium"), ("faq", "faq"))
    )
    legal_links = "".join(
        f'<li><a href="{base}{href}">{label}</a></li>' for href, label in FOOTER_LEGAL[lang]
    )
    instagram = CONFIG.get("instagram_url")
    instagram_item = (
        f'<li><a href="{html.escape(instagram)}" rel="noopener">{s["instagram"]}</a></li>'
        if instagram else ""
    )
    tiktok = CONFIG.get("tiktok_url")
    if tiktok:
        instagram_item += f'<li><a href="{html.escape(tiktok)}" rel="noopener">TikTok</a></li>'
    draft = f'<div class="draft"><div class="wrap">{s["draft"]}</div></div>' if show_draft else ""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{base}assets/logo.png">
<meta name="theme-color" content="#014421">
<link rel="icon" href="{base}assets/icon.png">
<link rel="stylesheet" href="{base}assets/site.css">
{head_extra}</head>
<body>
<a class="skip" href="#main">{s["skip"]}</a>
{draft}
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{home_href}"><img src="{base}assets/icon.png" alt="" width="36" height="36"><span>Book<b>Atlas</b></span></a>
    <nav class="nav-links" aria-label="{s["product"]}">
      {nav_links}
      <a class="lang" href="{other_lang_href}" lang="{'en' if lang == 'tr' else 'tr'}" aria-label="{s["other_lang_label"]}">{s["other_lang"]}</a>
    </nav>
  </div>
</header>
<main id="main">
{main}
</main>
<footer class="footer">
  <div class="wrap">
    <div>
      <a class="brand" href="{home_href}"><img src="{base}assets/icon.png" alt="" width="36" height="36"><span>Book<b>Atlas</b></span></a>
      <p style="margin-top:12px;max-width:26em">{s["tagline"]}</p>
    </div>
    <div>
      <h4>{s["legal"]}</h4>
      <ul>{legal_links}</ul>
    </div>
    <div>
      <h4>{s["contact"]}</h4>
      <ul>
        <li>{email_link("e-posta adresi" if lang == "tr" else "email address")}</li>
        {instagram_item}
      </ul>
    </div>
    <p class="fine">© 2026 BookAtlas — {html.escape(CONFIG["controller"] or "")}. {s["rights"]}</p>
  </div>
</footer>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print("yazıldı:", path)


# ── Açılış sayfası ───────────────────────────────────────────────────────────

LANDING = {
    "en": {
        "title": "BookAtlas — Read the world, one country at a time",
        "description": "Log the books you read, watch the world map fill in, and discover overlooked authors from every corner of the globe.",
        "eyebrow": "Reading tracker · World literature",
        "h1": "Read the world,<br><em>one country at a time.</em>",
        "lede": "BookAtlas turns your reading into a map. Log the books you finish, watch countries light up, and let an AI guide point you to the authors the bestseller lists overlooked.",
        "app_store": ("Download on the", "App Store"),
        "google_play": ("Get it on", "Google Play"),
        "cta_note": "Free to use. Available in English and Turkish.",
        "card_title": "My reading atlas",
        "card_year": "2026",
        "stats": [("42", "books"), ("17", "countries"), ("31", "authors")],
        "card_caption": "Illustrative example",
        "how_h2": "From a finished book to a coloured map",
        "how_p": "Three steps, a few seconds each.",
        "steps": [
            ("Log a book", "Search by title, scan the barcode on the back cover, or type it in. Add the country, the city and a note if you like."),
            ("Watch the map fill in", "Every book colours its country. The more you read from a place, the deeper the green."),
            ("Find the next one", "Ask the assistant for a recommendation, or tap a country to explore its literature."),
        ],
        "features_h2": "Everything a curious reader needs",
        "features_p": "No feeds, no ads, no noise. Just your books and where they take you.",
        "features": [
            ("🗺️", "A map of your reading", "Filter by country, city, author or year and see your reading life at a glance."),
            ("📚", "Reading list and goals", "Keep track of what you want to read next and set yearly goals for books and countries."),
            ("📊", "Statistics", "Most-read authors and countries, books per year and your best reading months."),
            ("✨", "AI book assistant", "Personal recommendations based on what you have read, with a short reason for each pick."),
            ("🌍", "Country literature", "Pick any country on the map and get a book by an author from there."),
            ("🎬", "Movie pairings", "A daily film suggestion that matches the mood of the books on your shelf."),
            ("📷", "Barcode scanning", "Point your camera at the ISBN and the title and author fill in for you."),
            ("🖼️", "Shareable map card", "Turn your map into an image and share how far your reading has travelled."),
            ("📤", "Your data stays yours", "Export your books as a CSV file whenever you want. View your map even when you are offline."),
        ],
        "band_eyebrow": "Alternative literature",
        "band_h2": "The shelf <em>beyond</em> the bestsellers",
        "band_p1": "BookAtlas grew out of a simple habit: recommending the writers who rarely make the front table. Translated fiction, small presses, regional voices, books that deserve more readers than they have.",
        "band_p2": "The assistant follows the same line. It favours overlooked authors and places you have not read from yet — and if you just want a well-loved classic, ask and it will give you one.",
        "band_link": "Follow the series on Instagram",
        "shelf": [
            ("Under-read authors first", "Recommendations lean away from the titles everyone already knows."),
            ("New countries on your map", "Suggestions nudge you toward places you have not read from."),
            ("Honest about being AI", "Picks are generated by AI and can be wrong; each one says why it was chosen."),
        ],
        "premium_h2": "Free to start. Premium when you want more.",
        "premium_p": "The map, reading list, goals and statistics are free. Premium raises your daily AI limit.",
        "plans": [
            ("Free", "Everything you need to track your reading", [
                "Unlimited book entries and world map",
                "Reading list, goals and statistics",
                "3 AI recommendation credits per day",
                "1 movie pairing per day",
            ], False),
            ("Premium", "For readers who want more discovery", [
                "Everything in Free",
                "20 AI recommendation credits per day",
                "Room for more country literature discoveries (2 credits each)",
            ], True),
        ],
        "premium_note": "Prices are shown in the app in your local currency. Subscriptions are billed through the App Store or Google Play and can be cancelled at any time.",
        "promise_h2": "Built to respect readers",
        "promise": [
            ("No ads", "Nothing is sold to advertisers, and there are no ads in the app."),
            ("No tracking", "No third-party analytics in the app, and no cookies on this website."),
            ("Export anytime", "Download your book entries as a CSV file from the Statistics page."),
            ("Delete anytime", "Remove your account and data from your profile in a few taps."),
        ],
        "faq_h2": "Questions",
        "faq": [
            ("Is BookAtlas free?", "Yes. Logging books, the world map, the reading list, goals and statistics are free. Free accounts also get 3 AI recommendation credits per day. Premium raises that to 20."),
            ("Which languages does it support?", "The app is available in English and Turkish, and it follows your device language. You can log books in any language."),
            ("How do the AI recommendations work?", "When you ask for a recommendation, the titles, authors and countries of the books you have read are sent to an AI model, together with anything you type. Your name and email are not sent. Recommendations are generated by AI and may contain mistakes, so check a book before you buy it."),
            ("Do I need an account?", "Yes. Your books are stored in your account so that they are there when you change phones."),
            ("How do I delete my account?", "Open your profile in the app and choose Delete Account. See the <a href=\"account_deletion.html\">Account Deletion</a> page for details."),
        ],
    },
    "tr": {
        "title": "BookAtlas — Dünyayı ülke ülke oku",
        "description": "Okuduğun kitapları kaydet, dünya haritasının boyanmasını izle ve dünyanın dört bir yanından gözden kaçmış yazarları keşfet.",
        "eyebrow": "Okuma takibi · Dünya edebiyatı",
        "h1": "Dünyayı<br><em>ülke ülke oku.</em>",
        "lede": "BookAtlas okuduklarını bir haritaya dönüştürür. Bitirdiğin kitapları kaydet, ülkelerin renklenmesini izle ve çok satanlar listesinin gözden kaçırdığı yazarları yapay zekâ rehberiyle keşfet.",
        "app_store": ("App Store’dan", "İndir"),
        "google_play": ("Google Play’den", "İndir"),
        "cta_note": "Kullanımı ücretsiz. Türkçe ve İngilizce.",
        "card_title": "Okuma atlasım",
        "card_year": "2026",
        "stats": [("42", "kitap"), ("17", "ülke"), ("31", "yazar")],
        "card_caption": "Örnek görsel",
        "how_h2": "Biten bir kitaptan boyanmış bir haritaya",
        "how_p": "Üç adım, her biri birkaç saniye.",
        "steps": [
            ("Kitabını kaydet", "Adıyla ara, arka kapaktaki barkodu tara ya da elle yaz. İstersen ülke, şehir ve not ekle."),
            ("Haritanın dolmasını izle", "Her kitap kendi ülkesini boyar. Bir yerden ne kadar çok okursan yeşil o kadar koyulaşır."),
            ("Sıradakini bul", "Asistandan öneri iste ya da bir ülkeye dokunup o ülkenin edebiyatını keşfet."),
        ],
        "features_h2": "Meraklı bir okurun ihtiyacı olan her şey",
        "features_p": "Akış yok, reklam yok, gürültü yok. Yalnızca kitapların ve seni götürdükleri yerler.",
        "features": [
            ("🗺️", "Okumalarının haritası", "Ülkeye, şehre, yazara ya da yıla göre filtrele; okuma hayatını tek bakışta gör."),
            ("📚", "Okuma listesi ve hedefler", "Sırada ne okuyacağını takip et, yıllık kitap ve ülke hedefleri koy."),
            ("📊", "İstatistikler", "En çok okuduğun yazarlar ve ülkeler, yıllara göre kitap sayın ve en verimli ayların."),
            ("✨", "Yapay zekâ kitap asistanı", "Okuduklarına göre kişisel öneriler; her öneriyle birlikte kısa bir gerekçe."),
            ("🌍", "Ülke edebiyatı", "Haritadan bir ülke seç, o ülkeden bir yazarın kitabını öneri olarak al."),
            ("🎬", "Film eşleştirmeleri", "Rafındaki kitapların havasına uyan günlük bir film önerisi."),
            ("📷", "Barkod tarama", "Kamerayı ISBN’e tut; kitap adı ve yazar kendiliğinden dolsun."),
            ("🖼️", "Paylaşılabilir harita kartı", "Haritanı bir görsele dönüştür, okumalarının nerelere uzandığını paylaş."),
            ("📤", "Verin senin", "Kitaplarını dilediğin zaman CSV dosyası olarak dışa aktar. Haritanı çevrimdışıyken de gör."),
        ],
        "band_eyebrow": "Alternatif edebiyat",
        "band_h2": "Çok satanların <em>ötesindeki</em> raf",
        "band_p1": "BookAtlas basit bir alışkanlıktan doğdu: vitrine pek çıkmayan yazarları önermek. Çeviri edebiyat, küçük yayınevleri, yerel sesler; hak ettiğinden az okunan kitaplar.",
        "band_p2": "Asistan da aynı çizgiyi izler. Gözden kaçmış yazarları ve henüz okumadığın ülkeleri öne çıkarır. Herkesin sevdiği bir klasik istersen söylemen yeterli.",
        "band_link": "Seriyi Instagram’da takip et",
        "shelf": [
            ("Önce az okunan yazarlar", "Öneriler, herkesin zaten bildiği kitaplardan uzak durur."),
            ("Haritana yeni ülkeler", "Öneriler seni henüz okumadığın yerlere yönlendirir."),
            ("Yapay zekâ olduğunu gizlemez", "Öneriler yapay zekâ tarafından üretilir ve hatalı olabilir; her biri neden seçildiğini söyler."),
        ],
        "premium_h2": "Ücretsiz başla. Daha fazlasını istediğinde Premium.",
        "premium_p": "Harita, okuma listesi, hedefler ve istatistikler ücretsizdir. Premium, günlük yapay zekâ limitini artırır.",
        "plans": [
            ("Ücretsiz", "Okumalarını takip etmek için gereken her şey", [
                "Sınırsız kitap kaydı ve dünya haritası",
                "Okuma listesi, hedefler ve istatistikler",
                "Günde 3 yapay zekâ öneri kredisi",
                "Günde 1 film eşleştirmesi",
            ], False),
            ("Premium", "Daha çok keşfetmek isteyen okurlar için", [
                "Ücretsiz plandaki her şey",
                "Günde 20 yapay zekâ öneri kredisi",
                "Daha çok ülke edebiyatı keşfi (her biri 2 kredi)",
            ], True),
        ],
        "premium_note": "Fiyatlar uygulamada kendi para biriminle gösterilir. Abonelikler App Store veya Google Play üzerinden ücretlendirilir ve dilediğin zaman iptal edilebilir.",
        "promise_h2": "Okura saygıyla tasarlandı",
        "promise": [
            ("Reklam yok", "Reklamverenlere hiçbir şey satılmaz; uygulamada reklam bulunmaz."),
            ("Takip yok", "Uygulamada üçüncü taraf analiz aracı, bu sitede çerez yoktur."),
            ("Dilediğinde dışa aktar", "Kitap kayıtlarını İstatistik sayfasından CSV dosyası olarak indir."),
            ("Dilediğinde sil", "Hesabını ve verilerini profilinden birkaç dokunuşla kaldır."),
        ],
        "faq_h2": "Sorular",
        "faq": [
            ("BookAtlas ücretsiz mi?", "Evet. Kitap kaydı, dünya haritası, okuma listesi, hedefler ve istatistikler ücretsizdir. Ücretsiz hesaplar günde 3 yapay zekâ öneri kredisi kullanır; Premium bunu 20’ye çıkarır."),
            ("Hangi dilleri destekliyor?", "Uygulama Türkçe ve İngilizce kullanılabilir ve cihazının dilini izler. Kitaplarını istediğin dilde kaydedebilirsin."),
            ("Yapay zekâ önerileri nasıl çalışıyor?", "Öneri istediğinde okuduğun kitapların adı, yazarı ve ülkesi, yazdığın istekle birlikte bir yapay zekâ modeline gönderilir. Adın ve e-posta adresin gönderilmez. Öneriler yapay zekâ tarafından üretilir ve hata içerebilir; satın almadan önce kitabı kontrol etmeni öneririz."),
            ("Hesap açmam gerekiyor mu?", "Evet. Kitapların hesabında saklanır; böylece telefon değiştirdiğinde kaybolmaz."),
            ("Hesabımı nasıl silerim?", "Uygulamada profilini aç ve Hesabı Sil seçeneğini kullan. Ayrıntılar <a href=\"hesap-silme.html\">Hesap Silme</a> sayfasında."),
        ],
    },
}


SOON = {"en": ("Coming soon to", "Google Play"), "tr": ("Yakında", "Google Play’de")}


def store_button(key: str, labels: tuple[str, str], primary: bool, lang: str) -> str:
    url = (lang == "tr" and CONFIG.get(f"{key}_tr")) or CONFIG.get(key)
    style = "btn-primary" if primary else "btn-ghost"
    if url:
        inner = f"<span><small>{labels[0]}</small>{labels[1]}</span>"
        return f'<a class="btn {style}" href="{html.escape(url)}" rel="noopener">{inner}</a>'
    # Mağaza bağlantısı yok: tıklanamaz "Yakında" rozeti.
    soon = SOON[lang]
    inner = f"<span><small>{soon[0]}</small>{soon[1]}</span>"
    return f'<span class="btn {style} btn-soon" aria-disabled="true">{inner}</span>'


def landing(lang: str) -> str:
    c = LANDING[lang]
    store_todo = f' {todo("App Store bağlantısı eklenecek")}' if not CONFIG.get("app_store_url") else ""
    instagram = CONFIG.get("instagram_url")
    tiktok = CONFIG.get("tiktok_url")
    tiktok_link = (
        f' · <a href="{html.escape(tiktok)}" rel="noopener">TikTok →</a>' if tiktok else ""
    )
    band_link = (
        f'<p><a href="{html.escape(instagram)}" rel="noopener">{c["band_link"]} →</a>{tiktok_link}</p>'
        if instagram else f'<p>{c["band_link"]} {todo("Instagram bağlantısı")}</p>'
    )

    steps = "".join(f"<li><h3>{t}</h3><p>{p}</p></li>" for t, p in c["steps"])
    features = "".join(
        f'<article><div class="glyph" aria-hidden="true">{g}</div><h3>{t}</h3><p>{p}</p></article>'
        for g, t, p in c["features"]
    )
    shelf = "".join(f"<li><b>{t}</b>{p}</li>" for t, p in c["shelf"])
    plans = "".join(
        f'<div class="plan{" featured" if featured else ""}"><h3>{name}</h3>'
        f'<p class="tag">{tag}</p><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for name, tag, items, featured in c["plans"]
    )
    promise = "".join(f"<li><b>{t}</b><span>{p}</span></li>" for t, p in c["promise"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in c["faq"])
    stats = "".join(f"<div><b>{n}</b><span>{label}</span></div>" for n, label in c["stats"])

    return f"""
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow">{c["eyebrow"]}</span>
      <h1>{c["h1"]}</h1>
      <p class="lede">{c["lede"]}</p>
      <div class="cta" id="download">
        {store_button("app_store_url", c["app_store"], True, lang)}
        {store_button("google_play_url", c["google_play"], False, lang)}
      </div>
      <p class="cta-note">{c["cta_note"]}{store_todo}</p>
    </div>
    <figure class="map-card" style="margin:0">
      <header>{c["card_title"]} <span>{c["card_year"]}</span></header>
      {map_svg()}
      <div class="map-stats">{stats}</div>
      <figcaption>{c["card_caption"]}</figcaption>
    </figure>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="section-head"><h2>{c["how_h2"]}</h2><p>{c["how_p"]}</p></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <div class="section-head"><h2>{c["features_h2"]}</h2><p>{c["features_p"]}</p></div>
    <div class="features">{features}</div>
  </div>
</section>

<section class="band" id="discover">
  <div class="wrap">
    <div>
      <span class="eyebrow">{c["band_eyebrow"]}</span>
      <h2>{c["band_h2"]}</h2>
      <p>{c["band_p1"]}</p>
      <p>{c["band_p2"]}</p>
      {band_link}
    </div>
    <ul class="shelf">{shelf}</ul>
  </div>
</section>

<section id="premium">
  <div class="wrap">
    <div class="section-head"><h2>{c["premium_h2"]}</h2><p>{c["premium_p"]}</p></div>
    <div class="plans">{plans}</div>
    <p style="margin-top:18px;color:var(--ink-faint);font-size:15px">{c["premium_note"]}</p>
  </div>
</section>

<section id="privacy">
  <div class="wrap">
    <div class="section-head"><h2>{c["promise_h2"]}</h2></div>
    <ul class="promise">{promise}</ul>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="section-head"><h2>{c["faq_h2"]}</h2></div>
    <div class="faq">{faq}</div>
  </div>
</section>
"""


# Türkçe tarayıcıları Türkçe sayfaya yönlendirir. "?lang=en" ile devre dışı kalır.
# Hiçbir şey saklamaz (çerez / localStorage kullanılmaz).
def language_redirect(target: str) -> str:
    return (
        "<script>(function(){try{var q=location.search;"
        "if(q.indexOf('lang=en')>-1)return;"
        "var l=(navigator.language||'').toLowerCase();"
        f"if(l.indexOf('tr')===0)location.replace('{target}');"
        "}catch(e){}})();</script>\n"
    )


def build_landing() -> None:
    en, tr = LANDING["en"], LANDING["tr"]
    alternates = (
        '<link rel="alternate" hreflang="en" href="{en}">\n'
        '<link rel="alternate" hreflang="tr" href="{tr}">\n'
    )
    write("index.html", layout(
        lang="en", path="index.html", title=en["title"], description=en["description"],
        main=landing("en"), other_lang_href="tr/",
        head_extra=alternates.format(en="./", tr="tr/") + language_redirect("tr/"),
        show_draft=False,
    ))
    write("tr/index.html", layout(
        lang="tr", path="tr/index.html", title=tr["title"], description=tr["description"],
        main=landing("tr"), other_lang_href="../?lang=en",
        head_extra=alternates.format(en="../", tr="./"),
        show_draft=False,
    ))


# ── Hukuki sayfalar ──────────────────────────────────────────────────────────

def doc_page(*, lang, path, page, nav, current, other_lang_href, head_extra=""):
    s = STRINGS[lang]
    updated = CONFIG["updated_tr"] if lang == "tr" else CONFIG["updated_en"]
    pills = "".join(
        '<a href="{}.html"{}>{}</a>'.format(
            slug, ' aria-current="page"' if slug == current else "", label
        )
        for slug, label in nav
    )
    main = f"""
<article class="doc">
  <div class="wrap">
    <nav class="doc-nav" aria-label="{s["legal"]}">{pills}</nav>
    <h1>{page["h1"]}</h1>
    <p class="meta">{s["updated"]}: {updated}</p>
    {fill(page["body"], lang)}
  </div>
</article>
"""
    return layout(
        lang=lang, path=path, title=f'{page["title"]} — BookAtlas',
        description=page["description"], main=main, other_lang_href=other_lang_href,
        home_sections=False, head_extra=head_extra, show_draft=CONFIG["draft"],
    )


# Türkçe sayfanın İngilizce karşılığı (yoksa İngilizce ana sayfa).
TR_TO_EN = {
    "kullanici-sozlesmesi": "terms_of_use.html",
    "aydinlatma-metni-uyeler": "privacy_policy.html",
    "hesap-silme": "account_deletion.html",
    "acik-riza-beyani": "explicit_consent.html",
}


def build_legal() -> None:
    for slug, page in legal_tr.PAGES.items():
        english = TR_TO_EN.get(slug)
        write(f"tr/{slug}.html", doc_page(
            lang="tr", path=f"tr/{slug}.html", page=page, nav=legal_tr.NAV, current=slug,
            other_lang_href=f"../{english}?lang=en" if english else "../?lang=en",
        ))
    for slug, page in legal_en.PAGES.items():
        # Uygulama bu adresleri iki dilde de açar; Türkçe cihazlar Türkçe metne gider.
        write(f"{slug}.html", doc_page(
            lang="en", path=f"{slug}.html", page=page, nav=legal_en.NAV, current=slug,
            other_lang_href=page["tr"], head_extra=language_redirect(page["tr"]),
        ))

    # Eski adres çalışmaya devam etsin.
    target = "tr/aydinlatma-metni-uyeler.html"
    write("kvkk.html", f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>BookAtlas — KVKK Aydınlatma Metni</title>
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
</head>
<body><p><a href="{target}">Üyelere İlişkin Aydınlatma Metni</a></p></body>
</html>
""")


if __name__ == "__main__":
    build_landing()
    build_legal()
    missing = [key for key, current in CONFIG.items() if current is None]
    if missing:
        print("\nDoldurulması gereken alanlar:", ", ".join(missing))
    if CONFIG["draft"]:
        print("Hukuki sayfalar TASLAK şeridiyle üretildi (CONFIG['draft'] = True).")
