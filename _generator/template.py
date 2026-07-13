import json

SITE = "https://sepco-online-bill.com"
SITE_NAME = "SEPCO Online Bill"
UPDATED_HUMAN = "13 July 2026"
UPDATED_ISO = "2026-07-13"
OFFICIAL = "https://bill.pitc.com.pk/sepcobill"

# slug -> (card title, one-line card description). Used for nav, related cards, footer, sitemap.
SLUG_META = {
    "sepco-online-bill-check": ("SEPCO Online Bill Check", "View your latest SEPCO bill free with your 14-digit reference number."),
    "how-to-check-sepco-bill-online": ("How to Check SEPCO Bill Online", "Step-by-step walkthrough of the official portal on phone and computer."),
    "sepco-duplicate-bill-guide": ("SEPCO Duplicate Bill Guide", "What a duplicate bill is, when you need one, and where banks accept it."),
    "how-to-download-duplicate-sepco-bill": ("Download Duplicate SEPCO Bill", "Save your bill as a PDF on Android, iPhone, or computer."),
    "how-to-print-sepco-duplicate-bill": ("Print SEPCO Duplicate Bill", "Print settings and options when you don't have a printer at home."),
    "sepco-reference-number-guide": ("SEPCO Reference Number Guide", "What the 14-digit reference number is and how it is structured."),
    "where-to-find-sepco-reference-number": ("Find Your Reference Number", "Five places to recover your reference number if you lost the bill."),
    "sepco-consumer-id-vs-reference-number": ("Consumer ID vs Reference Number", "The 10-digit customer ID and 14-digit reference number compared."),
    "how-to-read-a-sepco-electricity-bill": ("How to Read a SEPCO Bill", "Every section of the bill explained: readings, charges, history."),
    "sepco-bill-charges-explained": ("SEPCO Bill Charges Explained", "Energy charge, FC surcharge, FPA, QTA and fixed charges decoded."),
    "sepco-bill-taxes-explained": ("SEPCO Bill Taxes Explained", "GST, electricity duty, TV fee and income tax on your bill."),
    "sepco-bill-units-meaning": ("What Bill Units Mean", "How kWh units are read from your meter and priced in slabs."),
    "sepco-due-date-and-late-payment-guide": ("Due Date & Late Payment", "Late payment surcharge, paying after due date, disconnection rules."),
    "sepco-bill-payment-methods-guide": ("SEPCO Bill Payment Methods", "Every way to pay: banks, ATMs, apps, post office and NADRA e-Sahulat."),
    "sepco-peak-hour-charges-guide": ("Peak Hour Charges", "Time-of-use peak timings by season and how to avoid peak rates."),
    "sepco-bill-estimate-calculator-guide": ("SEPCO Bill Calculator", "Estimate your bill from units with FY 2025-26 slab rates."),
    "sepco-bill-not-received-what-to-do": ("Bill Not Received?", "What to do when your paper bill doesn't arrive before the due date."),
    "sepco-online-bill-on-mobile": ("Check Bill on Mobile", "Check, save and pay your SEPCO bill from any smartphone."),
    "common-sepco-bill-check-errors": ("Bill Check Errors & Fixes", "Fixes for 'no record found', wrong digits and portal downtime."),
    "faq-about-sepco-online-bill": ("SEPCO Bill FAQs", "Quick answers to the most common SEPCO billing questions."),
    # new articles
    "sepco-tariff-rates-2026": ("SEPCO Tariff Rates 2026", "Full FY 2025-26 slab rates: lifeline, protected and non-protected."),
    "sepco-protected-vs-unprotected-tariff": ("Protected vs Non-Protected", "The 200-unit rule that can double your per-unit rate."),
    "sepco-fuel-price-adjustment-fpa": ("Fuel Price Adjustment (FPA)", "Why FPA appears on your bill and why it changes every month."),
    "pay-sepco-bill-jazzcash-easypaisa": ("Pay via JazzCash / Easypaisa", "Pay your SEPCO bill from your phone in under two minutes."),
    "sepco-helpline-complaint-numbers": ("Helpline & Complaint Numbers", "SEPCO helpline 118, SMS complaints, offices and NEPRA escalation."),
    "sepco-new-connection-guide": ("New Connection Guide", "Apply online for a SEPCO meter: documents, fees and timelines."),
    "sepco-net-metering-guide-2026": ("Net Metering in 2026", "The new net-billing rules, buyback rates and what still makes sense."),
    "how-to-reduce-sepco-electricity-bill": ("Reduce Your SEPCO Bill", "Practical ways to cut units and stay in a cheaper slab."),
    "apna-meter-apni-reading-sepco": ("Apna Meter Apni Reading", "Submit your own meter reading with PITC's AMAR app."),
    "sepco-load-shedding-schedule-check": ("Load Shedding Schedule", "How to find the outage schedule for your SEPCO feeder."),
    "sepco-bill-check-by-reference-number": ("Check Bill by Reference Number", "The standard method explained: format, entry tips and troubleshooting."),
    "sepco-bill-check-by-customer-id": ("Check Bill by Customer ID", "Why the 10-digit ID doesn't work online and how to convert it."),
    "sepco-bill-check-by-cnic": ("Check Bill by CNIC?", "What your CNIC can and can't do in SEPCO's billing system."),
    "sepco-bill-check-by-name": ("Check Bill by Name?", "Why name search isn't offered and the fastest alternatives."),
    "sepco-bill-check-by-meter-number": ("Check Bill by Meter Number", "Meter number vs reference number, and how to trace one from the other."),
    # legal
    "about-us": ("About Us", "Who runs this site and how the information is checked."),
    "contact-us": ("Contact Us", "Report a correction or send feedback."),
    "privacy-policy": ("Privacy Policy", "How this site handles your data."),
    "terms-and-conditions": ("Terms & Conditions", "Rules for using this website."),
    "disclaimer": ("Disclaimer", "This is an independent guide, not the official SEPCO website."),
}

NAV_ITEMS = [
    ("/", "Home"),
    ("/sepco-online-bill-check/", "Check Bill"),
    ("/sepco-tariff-rates-2026/", "Tariff 2026"),
    ("/sepco-bill-estimate-calculator-guide/", "Calculator"),
    ("/sepco-bill-payment-methods-guide/", "Payments"),
    ("/sepco-helpline-complaint-numbers/", "Helpline"),
    ("/faq-about-sepco-online-bill/", "FAQs"),
]

FOOTER_GUIDES = [
    "sepco-online-bill-check", "how-to-check-sepco-bill-online", "sepco-duplicate-bill-guide",
    "sepco-reference-number-guide", "sepco-bill-payment-methods-guide", "how-to-read-a-sepco-electricity-bill",
]
FOOTER_LATEST = [
    "sepco-tariff-rates-2026", "sepco-net-metering-guide-2026", "sepco-protected-vs-unprotected-tariff",
    "sepco-fuel-price-adjustment-fpa", "pay-sepco-bill-jazzcash-easypaisa", "sepco-helpline-complaint-numbers",
]
FOOTER_LEGAL = ["about-us", "contact-us", "privacy-policy", "terms-and-conditions", "disclaimer"]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def nav_html(current_path):
    links = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == current_path else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return (
        '<header class="site-header"><div class="header-inner">'
        '<a class="brand" href="/"><span class="brand-mark" aria-hidden="true">S</span>'
        '<span class="brand-title">SEPCO Online Bill</span></a>'
        '<nav class="site-nav" aria-label="Primary">' + "".join(links) + "</nav>"
        "</div></header>"
    )


def footer_links(slugs):
    return "".join(f'<a href="/{s}/">{SLUG_META[s][0]}</a>' for s in slugs)


FOOTER = (
    '<footer class="footer-wrap"><div class="footer-inner">'
    "<div><strong>SEPCO Online Bill</strong>"
    '<p class="footer-note">Independent guide to checking, understanding, and paying Sukkur Electric Power Company (SEPCO) bills. '
    "We are not affiliated with SEPCO, PITC, or the Government of Pakistan. For your actual bill, always use the official portal at "
    f'<a href="{OFFICIAL}" rel="noopener" target="_blank">bill.pitc.com.pk/sepcobill</a>.</p></div>'
    "<div><h2>Bill guides</h2>" + footer_links(FOOTER_GUIDES) + "</div>"
    "<div><h2>Latest articles</h2>" + footer_links(FOOTER_LATEST) + "</div>"
    "<div><h2>Site</h2>" + footer_links(FOOTER_LEGAL) + "</div>"
    '</div><div class="footer-bottom">&copy; 2026 sepco-online-bill.com &middot; Tariff figures reflect the NEPRA-notified FY 2025-26 schedule and may change.</div></footer>'
)

CTA_OFFICIAL = (
    '<div class="cta-box"><strong>Check your actual bill:</strong> the official SEPCO bill portal is '
    f'<a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>. '
    "Enter your 14-digit reference number to view, download, or print the real bill free of charge.</div>"
)

TOOL_BLOCK = """
<section class="tool panel" aria-labelledby="tool-title">
  <h2 id="tool-title" style="margin-top:0">SEPCO bill estimator (FY 2025-26 rates)</h2>
  <p class="text-muted">Estimate a domestic bill from your units using the current NEPRA slab rates, and optionally check that your reference number has the correct 14-digit format. This is a local estimate &mdash; it does not fetch your real bill.</p>
  <div class="tool-grid">
    <form class="form-grid" id="billForm">
      <label class="field"><span>Units consumed (kWh)</span>
        <input id="billUnits" type="number" min="0" step="1" value="245" required></label>
      <label class="field"><span>Consumer category</span>
        <select id="billCategory">
          <option value="unprotected" selected>Non-protected (used over 200 units in last 6 months)</option>
          <option value="protected">Protected (200 units or less for 6 months)</option>
          <option value="lifeline">Lifeline (up to 100 units)</option>
        </select></label>
      <label class="field"><span>FPA this month (Rs/unit, from your bill)</span>
        <input id="billFpa" type="number" step="0.01" value="0"></label>
      <label class="field"><span>Reference number (optional format check)</span>
        <input id="billRef" type="text" inputmode="numeric" maxlength="14" placeholder="14 digits"></label>
      <div class="button-row">
        <button class="button button-primary" type="submit">Estimate bill</button>
        <button class="button button-ghost" type="button" id="billPrint">Print</button>
      </div>
    </form>
    <div class="panel" style="box-shadow:none">
      <div class="stat-row">
        <div><span class="eyebrow">Company</span><strong>Sukkur Electric Power Company</strong></div>
        <div><span class="eyebrow">Reference format</span><strong id="billStatus">Waiting</strong></div>
      </div>
      <div id="billPreview"><p class="text-muted">Enter your units and press <em>Estimate bill</em> to see a slab-by-slab breakdown with surcharges and taxes.</p></div>
    </div>
  </div>
</section>
"""


def breadcrumb_schema(name, path):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path},
        ],
    }


def article_schema(title, desc, path):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title,
                "description": desc,
                "dateModified": UPDATED_ISO,
                "inLanguage": "en",
                "mainEntityOfPage": SITE + path,
                "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/about-us/"},
                "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE + "/"},
            },
            breadcrumb_schema(title, path),
        ],
    }


def webpage_schema(title, desc, path):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "name": title, "description": desc, "url": SITE + path, "inLanguage": "en"},
            breadcrumb_schema(title, path),
        ],
    }


HOME_SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": SITE + "/",
            "description": "Independent guide to checking, understanding and paying SEPCO (Sukkur Electric Power Company) electricity bills.",
            "inLanguage": "en",
        },
        {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE + "/",
            "logo": SITE + "/favicon.svg",
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "url": SITE + "/contact-us/"},
        },
    ],
}


def related_cards(slugs):
    cards = []
    for s in slugs:
        title, desc = SLUG_META[s]
        cards.append(f'<a class="link-card" href="/{s}/"><strong>{esc(title)}</strong><p>{esc(desc)}</p></a>')
    return (
        '<section class="related section"><h2>Related guides</h2><div class="cards">' + "".join(cards) + "</div></section>"
    )


def faq_html(faqs):
    if not faqs:
        return ""
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faqs
    )
    return f'<section class="faq section"><h2>Frequently asked questions</h2>{items}</section>'


def render(path, title, desc, main_html, schema, og_type="article", scripts=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{SITE}{path}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#0f8a83">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{SITE}{path}">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:image" content="{SITE}/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE}/og-image.png">
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {nav_html(path)}
  <main id="main">
{main_html}
  </main>
  {FOOTER}
{scripts}
</body>
</html>
"""


def article_page(slug, page):
    """page: dict with title, desc, h1, intro, body, faqs, related, tool(bool)"""
    path = f"/{slug}/"
    h1 = page["h1"]
    tool = TOOL_BLOCK if page.get("tool") else ""
    scripts = '  <script src="/script.js" defer></script>' if page.get("tool") else ""
    main_html = f"""    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span>{esc(h1)}</span></nav>
      <article class="article">
        <p class="updated">Updated {UPDATED_HUMAN}</p>
        <h1>{esc(h1)}</h1>
        <p class="lede">{page["intro"]}</p>
        {tool}
{page["body"]}
{faq_html(page.get("faqs", []))}
      </article>
{related_cards(page.get("related", []))}
    </div>"""
    return render(path, page["title"], page["desc"], main_html, article_schema(page["title"], page["desc"], path), scripts=scripts)


def legal_page(slug, page):
    path = f"/{slug}/"
    main_html = f"""    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span>{esc(page["h1"])}</span></nav>
      <article class="article">
        <p class="updated">Updated {UPDATED_HUMAN}</p>
        <h1>{esc(page["h1"])}</h1>
{page["body"]}
      </article>
    </div>"""
    return render(path, page["title"], page["desc"], main_html, webpage_schema(page["title"], page["desc"], path), og_type="website")
