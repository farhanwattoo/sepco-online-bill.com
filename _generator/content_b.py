# 10 new high-value articles.
from template import CTA_OFFICIAL, OFFICIAL

PAGES_B = {

"sepco-tariff-rates-2026": dict(
    title="SEPCO Tariff Rates 2026 – Full Slab Table (FY 2025-26)",
    desc="Complete SEPCO electricity rates for 2026: lifeline, protected and non-protected slab rates per unit, fixed charges, surcharges and how slabs are applied.",
    h1="SEPCO Tariff Rates 2026 (FY 2025-26 Schedule)",
    intro="These are the domestic per-unit rates SEPCO bills under the NEPRA-notified uniform national tariff for FY 2025-26, effective 1 July 2025 — when the average base tariff was cut by about Rs 1.15/unit from the previous year. All figures are base rates; FPA, surcharges and taxes come on top.",
    body="""
<h2>Lifeline consumers (up to 100 units, low usage history)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Slab</th><th>Rate (Rs/unit)</th></tr></thead>
<tbody>
<tr><td>Up to 50 units</td><td>3.95</td></tr>
<tr><td>51 – 100 units</td><td>7.74</td></tr>
</tbody></table></div>
<h2>Protected consumers (≤ 200 units for 6 consecutive months)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Slab</th><th>Rate (Rs/unit)</th></tr></thead>
<tbody>
<tr><td>1 – 100 units</td><td>10.54</td></tr>
<tr><td>101 – 200 units</td><td>13.01</td></tr>
</tbody></table></div>
<h2>Non-protected consumers</h2>
<div class="table-wrap"><table>
<thead><tr><th>Slab</th><th>Rate (Rs/unit)</th><th>Monthly fixed charge</th></tr></thead>
<tbody>
<tr><td>1 – 100 units</td><td>22.44</td><td>—</td></tr>
<tr><td>101 – 200 units</td><td>28.92</td><td>—</td></tr>
<tr><td>201 – 300 units</td><td>33.10</td><td>—</td></tr>
<tr><td>301 – 400 units</td><td>38.00</td><td>Rs 200</td></tr>
<tr><td>401 – 500 units</td><td>40.21</td><td>Rs 400</td></tr>
<tr><td>501 – 600 units</td><td>41.63</td><td>Rs 600</td></tr>
<tr><td>601 – 700 units</td><td>42.77</td><td>Rs 800</td></tr>
<tr><td>Above 700 units</td><td>47.69</td><td>Rs 1,000</td></tr>
</tbody></table></div>
<h2>How slabs are applied (one-slab benefit)</h2>
<p>Domestic consumers keep the benefit of <strong>one previous slab</strong>. Example, 250 units (non-protected): the first 200 units are charged at Rs 28.92 and the remaining 50 at Rs 33.10 — not all 250 at the higher rate. Try any number in the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a>.</p>
<h2>What gets added on top of these rates</h2>
<ul>
  <li><strong>FC surcharge:</strong> Rs 3.23/unit (non-protected). </li>
  <li><strong>FPA:</strong> monthly fuel price adjustment — around Rs 2.5–3.5/unit on average in FY 2025-26, occasionally negative. <a href="/sepco-fuel-price-adjustment-fpa/">How it works</a>.</li>
  <li><strong>Temporary surcharges:</strong> NEPRA approved an extra Rs 3.82/unit for March–June 2026.</li>
  <li><strong>Taxes:</strong> 18% GST (non-protected), ~1.5% electricity duty, Rs 35 TV fee, and advance income tax on large non-filer bills. <a href="/sepco-bill-taxes-explained/">Tax details</a>.</li>
</ul>
<div class="notice">Rates are uniform across all DISCOs nationally, so "SEPCO rates" equal LESCO/HESCO/IESCO rates for the same category. NEPRA revises the base tariff each July and adjusts quarterly — figures above reflect the FY 2025-26 notification and 2026 surcharge decisions.</div>
""",
    faqs=[
        ("Did rates go up or down for 2025-26?", "Down slightly: NEPRA's FY 2025-26 determination cut the average base tariff by roughly Rs 1.15/unit from FY 2024-25 — though the March–June 2026 surcharge clawed part of that back temporarily."),
        ("What rate do I actually pay per unit, all-in?", "A non-protected consumer at 300 units pays roughly Rs 40–45/unit once FC surcharge, FPA, duty and GST are included — versus a base slab rate of Rs 33.10. The calculator shows your all-in figure."),
        ("Are commercial rates the same?", "No — commercial (A-2) tariffs are higher and structured differently (flat + ToU). This page covers domestic (A-1) rates, which apply to homes."),
    ],
    related=["sepco-protected-vs-unprotected-tariff", "sepco-bill-estimate-calculator-guide", "sepco-fuel-price-adjustment-fpa", "sepco-bill-charges-explained", "sepco-bill-taxes-explained", "sepco-peak-hour-charges-guide"],
),

"sepco-protected-vs-unprotected-tariff": dict(
    title="SEPCO Protected vs Non-Protected – The 200-Unit Rule",
    desc="How SEPCO's protected consumer status works: the 6-month 200-unit rule, how much extra non-protected consumers pay, and how to regain protection.",
    h1="Protected vs Non-Protected: SEPCO's 200-Unit Rule",
    intro="No single number affects a small household's bill more than protected status. Cross 200 average units and your per-unit rate roughly doubles on every unit — plus GST kicks in. Here's exactly how the rule works and what it costs.",
    body="""
<h2>The rule</h2>
<p>NEPRA defines a <strong>protected consumer</strong> as a domestic user whose consumption has stayed at <strong>200 units or less in each of the last six consecutive months</strong>. Exceed 200 in even one month, and you're billed as non-protected — and you must complete six consecutive months at ≤200 units to earn protection back.</p>
<h2>What the difference costs (FY 2025-26 rates)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Monthly usage</th><th>Protected (approx.)</th><th>Non-protected (approx.)</th><th>Difference</th></tr></thead>
<tbody>
<tr><td>100 units</td><td>Rs 1,100</td><td>Rs 3,300</td><td>~3× more</td></tr>
<tr><td>180 units</td><td>Rs 2,400</td><td>Rs 6,600</td><td>~2.7× more</td></tr>
<tr><td>200 units</td><td>Rs 2,800</td><td>Rs 7,500</td><td>~2.7× more</td></tr>
</tbody></table></div>
<p class="text-muted">Approximate totals including surcharges, duty, GST and TV fee, excluding FPA. Exact math in the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a>.</p>
<p>The gap has three parts: base rates (Rs 10.54–13.01 vs Rs 22.44–28.92), the FC surcharge (protected consumers are exempt), and 18% GST (protected consumers are exempt).</p>
<h2>How to stay under 200</h2>
<ul>
  <li>Watch the bill mid-month — if you're near 180 units by the reading date, defer heavy loads (see <a href="/how-to-reduce-sepco-electricity-bill/">reduction tactics</a>).</li>
  <li>Summer AC is the usual culprit: one non-inverter AC used nightly adds 300+ units. An inverter model or fan-first cooling keeps many homes protected.</li>
  <li>Verify readings: a single estimated reading above 200 can cost you protection for six months. Contest wrong readings immediately and use the <a href="/apna-meter-apni-reading-sepco/">AMAR app</a>.</li>
</ul>
<h2>Which category am I in right now?</h2>
<p>Your printed bill shows the applied tariff/category, and the 12-month history table lets you count consecutive months under 200. If the bill applied non-protected rates despite six clean months, file a billing complaint — category errors after estimated readings are a known problem. <a href="/sepco-helpline-complaint-numbers/">Complaint contacts</a>.</p>
""",
    faqs=[
        ("Is the 200-unit limit per month or on average?", "The test is consumption in each of the previous six months. One month above 200 breaks the streak and reclassifies you."),
        ("I split my home onto two meters to stay protected — is that allowed?", "Separate legitimate connections for separate portions each get their own status. Artificial splitting of one premises can be challenged during inspection, so tread carefully."),
        ("Does protection apply automatically or must I apply?", "Automatically — the billing system tracks your six-month history and applies the category. No application exists; your only lever is consumption."),
    ],
    related=["sepco-tariff-rates-2026", "how-to-reduce-sepco-electricity-bill", "sepco-bill-units-meaning", "sepco-bill-estimate-calculator-guide", "apna-meter-apni-reading-sepco", "sepco-bill-taxes-explained"],
),

"sepco-fuel-price-adjustment-fpa": dict(
    title="FPA on SEPCO Bills – Fuel Price Adjustment Explained",
    desc="Why the FPA line on your SEPCO bill changes every month, how NEPRA calculates it with a two-month lag, when it's negative, and who's exempt.",
    h1="Fuel Price Adjustment (FPA) on SEPCO Bills",
    intro="FPA is the one line on your bill that changes every single month, sometimes by rupees per unit. It's not a SEPCO decision — it's a national true-up for what generation fuel actually cost, applied to your bill about two months later.",
    body="""
<h2>What FPA is</h2>
<p>The base tariff assumes a reference fuel cost. Real costs vary with global oil/LNG/coal prices, the rupee's exchange rate, and how much cheap hydel or expensive imported fuel was in the generation mix. Each month, the CPPA calculates the difference for the whole country and NEPRA approves passing it on as the <strong>Fuel Price Adjustment</strong> — a per-unit amount multiplied by the units you consumed in the reference month.</p>
<h2>Why the two-month lag</h2>
<p>Fuel accounts are settled after the month closes, then reviewed in a NEPRA hearing, then applied. So the FPA on your July bill typically reflects May's fuel costs. That's why a bill can spike even in a month when you used less electricity.</p>
<h2>Negative FPA happens</h2>
<p>When hydel generation is high (good river flows) or fuel prices fall, the adjustment reverses and appears as a <strong>credit</strong>, reducing your bill. In FY 2025-26 the FPA has averaged roughly Rs 2.5–3.5/unit positive, with occasional negative months.</p>
<h2>Who is exempt or shielded</h2>
<ul>
  <li><strong>Lifeline consumers</strong> are exempt from FPA.</li>
  <li><strong>Protected consumers (≤200 units)</strong> are shielded from most FPA pass-through under current policy.</li>
  <li>EV charging stations and certain categories have specific treatments set in the monthly SRO.</li>
</ul>
<h2>Reading FPA on your bill</h2>
<p>Look for a line labelled <strong>FPA</strong> or "Fuel Price Adjustment" in the charges block, showing the Rs/unit rate and the month it belongs to. GST applies on top of FPA, so a Rs 3/unit FPA actually costs a non-protected consumer ~Rs 3.54/unit. Enter your bill's FPA rate into the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a> to reproduce your total.</p>
""",
    faqs=[
        ("Can I avoid FPA by paying early?", "No — FPA is part of the billed amount. The only ways to reduce FPA exposure are using fewer units or qualifying as protected/lifeline."),
        ("Why is FPA the same across DISCOs?", "Generation costs are pooled nationally through the CPPA, so NEPRA notifies one uniform FPA rate for all DISCOs including SEPCO (K-Electric is determined separately)."),
        ("My neighbour's FPA differed from mine — how?", "The Rs/unit rate is uniform, but it multiplies each home's units in the reference month, and category exemptions (protected/lifeline) change what's actually charged."),
    ],
    related=["sepco-bill-charges-explained", "sepco-tariff-rates-2026", "sepco-protected-vs-unprotected-tariff", "sepco-bill-estimate-calculator-guide", "sepco-bill-taxes-explained", "how-to-reduce-sepco-electricity-bill"],
),

"pay-sepco-bill-jazzcash-easypaisa": dict(
    title="Pay SEPCO Bill via JazzCash or Easypaisa – 2-Minute Guide",
    desc="Exact steps to pay a SEPCO bill in the JazzCash and Easypaisa apps, fees, confirmation, saving the biller, and fixing a payment that doesn't show.",
    h1="Pay Your SEPCO Bill with JazzCash or Easypaisa",
    intro="Both wallets pay SEPCO bills free of charge, in about two minutes, with nothing but your 14-digit reference number. Here are the exact taps in each app, plus what to do if a payment doesn't reflect.",
    body="""
<h2>JazzCash steps</h2>
<ol>
  <li>Open the JazzCash app and log in.</li>
  <li>Tap <strong>Pay Bills</strong> (or "Bill Payment") &rarr; <strong>Electricity</strong>.</li>
  <li>Select <strong>SEPCO</strong> from the company list.</li>
  <li>Enter your <strong>14-digit reference number</strong> — the app fetches your name, bill month, amount, and due date. Verify these before paying.</li>
  <li>Confirm with your PIN. You'll get an in-app receipt and SMS with a transaction ID — screenshot or save it.</li>
</ol>
<h2>Easypaisa steps</h2>
<ol>
  <li>Open Easypaisa and tap <strong>Bill Payment</strong>.</li>
  <li>Choose <strong>Electricity</strong> &rarr; <strong>SEPCO</strong>.</li>
  <li>Enter the reference number, review the fetched bill details, and confirm with your PIN.</li>
  <li>Save the confirmation. Use "Save this bill" / favourites so next month is three taps.</li>
</ol>
<h2>Fees, limits, timing</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>JazzCash</th><th>Easypaisa</th></tr></thead>
<tbody>
<tr><td>Fee for utility bills</td><td>Free</td><td>Free</td></tr>
<tr><td>After due date bills</td><td>Accepted (collects the higher amount)</td><td>Accepted</td></tr>
<tr><td>Confirmation</td><td>Instant SMS + in-app receipt</td><td>Instant SMS + in-app receipt</td></tr>
<tr><td>Posting to SEPCO's system</td><td>Usually same day, up to 2 working days</td><td>Usually same day, up to 2 working days</td></tr>
</tbody></table></div>
<h2>If the payment doesn't reflect</h2>
<ol>
  <li>Wait two working days — posting lags are normal, and your transaction timestamp protects you from surcharge disputes.</li>
  <li>If the next bill still shows the amount as arrears, contact the wallet's helpline (JazzCash <strong>4444</strong>, Easypaisa <strong>3737</strong>) with the transaction ID for a trace.</li>
  <li>Take the receipt to your SEPCO subdivision office for a manual adjustment if needed — <a href="/sepco-helpline-complaint-numbers/">contacts here</a>.</li>
</ol>
<p>No smartphone? Both networks' <strong>agent shops</strong> pay the bill over the counter for cash — just bring the reference number. All other channels: <a href="/sepco-bill-payment-methods-guide/">payment methods compared</a>.</p>
""",
    faqs=[
        ("Do I need a JazzCash/Easypaisa account with money in it?", "Yes for in-app payment — top up at any agent, via bank transfer, or debit card. Alternatively pay cash at an agent shop without any account."),
        ("Can I pay someone else's bill?", "Yes. The apps don't check whose bill it is — enter any reference number, verify the fetched name matches who you intend to pay for, and confirm."),
        ("Is there a limit on the bill amount?", "Wallet accounts have monthly transaction limits based on your account tier. Very large bills may exceed a basic account's limit — upgrade the account or pay at a bank."),
    ],
    related=["sepco-bill-payment-methods-guide", "sepco-due-date-and-late-payment-guide", "sepco-online-bill-on-mobile", "sepco-online-bill-check", "where-to-find-sepco-reference-number", "faq-about-sepco-online-bill"],
),

"sepco-helpline-complaint-numbers": dict(
    title="SEPCO Helpline & Complaint Numbers 2026 – All Contacts",
    desc="SEPCO helpline 118, complaint SMS 8118, regional office numbers, what info to have ready, and how to escalate unresolved complaints to NEPRA.",
    h1="SEPCO Helpline and Complaint Numbers",
    intro="For outages, billing errors, meter problems, or theft reporting, SEPCO runs a 24/7 helpline plus SMS and walk-in channels — and if SEPCO doesn't resolve it, NEPRA runs a formal escalation path. All working contacts below.",
    body="""
<h2>Primary contacts</h2>
<div class="table-wrap"><table>
<thead><tr><th>Channel</th><th>Contact</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><strong>Helpline (24/7)</strong></td><td><strong>118</strong></td><td>Outages, urgent complaints</td></tr>
<tr><td>Helpline (direct)</td><td>071-9310797</td><td>If 118 doesn't connect from your network</td></tr>
<tr><td><strong>SMS complaints</strong></td><td>SMS to <strong>8118</strong></td><td>Text "SEPCO [your complaint]" — get a tracking ID</td></tr>
<tr><td>Regional customer service centre</td><td>Minara Road, Sukkur — 071-9310921</td><td>In-person follow-up</td></tr>
<tr><td>Your subdivision (SDO) office</td><td>Printed on your bill</td><td>Billing corrections, duplicate bills, installments, name transfer</td></tr>
</tbody></table></div>
<h2>Have this ready before you call</h2>
<ul>
  <li>Your <strong>14-digit reference number</strong> (the agent's first question).</li>
  <li>The bill month and the specific line item you're disputing, if it's a billing complaint.</li>
  <li>Your meter's actual current reading (photo helps) for wrong-reading complaints.</li>
  <li>Note the <strong>complaint number</strong> the agent gives you — you'll need it for follow-up and escalation.</li>
</ul>
<h2>Escalation ladder</h2>
<ol>
  <li><strong>118 / SDO office</strong> — most complaints resolve here. Allow the standard response time (outages: hours; billing: up to a couple of weeks).</li>
  <li><strong>XEN / Superintending Engineer</strong> — take your complaint number up a level; numbers are on your bill or at the regional office.</li>
  <li><strong>NEPRA</strong> — the regulator accepts unresolved consumer complaints: toll-free <strong>0800-63762</strong>, or file online at <a href="https://nepra.org.pk" target="_blank" rel="noopener">nepra.org.pk</a> (Consumer Affairs &rarr; Complaints). NEPRA directions are binding on SEPCO.</li>
</ol>
<h2>What each office can actually do</h2>
<p>Phone agents log complaints and dispatch line staff. Money matters — bill corrections, surcharge reversal, <a href="/sepco-due-date-and-late-payment-guide/">installment plans</a>, detection bill disputes — are decided at the SDO/XEN office, so go in person for those, with photocopies of your CNIC, bill, and any payment receipts.</p>
""",
    faqs=[
        ("Is 118 free to call?", "From most networks 118 is charged as a normal local call and connects to your regional complaint centre; if it fails, use the direct city number."),
        ("How long until an outage complaint is acted on?", "Routine fault restoration typically happens within hours under NEPRA's service standards; transformer replacement and major faults take longer. Repeated unaddressed outages are exactly what the NEPRA escalation exists for."),
        ("Can I complain about load shedding?", "You can complain about excess/unscheduled shedding, especially if your feeder is being shed beyond announced schedules. See our load shedding guide for how schedules are set."),
    ],
    related=["sepco-load-shedding-schedule-check", "sepco-bill-not-received-what-to-do", "common-sepco-bill-check-errors", "sepco-due-date-and-late-payment-guide", "sepco-new-connection-guide", "faq-about-sepco-online-bill"],
),

"sepco-new-connection-guide": dict(
    title="SEPCO New Connection 2026 – Apply Online, Fees, Timeline",
    desc="How to get a new SEPCO electricity connection: the ENC online portal, required documents, demand notice payment, fees and NEPRA timelines.",
    h1="SEPCO New Electricity Connection Guide",
    intro="New domestic connections are applied for online through the national ENC portal — no agent required. Here's the document list, the actual sequence of steps, what it costs, and the timelines NEPRA holds SEPCO to.",
    body="""
<h2>Where to apply</h2>
<p>Use the <strong>ENC (Electricity New Connection) portal</strong> at <a href="https://enc.com.pk" target="_blank" rel="noopener">enc.com.pk</a> — the unified online application system for all DISCOs including SEPCO. Select SEPCO, your district and subdivision, then fill the application. You can also apply on paper at the subdivision office, but the portal gives you tracking and cuts visits.</p>
<h2>Documents you'll need</h2>
<ul>
  <li>CNIC copy of the applicant (and of the property owner, if different).</li>
  <li>Proof of ownership or tenancy: registry, allotment letter, lease/rent agreement.</li>
  <li>A copy of a <strong>neighbour's recent bill</strong> (locates your premises on the network).</li>
  <li>Site/location details and requested load (a normal house is a single-phase connection up to 5 kW).</li>
  <li>Passport photo and, for tenants, an owner NOC in some cases.</li>
</ul>
<h2>The process, step by step</h2>
<ol>
  <li><strong>Apply</strong> on ENC with scanned documents; note your tracking number.</li>
  <li><strong>Site survey:</strong> SEPCO staff verify the premises and distance from the distribution network.</li>
  <li><strong>Demand notice:</strong> you receive a notice stating the connection charges — pay it at a designated bank and upload/submit the receipt.</li>
  <li><strong>Meter installation:</strong> after demand-notice payment, the connection order is issued and the meter installed.</li>
</ol>
<h2>Costs and timelines</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Typical range</th></tr></thead>
<tbody>
<tr><td>Application</td><td>Free on the ENC portal</td></tr>
<tr><td>Demand notice (single-phase domestic)</td><td>Varies by load and service length — commonly tens of thousands of rupees; the notice itself is the authoritative figure</td></tr>
<tr><td>NEPRA timeline (single-phase, no network extension)</td><td>~30 days from demand-notice payment</td></tr>
<tr><td>Where network extension is needed</td><td>Longer, per the survey's scope</td></tr>
</tbody></table></div>
<div class="notice">Pay only against the printed demand notice at the designated bank. No SEPCO field employee is authorised to collect connection money in cash — "speed money" requests are a scam and worth reporting on 118 or to NEPRA.</div>
<p>Once the meter is live, your first bill establishes your <a href="/sepco-reference-number-guide/">14-digit reference number</a> — save it immediately for online checking and payments.</p>
""",
    faqs=[
        ("Can a tenant apply for a connection?", "Yes, with the tenancy agreement and typically the owner's NOC/CNIC copy. The connection can later be transferred to the owner's or a new occupant's name at the SDO office."),
        ("How do I track my application?", "The ENC portal shows status against your tracking number at each stage (survey, demand notice, connection order). Stalled applications can be pursued at the SDO office or escalated to NEPRA."),
        ("What load should a normal house request?", "Most homes fit comfortably in a single-phase 5 kW sanctioned load. If you plan heavy AC use or a large motor, discuss a three-phase connection at survey time — upgrading later costs more."),
    ],
    related=["sepco-reference-number-guide", "sepco-helpline-complaint-numbers", "sepco-tariff-rates-2026", "sepco-net-metering-guide-2026", "sepco-online-bill-check", "faq-about-sepco-online-bill"],
),

"sepco-net-metering-guide-2026": dict(
    title="SEPCO Net Metering 2026 – New Rules & Buyback Rates",
    desc="Pakistan's 2026 solar rules changed everything: net billing replaces net metering, buyback near Rs 8-13/unit for new users, existing agreements protected.",
    h1="SEPCO Net Metering in 2026: What Changed",
    intro="In early 2026 NEPRA replaced the old net metering regime with new Prosumer Regulations — new solar users now sell surplus at a far lower rate under 'net billing'. Existing agreement holders keep their old terms. Here's what the rules mean for a SEPCO consumer deciding on solar now.",
    body="""
<h2>Old system vs new system</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Net metering (old)</th><th>Net billing (2026 rules)</th></tr></thead>
<tbody>
<tr><td>Exported units</td><td>Offset imported units ~1:1</td><td>Bought at a fixed buyback rate</td></tr>
<tr><td>Buyback rate</td><td>~Rs 25.32/unit (national average power purchase price)</td><td>~Rs 8–13/unit for new consumers (finalized around Rs 8.13 in NEPRA's decision, subject to tariff updates)</td></tr>
<tr><td>Agreement term</td><td>7 years</td><td>5 years</td></tr>
<tr><td>Who it applies to</td><td>Agreements signed before the new regulations (protected until expiry per NEPRA's Feb 2026 draft amendment)</td><td>New applicants</td></tr>
</tbody></table></div>
<h2>Are existing solar users affected?</h2>
<p>After significant public pushback and the Prime Minister's intervention, NEPRA issued a draft amendment (16 February 2026) confirming that consumers holding <strong>valid net metering agreements as of 9 February 2026 keep their existing rates until their agreement expires</strong>. If you already have net metering on a SEPCO connection, your terms continue; watch renewal dates.</p>
<h2>Does solar still make sense on SEPCO?</h2>
<p>Yes — but the economics now favour <strong>self-consumption</strong> over exporting:</p>
<ul>
  <li>Every unit you consume directly from your panels still saves the full retail rate — Rs 40+ all-in for non-protected consumers (<a href="/sepco-tariff-rates-2026/">rates</a>). That value didn't change.</li>
  <li>Exported surplus now earns ~Rs 8–13 instead of ~Rs 25 — so oversizing a system to "sell to SEPCO" no longer pays.</li>
  <li>Right-size the system to your daytime load, and consider batteries to shift solar into the expensive <a href="/sepco-peak-hour-charges-guide/">evening peak</a>.</li>
</ul>
<h2>How to apply on a SEPCO connection</h2>
<ol>
  <li>Use an <strong>AEDB-registered installer</strong> — they prepare the interconnection application.</li>
  <li>Apply through SEPCO with your connection's reference number; the file covers inverter specs, protection, and a site inspection.</li>
  <li>After approval and agreement signing, a bidirectional meter is installed and export credits appear on your bill.</li>
</ol>
<div class="notice">Rules were still being amended through 2026 — verify the current buyback rate and agreement terms at <a href="https://nepra.org.pk" target="_blank" rel="noopener">nepra.org.pk</a> before signing anything.</div>
""",
    faqs=[
        ("I applied before the new regulations but wasn't approved yet — which rules apply?", "The cutoff in NEPRA's amendment is holding a valid agreement as of 9 February 2026. In-process applications generally fall under the new net billing framework — confirm your file's status with SEPCO and your installer."),
        ("Do protected consumers lose protection by installing solar?", "Protection status is based on your billed (net) consumption. Solar that keeps your grid consumption at/under 200 units can actually help you stay protected — one more argument for self-consumption sizing."),
        ("What system size does a typical home need?", "Rule of thumb: ~4 units/day generated per kW installed in upper Sindh's sun. A home using 300 units monthly needs roughly 3 kW to cover daytime usage; batteries change the calculus."),
    ],
    related=["sepco-tariff-rates-2026", "sepco-peak-hour-charges-guide", "how-to-reduce-sepco-electricity-bill", "sepco-new-connection-guide", "sepco-bill-units-meaning", "sepco-protected-vs-unprotected-tariff"],
),

"how-to-reduce-sepco-electricity-bill": dict(
    title="How to Reduce Your SEPCO Bill – 10 Tactics That Work",
    desc="Practical, Pakistan-specific ways to cut a SEPCO electricity bill: stay protected, beat the slab system, AC strategy, and appliance-level wins.",
    h1="How to Reduce Your SEPCO Electricity Bill",
    intro="Because of slab pricing and the protection rule, cutting a modest number of units often saves a disproportionate amount of money. These tactics are ordered by impact for a typical upper-Sindh household.",
    body="""
<h2>1. Defend protected status (biggest single lever)</h2>
<p>Keeping every month at ≤200 units bills you at roughly a third of the non-protected cost (<a href="/sepco-protected-vs-unprotected-tariff/">why</a>). If you hover near the line, the marginal value of saving 10–20 units is enormous — a Rs 4,000+ difference for essentially the same lifestyle.</p>
<h2>2. Fix the AC, fix the bill</h2>
<ul>
  <li>A 1.5-ton <strong>inverter AC</strong> uses roughly 40–60% less than an old non-inverter unit — often 150+ units/month saved in summer.</li>
  <li>Set 26°C, not 18°C: each degree lower adds ~5–8% consumption.</li>
  <li>Service filters before summer; a choked filter can add 15–20%.</li>
  <li>Cool the person, not the room: a fan alongside the AC lets you raise the thermostat 2 degrees comfortably.</li>
</ul>
<h2>3. Beat the slab boundaries</h2>
<p>Slabs mean the <em>last</em> units are the expensive ones. If you're at 310 units, cutting just 11 units drops the fixed charge (Rs 200) and moves your marginal rate down a slab. Check where you sit with the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a> before deciding what's worth changing.</p>
<h2>4. The quiet baseline eaters</h2>
<div class="table-wrap"><table>
<thead><tr><th>Change</th><th>Approx. monthly saving</th></tr></thead>
<tbody>
<tr><td>Replace 10 old bulbs/tubes with LEDs</td><td>30–60 units</td></tr>
<tr><td>Old fridge → inverter fridge (or fix door seals)</td><td>20–40 units</td></tr>
<tr><td>DC-inverter ceiling fans (vs old 100 W fans)</td><td>10–20 units per fan in summer</td></tr>
<tr><td>Iron once–twice weekly in batches</td><td>5–10 units</td></tr>
<tr><td>Water pump on a timer (no dry running)</td><td>10–20 units</td></tr>
</tbody></table></div>
<h2>5. Verify you're only paying for your own units</h2>
<ul>
  <li>Compare the bill's reading with the meter monthly — estimated readings above actual are money out the door (<a href="/apna-meter-apni-reading-sepco/">submit your own with AMAR</a>).</li>
  <li>A meter that runs with the main switch off needs a meter-accuracy complaint (118).</li>
  <li>Direct-line theft on your feeder raises everyone's outage hours, not your bill — but report it anyway; feeders with lower losses get less load shedding (<a href="/sepco-load-shedding-schedule-check/">how that works</a>).</li>
</ul>
<h2>6. Solar for self-consumption</h2>
<p>Even under the 2026 net-billing rules, replacing Rs 40+/unit grid daytime consumption with your own panels remains highly economic — the payback on a right-sized system is typically 3–5 years. What changed is that <em>overselling</em> to the grid no longer pays (<a href="/sepco-net-metering-guide-2026/">2026 rules explained</a>).</p>
""",
    faqs=[
        ("What saves more — solar or an inverter AC?", "If your summer bill is AC-driven, the inverter AC usually has the faster payback (1–2 summers). Solar has the bigger ceiling. Households that do both often cut bills by 70%+."),
        ("Do 'power saver' plug-in devices work?", "No. Domestic consumers are billed on real energy (kWh); the capacitor gadgets sold as savers don't reduce kWh. Spend the money on LEDs instead."),
        ("Is running appliances at night cheaper?", "Only for time-of-use (ToU) metered connections. Standard domestic meters charge the same rate around the clock — but night running still helps if you have solar during the day and batteries."),
    ],
    related=["sepco-protected-vs-unprotected-tariff", "sepco-bill-units-meaning", "sepco-net-metering-guide-2026", "sepco-tariff-rates-2026", "sepco-peak-hour-charges-guide", "apna-meter-apni-reading-sepco"],
),

"apna-meter-apni-reading-sepco": dict(
    title="Apna Meter Apni Reading (AMAR) for SEPCO – Setup Guide",
    desc="Use PITC's AMAR app on a SEPCO connection: register with your reference number, photograph the meter in your reading window, avoid estimated bills.",
    h1="Apna Meter Apni Reading (AMAR) for SEPCO Consumers",
    intro="AMAR ('my meter, my reading') is PITC's official app that lets you photograph your own meter during a monthly window, so your bill is generated on your actual reading — the definitive fix for estimated and inflated readings.",
    body="""
<h2>Why it matters</h2>
<p>When a meter reader can't reach your meter (locked gate, absent household) the system bills an <strong>estimated</strong> figure. Estimates can push you over a slab boundary or past the 200-unit protection line — costing real money even after later correction. A self-submitted photo reading prevents the estimate from happening at all.</p>
<h2>Setting it up</h2>
<ol>
  <li>Install <strong>"Apna Meter Apni Reading"</strong> (PITC) from Google Play. It covers all PITC-billed DISCOs, including SEPCO.</li>
  <li>Register with your mobile number and add your connection using the <strong>14-digit reference number</strong> (<a href="/where-to-find-sepco-reference-number/">where to find it</a>).</li>
  <li>The app shows your <strong>reading window</strong> — a few days around your area's scheduled meter-reading date. You'll get a notification when it opens.</li>
  <li>In the window, photograph the meter display through the app. The image must show the kWh digits clearly; the app reads and submits them with the photo as evidence.</li>
</ol>
<h2>Getting a usable photo</h2>
<ul>
  <li>Clean the meter glass; shoot straight-on without flash glare (angle slightly if the LCD reflects).</li>
  <li>Include all integer digits — decimals/red digits aren't needed.</li>
  <li>For electromechanical (dial) meters, capture the counter row sharply.</li>
</ul>
<h2>What happens next</h2>
<p>Your submitted reading feeds the billing run for that month; the printed bill should match the reading you sent (the photo stays on record in case of dispute). If a bill ignores a valid submission, take the app's submission record to your SDO office or call 118 — it's strong evidence for a correction.</p>
<div class="notice">Miss the window? The app won't accept readings outside it — the ordinary reader/estimate process applies that month. Set the app's notification on and add a phone reminder for your window dates.</div>
""",
    faqs=[
        ("Is AMAR free? Is it official?", "Yes and yes — it's published by PITC, the company that runs billing for SEPCO and the other DISCOs. It's free with no in-app payments."),
        ("Is there an iPhone version?", "AMAR launched on Android; iOS availability has lagged. iPhone users can submit from any Android family member's phone — the account maps to the connection, not the device."),
        ("Can I use one app for several meters?", "Yes — add each connection's reference number to your account and you'll get separate reading windows for each."),
    ],
    related=["sepco-bill-units-meaning", "common-sepco-bill-check-errors", "how-to-read-a-sepco-electricity-bill", "sepco-protected-vs-unprotected-tariff", "sepco-bill-not-received-what-to-do", "sepco-online-bill-on-mobile"],
),

"sepco-load-shedding-schedule-check": dict(
    title="SEPCO Load Shedding Schedule – How to Find Yours",
    desc="How SEPCO load shedding schedules are set by feeder, how to find the hours for your area, and what to do about unscheduled outages.",
    h1="How to Check the SEPCO Load Shedding Schedule",
    intro="SEPCO publishes no reliable public schedule page, but shedding isn't random either — it's set per feeder based on that feeder's loss and recovery profile. Here's how to find your feeder's hours and act on unscheduled outages.",
    body="""
<h2>How shedding is decided</h2>
<p>Under the national policy, feeders are categorised by their <strong>AT&amp;C losses</strong> (theft + unpaid bills). Low-loss feeders get zero or minimal shedding; high-loss feeders can face many hours daily. That's why one neighbourhood in Sukkur has near-continuous supply while another a kilometre away doesn't — and why your area's schedule changes when its recovery figures change.</p>
<h2>Ways to find your feeder's hours</h2>
<ol>
  <li><strong>Call 118</strong> and ask for the current shedding schedule for your feeder — give your reference number or feeder name (printed on your bill near the subdivision details).</li>
  <li><strong>Ask at the subdivision (SDO) office</strong> — they hold the operative schedule for every feeder they manage.</li>
  <li><strong>Local sources:</strong> area WhatsApp groups and the SEPCO/local press often circulate seasonal schedule changes faster than any official channel.</li>
  <li>For planned <strong>maintenance shutdowns</strong>, SEPCO announces feeder-level timings in local newspapers a day or two ahead.</li>
</ol>
<h2>Scheduled vs unscheduled outages</h2>
<ul>
  <li>If outages consistently exceed the schedule you were quoted, that's a legitimate complaint — log it on <strong>118</strong> each time and keep the complaint numbers.</li>
  <li>Repeated feeder tripping (short random cuts) usually indicates an overloaded transformer or line fault — report it; this is a repairable fault, not policy shedding.</li>
  <li>A pattern of unresolved complaints is escalatable to <a href="/sepco-helpline-complaint-numbers/">XEN and then NEPRA</a>.</li>
</ul>
<h2>Living with it: practical notes</h2>
<ul>
  <li>Size UPS batteries to your feeder's real worst-case hours, not the advertised ones.</li>
  <li>Solar + battery combos decouple you from daytime shedding entirely — see the <a href="/sepco-net-metering-guide-2026/">2026 solar guide</a>.</li>
  <li>Community bill recovery genuinely changes categories: feeders that improve collections get moved to lower-shedding tiers.</li>
</ul>
""",
    faqs=[
        ("Is there an official app or page with SEPCO schedules?", "No dependable public one. The operative schedule lives with the subdivision and control room, which is why calling 118 or the SDO office is the accurate route."),
        ("Why does my area's schedule keep changing?", "Feeder categories are revisited as loss/recovery data updates, and summer generation shortfalls add temporary shedding on top of the base schedule."),
        ("Does paying my own bill on time reduce my shedding?", "Individually no, collectively yes — categorisation is per feeder. Areas that lift their collective recovery have moved into better categories."),
    ],
    related=["sepco-helpline-complaint-numbers", "sepco-net-metering-guide-2026", "how-to-reduce-sepco-electricity-bill", "sepco-peak-hour-charges-guide", "faq-about-sepco-online-bill", "sepco-online-bill-check"],
),
}
