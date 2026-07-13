import os
from template import (render, article_page, legal_page, related_cards, faq_html,
                      TOOL_BLOCK, CTA_OFFICIAL, HOME_SCHEMA, SLUG_META, OFFICIAL,
                      UPDATED_ISO, SITE, esc)
from content_a import PAGES_A
from content_b import PAGES_B

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LEGAL = {
"about-us": dict(
    title="About Us – SEPCO Online Bill Guide",
    desc="Who runs sepco-online-bill.com, what the site covers, and how tariff figures are sourced and kept current.",
    h1="About This Site",
    body="""
<p><strong>sepco-online-bill.com</strong> is an independent consumer guide to electricity billing in the SEPCO (Sukkur Electric Power Company) service area of upper Sindh. We explain how to check, read, pay, and reduce SEPCO bills, and we maintain a free browser-based bill estimator built on the current NEPRA tariff schedule.</p>
<h2>What we are — and are not</h2>
<p>We are not affiliated with SEPCO, PITC, NEPRA, or any government body. This site cannot show your actual bill; the only official source for that is PITC's portal at <a href="https://bill.pitc.com.pk/sepcobill" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>. What we add is plain-language guidance: current slab rates, worked examples, complaint routes, and step-by-step instructions that the official channels don't provide in one place.</p>
<h2>How the information is sourced</h2>
<ul>
  <li>Tariff figures follow the NEPRA-notified uniform national tariff (currently FY 2025-26, effective 1 July 2025) and subsequent NEPRA surcharge and adjustment decisions.</li>
  <li>Procedural guidance (portal steps, payment channels, complaint numbers) is verified against the official PITC portal, DISCO publications, and reader corrections.</li>
  <li>Every guide carries its last-updated date. Rates change each July and via quarterly/monthly adjustments — if you spot an outdated figure, please <a href="/contact-us/">tell us</a>.</li>
</ul>
""",
),
"contact-us": dict(
    title="Contact Us – SEPCO Online Bill Guide",
    desc="Report a correction, ask a question about a guide, or send feedback to the sepco-online-bill.com team.",
    h1="Contact Us",
    body="""
<p>Found an outdated rate, a broken step, or something our guides don't cover? We read every message.</p>
<ul>
  <li><strong>Email:</strong> <a href="mailto:contact@sepco-online-bill.com">contact@sepco-online-bill.com</a></li>
</ul>
<h2>Before you write</h2>
<ul>
  <li><strong>For your actual bill amount, outages, or complaints</strong>, we can't help — contact SEPCO directly: helpline <strong>118</strong>, SMS <strong>8118</strong>, or your subdivision office. Full directory: <a href="/sepco-helpline-complaint-numbers/">SEPCO helpline &amp; complaint numbers</a>.</li>
  <li><strong>Never send us your CNIC, account passwords, or payment details.</strong> A bill reference number is enough context for most questions.</li>
  <li>For corrections, include a link to the page and, if possible, a source for the updated figure — corrections ship fastest that way.</li>
</ul>
""",
),
"privacy-policy": dict(
    title="Privacy Policy – SEPCO Online Bill Guide",
    desc="What data sepco-online-bill.com does and doesn't collect: no accounts, no tracking of calculator inputs, standard hosting logs only.",
    h1="Privacy Policy",
    body="""
<p>This site is designed to work without collecting personal data.</p>
<h2>The bill estimator</h2>
<p>Everything you type into the calculator (units, reference numbers, FPA values) is processed <strong>entirely in your browser</strong> by JavaScript running on your device. It is never transmitted to our servers or any third party, and it is not stored after you leave the page.</p>
<h2>What is collected</h2>
<ul>
  <li><strong>Hosting logs:</strong> our hosting provider records standard access logs (IP address, user agent, requested page) for security and reliability. We don't use them to identify visitors.</li>
  <li><strong>No accounts, no cookies for tracking, no analytics identifiers</strong> are set by this site at the time of writing. If we ever add analytics, this policy will be updated first.</li>
</ul>
<h2>External links</h2>
<p>Guides link to official services (e.g. bill.pitc.com.pk, nepra.org.pk, enc.com.pk) and app stores. Those sites have their own privacy practices — anything you enter there is governed by their policies, not ours.</p>
<h2>Contact</h2>
<p>Privacy questions: <a href="/contact-us/">contact page</a>. Last updated 13 July 2026.</p>
""",
),
"terms-and-conditions": dict(
    title="Terms & Conditions – SEPCO Online Bill Guide",
    desc="Terms of use for sepco-online-bill.com: informational content, estimate-only calculator, and limitation of liability.",
    h1="Terms and Conditions",
    body="""
<p>By using sepco-online-bill.com you agree to these terms.</p>
<h2>Informational service</h2>
<p>All content is general consumer information about electricity billing in Pakistan. It is not legal, financial, or official utility advice, and it does not replace communication with SEPCO, PITC, or NEPRA.</p>
<h2>Estimates, not bills</h2>
<p>The bill estimator produces approximations from published tariff schedules. Actual bills include month-specific adjustments (FPA, QTA, surcharges, arrears) that an estimator cannot know. Payment decisions must be based on your official bill from <a href="https://bill.pitc.com.pk/sepcobill" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</p>
<h2>Accuracy and liability</h2>
<p>We work to keep rates and procedures current (each page shows its update date), but tariffs, surcharges, and official processes change frequently. To the maximum extent permitted by law, we accept no liability for losses arising from reliance on this site, including late-payment surcharges, incorrect payments, or decisions based on estimates.</p>
<h2>Acceptable use</h2>
<p>Don't scrape the site at disruptive volume, misrepresent it as an official SEPCO property, or republish substantial portions without attribution and a link.</p>
<p>Last updated 13 July 2026.</p>
""",
),
"disclaimer": dict(
    title="Disclaimer – Independent Guide, Not Official SEPCO",
    desc="sepco-online-bill.com is an independent information site with no affiliation to SEPCO, PITC or the Government of Pakistan.",
    h1="Disclaimer",
    body="""
<p><strong>This is not the official SEPCO website.</strong> sepco-online-bill.com is an independent consumer information site. We have no affiliation with Sukkur Electric Power Company (SEPCO), PITC, NEPRA, or any government entity.</p>
<ul>
  <li><strong>Official bill portal:</strong> <a href="https://bill.pitc.com.pk/sepcobill" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a></li>
  <li><strong>Official SEPCO complaints:</strong> helpline 118 / SMS 8118</li>
  <li><strong>Regulator:</strong> <a href="https://nepra.org.pk" target="_blank" rel="noopener">nepra.org.pk</a></li>
</ul>
<p>Tariff rates, surcharges, taxes, and procedures cited on this site reflect public NEPRA notifications and official announcements as of each page's update date, but they change through the year. The bill estimator provides approximations only. Always confirm amounts, due dates, and procedures through official channels before acting.</p>
<p>Trademarks and names such as SEPCO, PITC, JazzCash, and Easypaisa belong to their respective owners and are used for identification only.</p>
""",
),
}

HOME = dict(
    title="SEPCO Online Bill – Check, Calculate & Understand Your Bill",
    desc="Check your SEPCO bill free with your 14-digit reference number, estimate any bill with FY 2025-26 slab rates, and fix billing problems with clear guides.",
)

def home_page():
    latest = ["sepco-tariff-rates-2026", "sepco-net-metering-guide-2026", "sepco-protected-vs-unprotected-tariff",
              "sepco-fuel-price-adjustment-fpa", "pay-sepco-bill-jazzcash-easypaisa", "sepco-helpline-complaint-numbers",
              "sepco-new-connection-guide", "how-to-reduce-sepco-electricity-bill", "apna-meter-apni-reading-sepco",
              "sepco-load-shedding-schedule-check"]
    guides = ["sepco-online-bill-check", "how-to-check-sepco-bill-online", "sepco-duplicate-bill-guide",
              "sepco-reference-number-guide", "how-to-read-a-sepco-electricity-bill", "sepco-bill-charges-explained",
              "sepco-bill-payment-methods-guide", "sepco-due-date-and-late-payment-guide", "common-sepco-bill-check-errors",
              "sepco-online-bill-on-mobile", "sepco-bill-units-meaning", "faq-about-sepco-online-bill"]

    def cards(slugs):
        out = []
        for s in slugs:
            t, d = SLUG_META[s]
            out.append(f'<a class="link-card" href="/{s}/"><strong>{esc(t)}</strong><p>{esc(d)}</p></a>')
        return "".join(out)

    home_faqs = [
        ("How do I check my actual SEPCO bill?", f'Enter your 14-digit reference number at the official portal, <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>. It’s free with no registration. <a href="/how-to-check-sepco-bill-online/">Step-by-step guide</a>.'),
        ("Is this the official SEPCO website?", 'No — this is an independent guide. We explain the process, maintain current tariff tables, and provide a bill estimator, but only the PITC portal shows your real bill. See our <a href="/disclaimer/">disclaimer</a>.'),
        ("What are the electricity rates right now?", 'FY 2025-26 domestic rates range from Rs 3.95/unit (lifeline) to Rs 47.69/unit (above 700 units), plus surcharges and taxes. <a href="/sepco-tariff-rates-2026/">Full slab tables</a>.'),
        ("Why is my bill suddenly so high?", 'The usual suspects: losing protected status by crossing 200 units, a positive fuel price adjustment, or an estimated meter reading. <a href="/common-sepco-bill-check-errors/">Diagnosis checklist</a>.'),
        ("Which areas does SEPCO serve?", 'Upper Sindh, including Sukkur, Ghotki, Khairpur, Shikarpur, Jacobabad, Kashmore, Larkana, Qambar Shahdadkot, Naushahro Feroze and Dadu districts.'),
        ("Can I pay my bill from my phone?", 'Yes — JazzCash, Easypaisa and every major banking app pay SEPCO bills by reference number, free. <a href="/pay-sepco-bill-jazzcash-easypaisa/">Two-minute walkthrough</a>.'),
    ]

    main_html = f"""    <div class="container">
      <section class="hero">
        <h1>SEPCO Online Bill: Check, Calculate &amp; Understand</h1>
        <p class="lede">Everything for Sukkur Electric Power Company consumers in one place — check your bill on the official portal, estimate any bill with current FY 2025-26 slab rates, and fix billing problems with plain-language guides.</p>
{CTA_OFFICIAL}
      </section>
{TOOL_BLOCK}
      <section class="section">
        <h2>Check your bill in three steps</h2>
        <ol>
          <li>Find the <strong>14-digit reference number</strong> on any old bill (<a href="/where-to-find-sepco-reference-number/">lost it? recover it here</a>).</li>
          <li>Enter it at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> — the official, free PITC portal.</li>
          <li>Read the amount and due date, then <a href="/how-to-download-duplicate-sepco-bill/">save a PDF</a> or <a href="/pay-sepco-bill-jazzcash-easypaisa/">pay from your phone</a>.</li>
        </ol>
      </section>
      <section class="section">
        <h2>Current rates at a glance (FY 2025-26)</h2>
        <div class="table-wrap"><table>
          <thead><tr><th>Category</th><th>Rate range (Rs/unit)</th><th>Key condition</th></tr></thead>
          <tbody>
            <tr><td>Lifeline</td><td>3.95 – 7.74</td><td>Up to 100 units, low-usage history</td></tr>
            <tr><td>Protected</td><td>10.54 – 13.01</td><td>≤ 200 units for 6 straight months</td></tr>
            <tr><td>Non-protected</td><td>22.44 – 47.69</td><td>Everyone else; + FC surcharge &amp; 18% GST</td></tr>
          </tbody>
        </table></div>
        <p>Full slab-by-slab tables, fixed charges and surcharges: <a href="/sepco-tariff-rates-2026/">SEPCO tariff rates 2026</a>. Why crossing 200 units nearly triples the bill: <a href="/sepco-protected-vs-unprotected-tariff/">the 200-unit rule</a>.</p>
      </section>
      <section class="section">
        <h2>Latest guides</h2>
        <div class="cards">{cards(latest)}</div>
      </section>
      <section class="section">
        <h2>Bill basics</h2>
        <div class="cards">{cards(guides)}</div>
      </section>
{faq_html(home_faqs)}
    </div>"""
    return render("/", HOME["title"], HOME["desc"], main_html, HOME_SCHEMA,
                  og_type="website", scripts='  <script src="/script.js" defer></script>')


def notfound_page():
    main_html = """    <div class="container">
      <article class="article" style="text-align:center;padding:3rem 0">
        <h1>Page not found</h1>
        <p class="lede">The address may have changed or never existed. These pages cover most visits:</p>
        <div class="button-row" style="justify-content:center">
          <a class="button button-primary" href="/">Home</a>
          <a class="button button-ghost" href="/sepco-online-bill-check/">Check your bill</a>
          <a class="button button-ghost" href="/sepco-tariff-rates-2026/">Tariff 2026</a>
        </div>
      </article>
    </div>"""
    html = render("/404.html", "Page Not Found – SEPCO Online Bill",
                  "The page you requested was not found.", main_html,
                  {"@context": "https://schema.org", "@type": "WebPage", "name": "Page not found"},
                  og_type="website")
    # 404 should not be indexed or claim a canonical
    html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large">',
                        '<meta name="robots" content="noindex">')
    html = html.replace(f'<link rel="canonical" href="{SITE}/404.html">\n  ', '')
    return html


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


ALL_ARTICLES = {}
ALL_ARTICLES.update(PAGES_A)
ALL_ARTICLES.update(PAGES_B)

for slug, page in ALL_ARTICLES.items():
    write(f"{slug}/index.html", article_page(slug, page))

for slug, page in LEGAL.items():
    write(f"{slug}/index.html", legal_page(slug, page))

write("index.html", home_page())
write("404.html", notfound_page())

# sitemap
urls = [("", "1.0")]
urls += [(s + "/", "0.8") for s in ALL_ARTICLES]
urls += [(s + "/", "0.3") for s in LEGAL]
entries = "\n".join(
    f"  <url>\n    <loc>{SITE}/{u}</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n    <priority>{p}</priority>\n  </url>"
    for u, p in urls
)
write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n')

print(f"\nDone: {len(ALL_ARTICLES)} articles, {len(LEGAL)} legal pages, home, 404, sitemap ({len(urls)} URLs).")
