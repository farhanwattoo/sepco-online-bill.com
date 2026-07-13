# Rewritten content for the 20 existing pages (unique, factual, task-focused).
from template import CTA_OFFICIAL, OFFICIAL

PAGES_A = {

"sepco-online-bill-check": dict(
    title="SEPCO Online Bill Check 2026 – View Your Bill Free",
    desc="Check your SEPCO bill online free with your 14-digit reference number on the official PITC portal. See the amount, due date, and download a copy.",
    h1="SEPCO Online Bill Check",
    intro="You can check any Sukkur Electric Power Company (SEPCO) bill online in under a minute. All you need is the 14-digit reference number printed on any previous bill — the official portal run by PITC shows the current amount, due date, and a printable copy free of charge.",
    body=f"""
{CTA_OFFICIAL}
<h2>Quick steps</h2>
<ol>
  <li>Find the <strong>14-digit reference number</strong> on any old SEPCO bill (top-left area of the printed bill).</li>
  <li>Open the official portal: <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</li>
  <li>Type the reference number without spaces or dashes and submit.</li>
  <li>Your bill appears on screen &mdash; check the <strong>payable amount within due date</strong> and the higher amount that applies after the due date.</li>
  <li>Use your browser's print or save-as-PDF option if you need a copy for payment at a bank.</li>
</ol>
<h2>What you can see online</h2>
<div class="table-wrap"><table>
<thead><tr><th>Detail</th><th>Where it appears</th></tr></thead>
<tbody>
<tr><td>Current month's payable amount</td><td>"Payable within due date" box</td></tr>
<tr><td>Amount after due date</td><td>"Payable after due date" box (includes late payment surcharge)</td></tr>
<tr><td>Due date</td><td>Top section, next to the bill month</td></tr>
<tr><td>Units consumed and meter readings</td><td>Reading block (previous / present reading)</td></tr>
<tr><td>12-month billing history</td><td>History table at the bottom of the bill</td></tr>
</tbody></table></div>
<h2>No printer? No problem</h2>
<p>Most bank branches, JazzCash and Easypaisa agents, and NADRA e-Sahulat shops only need the reference number to accept payment — you usually don't need the paper bill at all. If a branch insists on a printed copy, see our <a href="/how-to-print-sepco-duplicate-bill/">printing guide</a>.</p>
<p>If the portal says no record was found or rejects your number, our <a href="/common-sepco-bill-check-errors/">error troubleshooting guide</a> covers every common cause and fix.</p>
""",
    faqs=[
        ("Is checking a SEPCO bill online free?", "Yes. The official PITC portal is completely free with no registration or login. You only need the 14-digit reference number."),
        ("Can I check someone else's bill?", "Yes — the portal only asks for a reference number, so you can check a bill for a family member, tenant, or landlord if you have their number."),
        ("How early does the new bill appear online?", "The online bill is usually available a few days after meter reading, around the same time the paper bill is printed — typically in the first half of the month for most SEPCO subdivisions."),
    ],
    related=["how-to-check-sepco-bill-online", "where-to-find-sepco-reference-number", "sepco-duplicate-bill-guide", "common-sepco-bill-check-errors", "sepco-bill-payment-methods-guide", "sepco-tariff-rates-2026"],
),

"how-to-check-sepco-bill-online": dict(
    title="How to Check SEPCO Bill Online – Phone & PC Steps",
    desc="Detailed walkthrough for checking your SEPCO bill on a mobile phone or computer, including saving a PDF copy and what each field on the portal means.",
    h1="How to Check SEPCO Bill Online (Step by Step)",
    intro="This is the detailed version of the bill-check process — written for someone doing it for the first time on a phone or computer, including how to save a PDF copy and what to do at each screen.",
    body=f"""
<h2>Before you start</h2>
<p>Keep one thing ready: the <strong>14-digit reference number</strong>. It is printed on every SEPCO bill near the top-left, usually inside a row of boxes. It stays the same every month, so any old bill works. Lost every copy? See <a href="/where-to-find-sepco-reference-number/">five ways to recover your reference number</a>.</p>
<h2>On a mobile phone</h2>
<ol>
  <li>Open Chrome, Safari, or any browser and go to <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</li>
  <li>Tap the input box and type all 14 digits. Don't add spaces, dashes, or the customer ID by mistake — the portal needs the <em>reference</em> number.</li>
  <li>Submit. The full bill image loads on screen; pinch to zoom in on the amount and due date.</li>
  <li>To save a copy: open the browser menu and choose <strong>Share &rarr; Print &rarr; Save as PDF</strong> (Android) or <strong>Share &rarr; Print &rarr; pinch out on the preview &rarr; Save to Files</strong> (iPhone).</li>
</ol>
<h2>On a computer</h2>
<ol>
  <li>Visit the same portal address and enter the 14-digit number.</li>
  <li>When the bill loads, press <strong>Ctrl&nbsp;+&nbsp;P</strong> (or Cmd&nbsp;+&nbsp;P on Mac).</li>
  <li>Choose a connected printer to print, or select <strong>Save as PDF</strong> as the destination to keep a digital copy.</li>
</ol>
<h2>What to check once the bill loads</h2>
<ul>
  <li><strong>Bill month</strong> — make sure it's the current month, not an older cached copy.</li>
  <li><strong>Payable within due date</strong> — this is the amount to pay on time.</li>
  <li><strong>Units billed</strong> — compare with your own meter if the amount looks high; a jump can mean an estimated reading. The <a href="/apna-meter-apni-reading-sepco/">AMAR app</a> lets you submit your own reading.</li>
  <li><strong>FPA line</strong> — fuel price adjustment can add or subtract from the total; it changes monthly. <a href="/sepco-fuel-price-adjustment-fpa/">Here's how FPA works</a>.</li>
</ul>
{CTA_OFFICIAL}
""",
    faqs=[
        ("Do I need an account or password?", "No. The PITC portal has no login. Enter the reference number and the bill appears."),
        ("Why does the portal look different from screenshots I've seen?", "PITC updates the portal design occasionally, and some third-party sites imitate it. The address to trust is bill.pitc.com.pk — check the URL bar."),
        ("Can I check bills for past months?", "The portal shows the current bill, but its history table lists the amounts and payment status of roughly the last 12 months."),
    ],
    related=["sepco-online-bill-check", "sepco-online-bill-on-mobile", "how-to-download-duplicate-sepco-bill", "where-to-find-sepco-reference-number", "common-sepco-bill-check-errors", "how-to-read-a-sepco-electricity-bill"],
),

"sepco-duplicate-bill-guide": dict(
    title="SEPCO Duplicate Bill – Get a Copy Online or In Person",
    desc="How to get a SEPCO duplicate bill: free online copy from the PITC portal, or a stamped copy from your subdivision office. Where each version is accepted.",
    h1="SEPCO Duplicate Bill Guide",
    intro="A duplicate bill is simply a second copy of your monthly bill. If yours was lost, damaged, or never delivered, you can get a free copy online in a minute — or a stamped copy from your local SEPCO office if a bank demands an official version.",
    body=f"""
<h2>Option 1: Free online copy (fastest)</h2>
<p>Enter your 14-digit reference number at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> and the full bill appears, identical in content to the printed one. Print it or save it as a PDF. This is what most people mean by a "duplicate bill" and it's enough in almost every situation — see the acceptance table below.</p>
<h2>Option 2: Stamped copy from the subdivision office</h2>
<p>Visit your SEPCO subdivision (SDO) office with your CNIC and the reference number or old bill. Staff can print an official duplicate and stamp it. This is occasionally required for legal or property matters where a plain printout isn't accepted.</p>
<h2>Where each version is accepted</h2>
<div class="table-wrap"><table>
<thead><tr><th>Use</th><th>Online printout</th><th>Stamped office copy</th></tr></thead>
<tbody>
<tr><td>Paying at bank / ATM / mobile app</td><td>Accepted (often only the number is needed)</td><td>Accepted</td></tr>
<tr><td>JazzCash / Easypaisa / e-Sahulat</td><td>Not needed — reference number is enough</td><td>Not needed</td></tr>
<tr><td>Address proof for documents</td><td>Sometimes accepted</td><td>Preferred</td></tr>
<tr><td>Court / legal disputes</td><td>Usually not</td><td>Yes</td></tr>
</tbody></table></div>
<h2>Duplicate bill vs. correction</h2>
<p>A duplicate is a copy of the bill as issued — it doesn't fix wrong readings or amounts. If the bill itself is wrong (inflated units, wrong meter reading), you need a billing complaint instead: call <strong>118</strong> or visit the subdivision office. Our <a href="/sepco-helpline-complaint-numbers/">helpline guide</a> lists every contact route.</p>
""",
    faqs=[
        ("Does a duplicate bill cost anything?", "The online copy is free. Offices generally don't charge for a duplicate printout either."),
        ("Is the online duplicate valid for payment at a bank?", "Yes. Banks scan the barcode or type the reference number from your printout. Many branches can pull up the bill with just the number."),
        ("My bill never arrives — do I have to get a duplicate every month?", "You can, but a better fix is to report the delivery problem to your subdivision office and check the bill online each month meanwhile. See our guide on bills that don't arrive."),
    ],
    related=["how-to-download-duplicate-sepco-bill", "how-to-print-sepco-duplicate-bill", "sepco-bill-not-received-what-to-do", "sepco-online-bill-check", "where-to-find-sepco-reference-number", "sepco-helpline-complaint-numbers"],
),

"how-to-download-duplicate-sepco-bill": dict(
    title="Download SEPCO Duplicate Bill as PDF – All Devices",
    desc="Save your SEPCO duplicate bill as a PDF on Android, iPhone, or computer using the free official portal — with exact menu steps for each device.",
    h1="How to Download a Duplicate SEPCO Bill (PDF)",
    intro="The official portal doesn't have a download button, but every phone and computer can save the bill as a PDF through the print menu. Here are the exact steps for each device.",
    body=f"""
<h2>Android (Chrome)</h2>
<ol>
  <li>Open <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> and load your bill with the 14-digit reference number.</li>
  <li>Tap the <strong>&#8942; menu &rarr; Share &rarr; Print</strong>.</li>
  <li>At the printer dropdown choose <strong>Save as PDF</strong>, then tap the PDF button.</li>
  <li>The file lands in your <strong>Downloads</strong> folder.</li>
</ol>
<h2>iPhone (Safari)</h2>
<ol>
  <li>Load the bill, tap the <strong>Share</strong> icon, then <strong>Print</strong>.</li>
  <li>Pinch outward on the print preview — it becomes a PDF.</li>
  <li>Tap Share again and choose <strong>Save to Files</strong>.</li>
</ol>
<h2>Windows / Mac</h2>
<ol>
  <li>Load the bill and press <strong>Ctrl + P</strong> / <strong>Cmd + P</strong>.</li>
  <li>Set the destination to <strong>Save as PDF</strong> and save.</li>
</ol>
<h2>Tips for a clean copy</h2>
<ul>
  <li>Wait for the bill image to load fully before printing, otherwise the PDF may be blank.</li>
  <li>Enable <strong>background graphics</strong> in the print dialog if the bill looks washed out.</li>
  <li>Name files like <code>sepco-2026-07.pdf</code> so months are easy to find later — handy for tax records and tenancy disputes.</li>
</ul>
<p>Need a paper copy instead? See <a href="/how-to-print-sepco-duplicate-bill/">printing options</a>, including what to do if you don't own a printer.</p>
""",
    faqs=[
        ("Is there an official SEPCO app to download bills?", "PITC's Apna Meter Apni Reading (AMAR) app covers meter readings, and bills can be viewed through the web portal. For saving a monthly PDF, the browser method above is the reliable route."),
        ("The saved PDF is blank — why?", "The bill image hadn't finished loading when you printed. Reload the page, wait for the full bill to appear, then save again."),
        ("Can I download several months at once?", "No, the portal shows the current bill only. Save each month's PDF when it arrives if you need a running record."),
    ],
    related=["sepco-duplicate-bill-guide", "how-to-print-sepco-duplicate-bill", "sepco-online-bill-on-mobile", "sepco-online-bill-check", "how-to-check-sepco-bill-online", "apna-meter-apni-reading-sepco"],
),

"how-to-print-sepco-duplicate-bill": dict(
    title="Print SEPCO Duplicate Bill – Settings & No-Printer Options",
    desc="Print a SEPCO duplicate bill with the right settings (A4, portrait, background graphics), plus where to get it printed if you don't have a printer.",
    h1="How to Print a SEPCO Duplicate Bill",
    intro="Banks and offices accept a plain A4 printout of the online bill. Here are the settings that make the printout legible, and your options when there's no printer at home.",
    body=f"""
<h2>Print settings that work</h2>
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>Recommended value</th></tr></thead>
<tbody>
<tr><td>Paper size</td><td>A4</td></tr>
<tr><td>Orientation</td><td>Portrait</td></tr>
<tr><td>Scale</td><td>Fit to page (or 100%)</td></tr>
<tr><td>Background graphics</td><td>ON — otherwise shaded boxes and the barcode area may print faint</td></tr>
<tr><td>Color</td><td>Black &amp; white is fine; banks don't require color</td></tr>
</tbody></table></div>
<h2>Steps</h2>
<ol>
  <li>Load your bill at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> with your 14-digit reference number.</li>
  <li>Press <strong>Ctrl + P</strong> (computer) or use <strong>Share &rarr; Print</strong> (phone connected to a Wi-Fi printer).</li>
  <li>Apply the settings above and print. One page is normally enough — uncheck extra pages in the range if the preview shows two.</li>
</ol>
<h2>No printer at home?</h2>
<ul>
  <li><strong>Save a PDF first</strong> (<a href="/how-to-download-duplicate-sepco-bill/">steps here</a>) and take it on a USB drive or WhatsApp it to a local <strong>photocopy / composing shop</strong> — printing typically costs Rs 10–30.</li>
  <li><strong>Skip printing entirely:</strong> banks, JazzCash, Easypaisa, and e-Sahulat agents can process payment with just the reference number. A printout is rarely mandatory for payment.</li>
  <li>For a stamped official copy (legal use), your subdivision office prints it for you — see the <a href="/sepco-duplicate-bill-guide/">duplicate bill guide</a>.</li>
</ul>
""",
    faqs=[
        ("Will a bank accept a black-and-white printout?", "Yes. The cashier needs the reference number and amount, both fully readable in black and white."),
        ("The barcode didn't print — is the copy useless?", "No. Cashiers can type the reference number manually. Turning on background graphics usually fixes barcode printing."),
        ("Can I print after the due date?", "Yes, the bill stays online after the due date and shows the higher 'payable after due date' amount, which is what you'll pay."),
    ],
    related=["how-to-download-duplicate-sepco-bill", "sepco-duplicate-bill-guide", "sepco-bill-payment-methods-guide", "sepco-due-date-and-late-payment-guide", "sepco-online-bill-check", "common-sepco-bill-check-errors"],
),

"sepco-reference-number-guide": dict(
    title="SEPCO Reference Number – Format, Meaning & Uses",
    desc="The SEPCO reference number is a 14-digit code identifying your connection. Learn its structure, where it's printed, and when it changes.",
    h1="SEPCO Reference Number Guide",
    intro="The 14-digit reference number is the single most important number on your SEPCO bill — it identifies your connection for bill checking, payments, complaints, and the AMAR app. Here's how it's structured and everything it's used for.",
    body=f"""
<h2>What the 14 digits encode</h2>
<p>The reference number is assigned by PITC's billing system and encodes where your connection sits in SEPCO's network. Broadly, the leading digits identify your <strong>batch, subdivision and feeder area</strong>, and the remaining digits identify your <strong>individual connection</strong> within that area. Two neighbours on the same street usually share the same first several digits.</p>
<h2>Where it's printed</h2>
<p>On the paper bill it sits near the <strong>top-left</strong>, usually in a row of boxed digits labelled "Reference No". It also appears on bank payment receipts and in SMS confirmations from payment apps.</p>
<h2>What you use it for</h2>
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>How the reference number is used</th></tr></thead>
<tbody>
<tr><td>Checking the bill online</td><td>Only input the <a href="{OFFICIAL}" target="_blank" rel="noopener">official portal</a> asks for</td></tr>
<tr><td>Paying via JazzCash / Easypaisa / bank apps</td><td>Identifies the bill to fetch and pay</td></tr>
<tr><td>Registering a complaint</td><td>Quoted on calls to 118 and at SDO offices</td></tr>
<tr><td>Submitting your own meter reading</td><td>Links your AMAR app account to your meter</td></tr>
<tr><td>Applying for net metering or a load change</td><td>Identifies the existing connection</td></tr>
</tbody></table></div>
<h2>Does it ever change?</h2>
<p>It stays the same month after month. It can change if your connection is restructured — for example after a feeder reorganization, a meter replacement with re-registration, or converting the connection to a different tariff category. If your saved number suddenly returns "no record", pull the newest paper bill and check whether the number changed. More fixes in the <a href="/common-sepco-bill-check-errors/">errors guide</a>.</p>
<p>Not sure whether a number you have is the reference number or the customer ID? They're different lengths and used in different places — see <a href="/sepco-consumer-id-vs-reference-number/">consumer ID vs reference number</a>.</p>
""",
    faqs=[
        ("Is the reference number confidential?", "Treat it like semi-public information: anyone with it can view and pay your bill, but cannot change your connection or identity details with it alone."),
        ("I have two meters — do they share a reference number?", "No. Every meter/connection has its own 14-digit reference number and gets its own monthly bill."),
        ("Can I find my reference number by name or CNIC online?", "No. The public portal only searches by reference number. Your subdivision office can trace it from your address and CNIC."),
    ],
    related=["where-to-find-sepco-reference-number", "sepco-consumer-id-vs-reference-number", "sepco-online-bill-check", "apna-meter-apni-reading-sepco", "common-sepco-bill-check-errors", "how-to-read-a-sepco-electricity-bill"],
),

"where-to-find-sepco-reference-number": dict(
    title="Where to Find Your SEPCO Reference Number – 5 Ways",
    desc="Lost your SEPCO bill? Five ways to recover the 14-digit reference number: old bills, payment receipts, banking apps, neighbours, and the SDO office.",
    h1="Where to Find Your SEPCO Reference Number",
    intro="You can't check or pay a bill without the 14-digit reference number — and the portal has no search by name or CNIC. If every paper bill is lost, work through these five recovery routes, fastest first.",
    body="""
<h2>1. Any old paper bill</h2>
<p>The number never changes month to month, so even a years-old bill works. Look at the top-left of the bill for a row of 14 boxed digits labelled <strong>Reference No</strong>. Don't confuse it with the 10-digit customer/consumer ID printed nearby.</p>
<h2>2. Old payment receipts and SMS</h2>
<p>Bank counter receipts, ATM slips, and the confirmation SMS from JazzCash/Easypaisa all contain the reference number of the bill that was paid. Search your SMS history for "SEPCO" or the amount you remember paying.</p>
<h2>3. Your banking or wallet app history</h2>
<p>If you've ever paid the bill through a mobile banking app, JazzCash, or Easypaisa, open the app's <strong>transaction history</strong> — the saved biller entry shows the full reference number, and most apps let you save it as a favourite for next time.</p>
<h2>4. A neighbour's bill (to locate your own)</h2>
<p>A neighbour on the same street can't give you your number, but their bill tells you your <strong>subdivision and feeder</strong>, which makes tracing your connection at the office much faster.</p>
<h2>5. Your SEPCO subdivision (SDO) office</h2>
<p>Take your <strong>CNIC</strong> and proof of the address (any utility document or the meter number written down from the meter itself). Office staff can trace the connection in the billing system and give you the reference number. If the connection is in a previous owner's or landlord's name, you can still get the number — the bill follows the premises, not the occupant.</p>
<div class="notice">Tip: once recovered, save the number in your phone contacts (e.g. as "SEPCO home bill") and as a saved biller in your payment app so this never happens again.</div>
""",
    faqs=[
        ("Can SEPCO's helpline 118 tell me my reference number?", "118 is primarily for outage and billing complaints. Agents can sometimes help trace a connection, but the subdivision office is the reliable route for number recovery."),
        ("Is the meter number the same as the reference number?", "No. The meter number identifies the physical device and is stamped on the meter; the reference number identifies your billing account. Offices can look up one from the other."),
        ("The property just changed hands — does the old reference number still work?", "Yes, the number stays with the connection. Name transfer is a separate process at the subdivision office and doesn't stop you from checking or paying the bill."),
    ],
    related=["sepco-reference-number-guide", "sepco-consumer-id-vs-reference-number", "sepco-online-bill-check", "sepco-helpline-complaint-numbers", "sepco-duplicate-bill-guide", "sepco-bill-not-received-what-to-do"],
),

"sepco-consumer-id-vs-reference-number": dict(
    title="SEPCO Consumer ID vs Reference Number – The Difference",
    desc="SEPCO bills carry a 10-digit consumer ID and a 14-digit reference number. What each identifies, where each is used, and which one payment apps need.",
    h1="SEPCO Consumer ID vs Reference Number",
    intro="SEPCO bills carry two identifying numbers, and entering the wrong one is the most common reason a bill check fails. The short answer: the 14-digit reference number is what you need for the portal and payment apps; the 10-digit consumer ID is mainly an internal account identifier.",
    body="""
<h2>Side-by-side comparison</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Reference number</th><th>Consumer / customer ID</th></tr></thead>
<tbody>
<tr><td>Length</td><td><strong>14 digits</strong></td><td><strong>10 digits</strong></td></tr>
<tr><td>Identifies</td><td>Your connection's place in the billing system (subdivision, feeder, connection)</td><td>Your customer account record</td></tr>
<tr><td>Bill check portal</td><td>Required</td><td>Not accepted on the SEPCO portal</td></tr>
<tr><td>JazzCash / Easypaisa / bank apps</td><td>Required</td><td>Not used</td></tr>
<tr><td>Complaints and office work</td><td>Accepted</td><td>Accepted</td></tr>
<tr><td>Changes over time?</td><td>Only if the connection is restructured</td><td>Stable</td></tr>
</tbody></table></div>
<h2>How to tell them apart on the bill</h2>
<p>Both are printed in the top section of the bill. Count the digits: fourteen boxed digits is the reference number; the ten-digit number labelled "Consumer ID" or "Customer ID" is the account identifier. Payment receipts echo the reference number, not the consumer ID.</p>
<h2>Why some other DISCO portals confuse people</h2>
<p>A few distribution companies (and many unofficial bill sites) accept either number, so guides written for other regions often say "enter your customer ID". For SEPCO's official PITC portal, use the <strong>14-digit reference number</strong> — a 10-digit entry simply returns no result. If you only know the consumer ID, your subdivision office can look up the matching reference number in a minute.</p>
""",
    faqs=[
        ("I entered 10 digits and got 'no record found' — is my connection deleted?", "No. The portal needs the 14-digit reference number; a 10-digit consumer ID will never match. Find the longer number on your bill and retry."),
        ("Do I ever actually need the consumer ID?", "Occasionally at the subdivision office for account-level work such as name transfer, load change, or tariff category corrections."),
        ("Are these the same as the meter number?", "No — the meter number is a third identifier, stamped on the physical meter. It matters for meter replacement and theft complaints, not for bill checking."),
    ],
    related=["sepco-reference-number-guide", "where-to-find-sepco-reference-number", "sepco-bill-check-by-customer-id", "sepco-bill-check-by-meter-number", "common-sepco-bill-check-errors", "sepco-online-bill-check"],
),

"how-to-read-a-sepco-electricity-bill": dict(
    title="How to Read a SEPCO Electricity Bill – Every Section",
    desc="A section-by-section tour of the SEPCO bill: meter readings, units, tariff, charges block, taxes, 12-month history, and the two payable amounts.",
    h1="How to Read a SEPCO Electricity Bill",
    intro="A SEPCO bill packs about thirty fields onto one page. This guide walks through each block in the order it appears, so you can verify the bill instead of just paying it.",
    body="""
<h2>1. Identity block (top)</h2>
<ul>
  <li><strong>Reference number (14 digits)</strong> and <strong>consumer ID (10 digits)</strong> — your connection and account identifiers.</li>
  <li><strong>Name and address</strong> — the registered connection holder (often a previous owner in older properties; the bill is still valid).</li>
  <li><strong>Tariff</strong> — e.g. A-1 for domestic. This decides which slab rates apply. See <a href="/sepco-tariff-rates-2026/">current tariff rates</a>.</li>
  <li><strong>Connected load and meter number.</strong></li>
</ul>
<h2>2. Reading block</h2>
<ul>
  <li><strong>Previous / present reading</strong> — the meter's cumulative figure at the last two readings.</li>
  <li><strong>MF (multiplying factor)</strong> — almost always 1 for homes. Units billed = (present − previous) × MF.</li>
  <li><strong>Units consumed</strong> — the number everything else is built on. If it doesn't match your own meter check, the reading may be estimated — our <a href="/apna-meter-apni-reading-sepco/">AMAR app guide</a> shows how to submit your own reading.</li>
</ul>
<h2>3. Charges block</h2>
<p>Line items typically include the energy charge (units × slab rate), FC surcharge, fuel price adjustment (FPA), quarterly tariff adjustment (QTA), and a fixed charge for higher-usage domestic consumers. Each is explained in <a href="/sepco-bill-charges-explained/">bill charges explained</a>.</p>
<h2>4. Taxes block</h2>
<p>GST, electricity duty, the Rs 35 TV licence fee, and (for some consumers) advance income tax. Details and current percentages: <a href="/sepco-bill-taxes-explained/">bill taxes explained</a>.</p>
<h2>5. The two payable amounts</h2>
<p><strong>Payable within due date</strong> is the normal total. <strong>Payable after due date</strong> adds the late payment surcharge. The due date sits beside the bill month — more on consequences in the <a href="/sepco-due-date-and-late-payment-guide/">due date guide</a>.</p>
<h2>6. Billing history table (bottom)</h2>
<p>Around 12 months of past units, amounts, and payment status. Use it to spot unusual months — a sudden spike with no season change often means an estimated or wrong reading, worth a complaint before paying.</p>
""",
    faqs=[
        ("What does 'ESTIMATED' or a jump in units mean?", "When a meter reader can't access the meter, the system bills an estimate based on past usage. The next actual reading self-corrects, but you can also complain at 118 or submit your own readings via the AMAR app."),
        ("Why is the name on the bill not mine?", "Connections often stay registered to a previous owner. Payment is valid regardless; name transfer is an optional process at your subdivision office with ownership documents."),
        ("What is the barcode for?", "Bank and agent systems scan it to pull the bill instantly. If it doesn't scan, the cashier types your 14-digit reference number instead."),
    ],
    related=["sepco-bill-charges-explained", "sepco-bill-taxes-explained", "sepco-bill-units-meaning", "sepco-tariff-rates-2026", "sepco-due-date-and-late-payment-guide", "apna-meter-apni-reading-sepco"],
),

"sepco-bill-charges-explained": dict(
    title="SEPCO Bill Charges Explained – Every Line Item",
    desc="What each charge on a SEPCO bill means: energy charge, FC surcharge, FPA, quarterly adjustment, fixed charges and late payment surcharge.",
    h1="SEPCO Bill Charges Explained",
    intro="The charges block is where your money actually goes. Here is every recurring line item on a domestic SEPCO bill, what drives it, and which ones you can influence.",
    body="""
<h2>The line items</h2>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>What it is</th><th>Can you reduce it?</th></tr></thead>
<tbody>
<tr><td><strong>Energy charge</strong></td><td>Units × your slab rate. The largest item on almost every bill.</td><td>Yes — fewer units, lower slab. See <a href="/how-to-reduce-sepco-electricity-bill/">reduction guide</a>.</td></tr>
<tr><td><strong>FC surcharge</strong></td><td>Financing cost surcharge, Rs 3.23 per unit, levied nationally to service power-sector debt.</td><td>Only by using fewer units.</td></tr>
<tr><td><strong>FPA</strong></td><td>Fuel price adjustment — monthly correction for actual generation fuel costs, can be positive or negative. <a href="/sepco-fuel-price-adjustment-fpa/">Full FPA guide</a>.</td><td>No, but protected consumers are shielded from much of it.</td></tr>
<tr><td><strong>QTA</strong></td><td>Quarterly tariff adjustment approved by NEPRA to true-up DISCO revenues.</td><td>No.</td></tr>
<tr><td><strong>Fixed charge</strong></td><td>Flat monthly amount for domestic consumers above 300 units (Rs 200–1,000 by slab).</td><td>Yes — stay at or under 300 units.</td></tr>
<tr><td><strong>LPS (late payment surcharge)</strong></td><td>Penalty added if you pay after the due date — the difference between the two payable amounts printed on the bill.</td><td>Yes — pay on time. <a href="/sepco-due-date-and-late-payment-guide/">Due date guide</a>.</td></tr>
</tbody></table></div>
<h2>Why the same units can cost more some months</h2>
<ul>
  <li><strong>Slab crossing:</strong> going from 200 to 210 units moves you off protected rates entirely — the single most expensive threshold on the bill. See <a href="/sepco-protected-vs-unprotected-tariff/">protected vs non-protected</a>.</li>
  <li><strong>FPA swings:</strong> a hot month with expensive imported fuel can add several rupees per unit two months later.</li>
  <li><strong>Seasonal surcharges:</strong> NEPRA approved an additional surcharge of Rs 3.82/unit for March–June 2026, which shows up inside the surcharge lines.</li>
</ul>
<p>To sanity-check any bill, run your units through our <a href="/sepco-bill-estimate-calculator-guide/">slab calculator</a> — if the printed energy charge differs a lot from the estimate, look for estimated readings or a slab change.</p>
""",
    faqs=[
        ("Which charges are set by SEPCO itself?", "None independently. Rates, surcharges, and adjustments are set or approved by NEPRA for all distribution companies; SEPCO applies them to your metered units."),
        ("What's the difference between FPA and QTA?", "FPA corrects for last month's actual fuel cost and changes every month. QTA is a quarterly true-up of overall revenue requirements. Both appear as separate lines."),
        ("Why do I pay a fixed charge some months only?", "The domestic fixed charge applies only when your billed units exceed 300 in that month, and its amount steps up with the slab."),
    ],
    related=["sepco-bill-taxes-explained", "sepco-fuel-price-adjustment-fpa", "sepco-tariff-rates-2026", "sepco-protected-vs-unprotected-tariff", "sepco-bill-estimate-calculator-guide", "how-to-reduce-sepco-electricity-bill"],
),

"sepco-bill-taxes-explained": dict(
    title="SEPCO Bill Taxes Explained – GST, Duty, TV Fee & More",
    desc="Taxes on a SEPCO bill explained: 18% GST, 1.5% electricity duty, Rs 35 TV licence fee, and advance income tax — plus who is exempt.",
    h1="SEPCO Bill Taxes Explained",
    intro="Taxes can add roughly a fifth on top of the electricity charges for non-protected consumers. Here's each tax on the SEPCO bill, its current rate, and who doesn't have to pay it.",
    body="""
<h2>The four taxes on a domestic bill</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tax</th><th>Rate</th><th>Applied to</th><th>Exemptions</th></tr></thead>
<tbody>
<tr><td><strong>GST (sales tax)</strong></td><td>18%</td><td>Electricity charges including surcharges and duty</td><td>Lifeline and protected domestic consumers are largely exempt</td></tr>
<tr><td><strong>Electricity duty</strong></td><td>~1.5%</td><td>Variable charges; collected for the provincial government (Sindh)</td><td>Applies to most consumers</td></tr>
<tr><td><strong>TV licence fee</strong></td><td>Rs 35 flat</td><td>Every domestic bill, collected for PTV</td><td>Can be removed only by declaring no TV at the subdivision office</td></tr>
<tr><td><strong>Advance income tax</strong></td><td>7.5% for non-filers</td><td>Domestic bills above Rs 25,000/month</td><td>Tax filers (listed on FBR's Active Taxpayer List) are not charged at the domestic level</td></tr>
</tbody></table></div>
<h2>Worked example (non-protected, 300 units)</h2>
<p>Suppose energy + surcharges come to about Rs 10,000. Electricity duty adds ~Rs 150. GST at 18% on roughly the sum adds ~Rs 1,830. With the Rs 35 TV fee, taxes total about Rs 2,000 — around 20% on top. Run your own numbers in the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a>.</p>
<h2>How to legally pay less tax</h2>
<ul>
  <li><strong>Stay protected:</strong> keeping 6-month usage at or under 200 units avoids most GST — the combined savings of lower rates plus tax exemption are dramatic. <a href="/sepco-protected-vs-unprotected-tariff/">How the 200-unit rule works</a>.</li>
  <li><strong>Become a filer</strong> if your bills cross Rs 25,000 — the 7.5% advance income tax on large domestic bills only hits non-filers (filers can also claim adjustments).</li>
  <li><strong>No TV?</strong> You can apply at the subdivision office to remove the Rs 35 PTV fee, though the paperwork often outweighs the saving.</li>
</ul>
""",
    faqs=[
        ("Why am I paying income tax on an electricity bill?", "FBR collects advance income tax through utility bills as a documentation measure. On domestic connections it applies only when the monthly bill exceeds Rs 25,000 and the account holder isn't on the Active Taxpayer List."),
        ("Is GST charged on the FPA line too?", "Yes — sales tax applies to the variable electricity charges including adjustments, which is why a high-FPA month raises the tax lines as well."),
        ("Do protected consumers pay any tax at all?", "They pay the TV fee and duty, but are spared GST and (given small bills) income tax — one more reason the protected category is worth keeping."),
    ],
    related=["sepco-bill-charges-explained", "sepco-tariff-rates-2026", "sepco-protected-vs-unprotected-tariff", "sepco-fuel-price-adjustment-fpa", "sepco-bill-estimate-calculator-guide", "how-to-read-a-sepco-electricity-bill"],
),

"sepco-bill-units-meaning": dict(
    title="SEPCO Bill Units Meaning – kWh, Readings & Slabs",
    desc="What 'units' on a SEPCO bill actually are (kWh), how they're read from your meter, how slab pricing works, and what common appliances consume.",
    h1="What Do the Units on a SEPCO Bill Mean?",
    intro="One unit is one kilowatt-hour (kWh) — the energy a 1,000-watt appliance uses in one hour. Everything on your bill is built on the month's unit count, so understanding units is understanding the bill.",
    body="""
<h2>From meter to bill</h2>
<p>Your meter counts cumulative kWh. Each month the reader photographs the display, and the system subtracts last month's figure: <strong>present reading − previous reading = units billed</strong> (× a multiplying factor, which is 1 for homes). Both readings are printed in the bill's reading block, so you can verify against the meter yourself.</p>
<h2>Why the 201st unit is so expensive</h2>
<p>Units are priced in slabs, and two rules matter:</p>
<ul>
  <li><strong>One-slab benefit:</strong> if you land in a slab, units up to the previous slab's ceiling are charged at the previous rate and only the remainder at your slab's rate.</li>
  <li><strong>The 200-unit protection cliff:</strong> average more than 200 units over six months and every unit — including the first hundred — switches from protected rates (Rs 10.54–13.01) to non-protected rates (Rs 22.44+). Details: <a href="/sepco-protected-vs-unprotected-tariff/">protected vs non-protected</a>.</li>
</ul>
<p>Current rates for every slab are in the <a href="/sepco-tariff-rates-2026/">2026 tariff table</a>.</p>
<h2>What appliances consume (approximate)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Appliance</th><th>Typical draw</th><th>Units per month (typical use)</th></tr></thead>
<tbody>
<tr><td>1.5-ton inverter AC</td><td>0.9–1.8 kW</td><td>150–300 (8 h/day in summer)</td></tr>
<tr><td>Old non-inverter AC (1.5-ton)</td><td>~2 kW</td><td>300–450</td></tr>
<tr><td>Ceiling fan</td><td>60–100 W</td><td>15–25 each</td></tr>
<tr><td>Refrigerator (medium)</td><td>100–200 W avg</td><td>40–75</td></tr>
<tr><td>LED bulb (12 W)</td><td>12 W</td><td>2–3 each</td></tr>
<tr><td>Washing machine</td><td>350–500 W</td><td>5–15</td></tr>
<tr><td>Water pump (1 hp)</td><td>~750 W</td><td>20–45</td></tr>
</tbody></table></div>
<p>Add your own appliances up and compare with the billed units — a big mismatch suggests an estimated reading or meter issue. You can submit your own reading with the <a href="/apna-meter-apni-reading-sepco/">AMAR app</a>, and cut usage with the <a href="/how-to-reduce-sepco-electricity-bill/">bill reduction guide</a>.</p>
""",
    faqs=[
        ("My meter shows more digits than the bill reading — why?", "Bills often drop the decimal (red) digits and sometimes leading zeros. Compare whole-number kWh digits only."),
        ("Do units expire or carry over?", "No. Billing is purely consumption between two readings. There's no carry-over — except under net metering, where exported solar units offset within the billing rules."),
        ("How many units does a typical small house use?", "A 2–3 room home with fans, LED lights, a fridge and a TV typically lands between 150 and 250 units — right around the protection threshold, which is why summer AC use often flips households into the expensive category."),
    ],
    related=["sepco-tariff-rates-2026", "sepco-protected-vs-unprotected-tariff", "how-to-reduce-sepco-electricity-bill", "apna-meter-apni-reading-sepco", "sepco-bill-charges-explained", "sepco-bill-estimate-calculator-guide"],
),

"sepco-due-date-and-late-payment-guide": dict(
    title="SEPCO Due Date & Late Payment – Surcharge and Rules",
    desc="What happens after the SEPCO due date: late payment surcharge, where to pay an overdue bill, disconnection timelines, and installment options.",
    h1="SEPCO Due Date and Late Payment Guide",
    intro="Missing the due date costs you the late payment surcharge immediately — and eventually risks disconnection. Here's exactly what happens when, and your options if you can't pay on time.",
    body="""
<h2>The two amounts on your bill</h2>
<p>Every bill prints <strong>payable within due date</strong> and <strong>payable after due date</strong>. The difference is the late payment surcharge (LPS) — for domestic consumers roughly 10% of the bill amount. The due date is typically 10–14 days after the bill issue date.</p>
<h2>Paying after the due date</h2>
<ul>
  <li>The online portal and payment apps automatically show/collect the after-due-date amount once the date passes.</li>
  <li>Banks accept overdue bills — you don't need a new bill issued, just pay the higher printed amount.</li>
  <li>If the bill is <em>very</em> old (a previous month's bill superseded by a new one), pay the newest bill, which rolls the arrears forward with the surcharge under "arrears".</li>
</ul>
<h2>Disconnection: the actual timeline</h2>
<p>Under NEPRA's consumer service rules, a connection can be disconnected after the due date passes on a bill containing arrears, but in practice SEPCO issues the next bill with arrears first and field disconnection usually follows continued non-payment. Reconnection requires paying the outstanding amount plus a reconnection fee at the subdivision office — same-day to a few days for restoration.</p>
<h2>Can't pay the full amount?</h2>
<ul>
  <li><strong>Installments:</strong> for large accumulated bills, subdivision offices (SDO/XEN) can approve splitting the amount across future bills. Take your CNIC and the bill; approval is discretionary.</li>
  <li><strong>Bill correction pending?</strong> If you've filed a complaint about a wrong bill, ask the office for a corrected/provisional bill <em>before</em> the due date rather than withholding payment — unpaid disputed bills still accrue surcharge until corrected.</li>
</ul>
<div class="notice">Set a monthly reminder 2–3 days before your usual due date and pay from your phone — the <a href="/pay-sepco-bill-jazzcash-easypaisa/">JazzCash/Easypaisa guide</a> takes under two minutes.</div>
""",
    faqs=[
        ("Is the late surcharge charged per day?", "No — it's a one-time addition printed on the bill. But if the unpaid amount rolls into the next bill as arrears, further surcharge applies to the new total."),
        ("The due date fell on a holiday — can I pay the normal amount the next day?", "Banks generally accept the within-due-date amount on the next working day after a gazetted holiday. Digital channels apply the printed dates automatically, so pay a day early to be safe."),
        ("Does late payment affect my protected status?", "No. Protected/non-protected status depends only on your units consumed, not payment behaviour."),
    ],
    related=["sepco-bill-payment-methods-guide", "pay-sepco-bill-jazzcash-easypaisa", "sepco-bill-charges-explained", "sepco-online-bill-check", "sepco-helpline-complaint-numbers", "sepco-bill-not-received-what-to-do"],
),

"sepco-bill-payment-methods-guide": dict(
    title="SEPCO Bill Payment Methods 2026 – All Options Compared",
    desc="Every way to pay a SEPCO bill in 2026: bank branches, ATMs, mobile banking, JazzCash, Easypaisa, 1Bill, Pakistan Post and NADRA e-Sahulat.",
    h1="SEPCO Bill Payment Methods",
    intro="You never need to stand in one specific bank's line — SEPCO bills can be paid through more than a dozen channels, most of them free and instant. Here's the full menu with the practical trade-offs.",
    body="""
<h2>All payment channels</h2>
<div class="table-wrap"><table>
<thead><tr><th>Channel</th><th>What you need</th><th>Fee</th><th>Notes</th></tr></thead>
<tbody>
<tr><td><strong>JazzCash / Easypaisa app</strong></td><td>Reference number</td><td>Free</td><td>Fastest; instant confirmation. <a href="/pay-sepco-bill-jazzcash-easypaisa/">Step-by-step guide</a>.</td></tr>
<tr><td><strong>Mobile/internet banking</strong> (HBL, UBL, MCB, ABL, Meezan, etc.)</td><td>Reference number (via 1Bill/1Link utility biller)</td><td>Free</td><td>Save SEPCO as a biller once; pay in seconds monthly.</td></tr>
<tr><td><strong>Bank branch counter</strong></td><td>Printed bill (or reference number)</td><td>Free</td><td>Cash accepted; long queues near due date.</td></tr>
<tr><td><strong>ATM bill payment</strong></td><td>Bank card + reference number</td><td>Free</td><td>Works outside banking hours.</td></tr>
<tr><td><strong>JazzCash / Easypaisa agent shop</strong></td><td>Reference number + cash</td><td>Free/small agent fee</td><td>Good for those without smartphones or accounts.</td></tr>
<tr><td><strong>NADRA e-Sahulat franchise</strong></td><td>Reference number + cash</td><td>Small fee (~Rs 10–20)</td><td>Widely available in small towns.</td></tr>
<tr><td><strong>Pakistan Post</strong></td><td>Printed bill + cash</td><td>Free</td><td>Useful where banks are far.</td></tr>
</tbody></table></div>
<h2>When is the payment reflected?</h2>
<p>Digital payments are confirmed instantly by SMS/receipt, but the "PAID" status can take 1–2 working days to sync into the billing system. Keep the transaction ID until the next bill shows the payment. If a paid amount appears as arrears on the next bill, take the receipt to your subdivision office or call 118.</p>
<h2>Recurring trick: save the biller</h2>
<p>In any bank or wallet app, save your 14-digit reference number as a favourite biller. Each month the app fetches the current amount automatically — no bill copy needed. Combine this with a reminder before the <a href="/sepco-due-date-and-late-payment-guide/">due date</a> and you'll never pay the surcharge again.</p>
""",
    faqs=[
        ("Can I pay a SEPCO bill from another city or abroad?", "Yes. Any Pakistani mobile banking app can pay it from anywhere; overseas family members with Pakistani accounts (or Roshan Digital Accounts) can pay for relatives using just the reference number."),
        ("Can I pay in installments through an app?", "No — apps collect the full billed amount. Installment plans for large arrears are arranged at the subdivision office."),
        ("Is partial payment possible?", "Counters and apps collect the exact billed amount. For partial/advance arrangements you need the subdivision office."),
    ],
    related=["pay-sepco-bill-jazzcash-easypaisa", "sepco-due-date-and-late-payment-guide", "sepco-online-bill-check", "sepco-duplicate-bill-guide", "sepco-helpline-complaint-numbers", "faq-about-sepco-online-bill"],
),

"sepco-peak-hour-charges-guide": dict(
    title="SEPCO Peak Hours 2026 – ToU Timings & Rates",
    desc="SEPCO time-of-use (ToU) peak hour timings by season, how peak vs off-peak rates work, and how shifting load can cut your bill.",
    h1="SEPCO Peak Hour Charges Guide",
    intro="If your connection has a time-of-use (ToU) meter, electricity used during the evening peak window costs significantly more than off-peak. Knowing the window — and moving heavy loads out of it — is one of the easiest real savings available.",
    body="""
<h2>Who has ToU billing?</h2>
<p>ToU applies to connections with ToU (multi-register) meters — mandatory for larger loads (5 kW and above, including many commercial, industrial, and some domestic consumers). Ordinary single-register domestic meters bill everything at slab rates with no peak distinction. Your bill shows separate <strong>peak</strong> and <strong>off-peak</strong> unit lines if ToU applies to you.</p>
<h2>Peak hour timings by season</h2>
<div class="table-wrap"><table>
<thead><tr><th>Season</th><th>Peak hours (typical NEPRA schedule)</th></tr></thead>
<tbody>
<tr><td>December – February</td><td>5:00 pm – 9:00 pm</td></tr>
<tr><td>March – May</td><td>6:00 pm – 10:00 pm</td></tr>
<tr><td>June – August</td><td>7:00 pm – 11:00 pm</td></tr>
<tr><td>September – November</td><td>6:00 pm – 10:00 pm</td></tr>
</tbody></table></div>
<p class="text-muted">Exact windows are set in the NEPRA tariff schedule and printed on ToU bills — confirm the window shown on your own bill.</p>
<h2>How the rates differ</h2>
<p>Under the FY 2025-26 schedule, the domestic ToU peak rate sits several rupees above the off-peak rate (peak is broadly comparable to the top flat slabs, off-peak meaningfully cheaper). The exact figures are in the <a href="/sepco-tariff-rates-2026/">tariff table</a>. The four peak hours are only ~17% of the day — but for many households they contain the AC, iron, washing machine, and motor use.</p>
<h2>Practical load-shifting</h2>
<ul>
  <li>Run the <strong>washing machine, iron, and water pump</strong> in the morning or after the peak window.</li>
  <li>Pre-cool bedrooms with the AC an hour before peak starts, then raise the thermostat during peak.</li>
  <li>Charge UPS/batteries and EVs off-peak (overnight is cheapest and coolest).</li>
  <li>If you're considering solar, peak-evening pricing strengthens the case for battery storage — see the <a href="/sepco-net-metering-guide-2026/">2026 net metering guide</a>.</li>
</ul>
""",
    faqs=[
        ("I have a normal domestic meter — do peak hours affect me?", "Not directly on billing. Slab rates apply regardless of time. But reducing evening load still helps the grid and prepares you if you later move to a ToU or solar setup."),
        ("Are peak timings the same across Pakistan?", "The seasonal structure is set nationally by NEPRA and shared by DISCOs, with the schedule printed in tariff notifications. Always confirm the window printed on your own bill."),
        ("Is Friday or Sunday exempt from peak billing?", "No — ToU peak windows apply every day of the week."),
    ],
    related=["sepco-tariff-rates-2026", "how-to-reduce-sepco-electricity-bill", "sepco-bill-units-meaning", "sepco-net-metering-guide-2026", "sepco-bill-charges-explained", "sepco-bill-estimate-calculator-guide"],
),

"sepco-bill-estimate-calculator-guide": dict(
    title="SEPCO Bill Calculator 2026 – Estimate From Units",
    desc="Estimate your SEPCO bill from units with FY 2025-26 slab rates — including surcharges, duty, GST and TV fee — and see exactly how it's calculated.",
    h1="SEPCO Bill Calculator (FY 2025-26 Rates)",
    intro="Enter your units below and get a line-by-line estimate built on the current NEPRA-notified slab rates — the same math your printed bill uses, minus the month-specific adjustments.",
    tool=True,
    body="""
<h2>How the estimate is calculated</h2>
<ol>
  <li><strong>Energy charge:</strong> your units are priced through the FY 2025-26 slabs with the one-previous-slab benefit (units up to the previous slab ceiling at the previous rate, the rest at your slab rate).</li>
  <li><strong>FC surcharge:</strong> Rs 3.23 per unit for non-protected consumers.</li>
  <li><strong>Fixed charge:</strong> Rs 200–1,000/month for domestic consumers above 300 units.</li>
  <li><strong>Electricity duty (~1.5%)</strong> on variable charges, then <strong>GST (18%)</strong> for non-protected consumers, plus the <strong>Rs 35 TV fee</strong>.</li>
  <li><strong>FPA:</strong> if you enter the Rs/unit fuel price adjustment from your latest bill, it's included; otherwise the estimate excludes it.</li>
</ol>
<h2>Worked example: 245 units, non-protected</h2>
<p>200 units × Rs 28.92 + 45 units × Rs 33.10 ≈ Rs 7,274 energy charge. Add FC surcharge (245 × 3.23 ≈ Rs 791), duty ≈ Rs 121, GST ≈ Rs 1,474, TV fee Rs 35 → estimated total ≈ <strong>Rs 9,700</strong> before FPA/QTA. The same house at 195 units on protected rates would pay barely Rs 2,800 — the <a href="/sepco-protected-vs-unprotected-tariff/">200-unit rule</a> is that consequential.</p>
<h2>Why your printed bill will differ slightly</h2>
<ul>
  <li><strong>FPA and QTA</strong> change monthly/quarterly and can move the total by hundreds of rupees either way.</li>
  <li><strong>Seasonal surcharges</strong> (e.g. the Rs 3.82/unit surcharge for March–June 2026) appear in some months.</li>
  <li><strong>Arrears, installments, or subsidies</strong> specific to your account.</li>
</ul>
<p>For the actual payable amount, always check the official portal — this tool is for planning and sanity-checking. Full rate tables: <a href="/sepco-tariff-rates-2026/">SEPCO tariff 2026</a>.</p>
""",
    faqs=[
        ("Which category should I pick in the calculator?", "If your average over the last six months is 200 units or less, pick protected. If any doubt, check a recent bill — it prints your tariff/category. Lifeline applies only up to 100 units with very low usage history."),
        ("Why is my estimate lower than the actual bill?", "Most often: FPA/QTA lines you didn't enter, the March–June 2026 surcharge, or arrears from a previous month included in the printed total."),
        ("Does the calculator send my data anywhere?", "No — it runs entirely in your browser. Nothing you type is uploaded or stored."),
    ],
    related=["sepco-tariff-rates-2026", "sepco-bill-charges-explained", "sepco-bill-taxes-explained", "sepco-protected-vs-unprotected-tariff", "sepco-bill-units-meaning", "how-to-reduce-sepco-electricity-bill"],
),

"sepco-bill-not-received-what-to-do": dict(
    title="SEPCO Bill Not Received? Do This Before the Due Date",
    desc="Paper bill didn't arrive? Check and pay it online in minutes, then fix delivery permanently — plus what happens if you simply don't pay.",
    h1="SEPCO Bill Not Received — What to Do",
    intro="A missing paper bill doesn't pause the due date or the late surcharge. Here's the immediate fix (two minutes, online), and how to stop the problem recurring.",
    body=f"""
<h2>Right now: get the bill online</h2>
<ol>
  <li>Find your 14-digit reference number from any old bill or payment SMS (<a href="/where-to-find-sepco-reference-number/">recovery options</a>).</li>
  <li>Check the current amount and due date at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</li>
  <li>Pay via your bank app, JazzCash, or Easypaisa using the reference number — no paper needed (<a href="/pay-sepco-bill-jazzcash-easypaisa/">steps</a>). Print a copy only if you want to pay at a counter (<a href="/how-to-print-sepco-duplicate-bill/">printing guide</a>).</li>
</ol>
<h2>Fix delivery permanently</h2>
<ul>
  <li><strong>Report it:</strong> call <strong>118</strong> or visit your subdivision office with the reference number. Repeated non-delivery is usually a distribution-round problem the office can correct.</li>
  <li><strong>Check the address on record:</strong> if the printed address is outdated or vague (common in newly built areas), have it corrected at the office.</li>
  <li><strong>Go self-serve:</strong> make a habit of checking online at the start of each month, or use the <a href="/apna-meter-apni-reading-sepco/">AMAR app</a> — submitting your own reading also means you know your bill before it's even printed.</li>
</ul>
<h2>What if a bill goes unpaid because it never arrived?</h2>
<p>Unfortunately non-delivery doesn't waive the late surcharge — the amount rolls into the next bill as arrears with LPS added. If you can show a pattern of non-delivery, the subdivision office can sometimes reverse a surcharge as a goodwill correction, but prevention (online checking) is far more reliable than the remedy.</p>
""",
    faqs=[
        ("Can I get my bill by SMS or email instead?", "PITC has piloted e-bill services for various DISCOs. Availability for SEPCO changes over time — ask at your subdivision office. Meanwhile the portal plus a monthly phone reminder covers the same need."),
        ("My whole street didn't get bills this month — what does that mean?", "Usually a delayed printing/distribution batch. The bills are still generated on schedule — check online; due dates apply regardless."),
        ("The bill arrives after the due date every month. Is that even allowed?", "You're entitled to a reasonable payment window. Document the arrival dates and complain to the subdivision office; meanwhile pay online by the printed due date to avoid surcharges."),
    ],
    related=["sepco-online-bill-check", "where-to-find-sepco-reference-number", "pay-sepco-bill-jazzcash-easypaisa", "apna-meter-apni-reading-sepco", "sepco-due-date-and-late-payment-guide", "sepco-helpline-complaint-numbers"],
),

"sepco-online-bill-on-mobile": dict(
    title="Check SEPCO Bill on Mobile – Browser, Apps & Saving",
    desc="Check, save and pay your SEPCO bill entirely from a smartphone: browser steps, PDF saving, payment apps, and the AMAR meter-reading app.",
    h1="SEPCO Online Bill on Mobile",
    intro="Everything about a SEPCO bill — checking, saving, paying, even submitting your own meter reading — works from an ordinary smartphone. Here's the complete mobile workflow.",
    body=f"""
<h2>1. Check the bill in your browser</h2>
<p>Open <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> in Chrome or Safari, enter the 14-digit reference number, and the bill loads as an image you can zoom. The page is light — it works fine on slow 3G/4G connections.</p>
<h2>2. Save it as a PDF</h2>
<p><strong>Android:</strong> menu &rarr; Share &rarr; Print &rarr; Save as PDF. <strong>iPhone:</strong> Share &rarr; Print &rarr; pinch out on the preview &rarr; Save to Files. Full detail with screenshots-level steps in the <a href="/how-to-download-duplicate-sepco-bill/">download guide</a>.</p>
<h2>3. Pay without leaving the phone</h2>
<p>JazzCash, Easypaisa, and every major bank's app pay SEPCO bills by reference number with instant confirmation — <a href="/pay-sepco-bill-jazzcash-easypaisa/">two-minute walkthrough here</a>. Save the biller once and future months take three taps.</p>
<h2>4. Optional: the AMAR app</h2>
<p>PITC's <strong>Apna Meter Apni Reading</strong> app lets you photograph your own meter during the reading window so you're billed on actual, not estimated, consumption — particularly useful if your meter is behind a locked gate. <a href="/apna-meter-apni-reading-sepco/">Setup guide</a>.</p>
<h2>Mobile-specific tips</h2>
<ul>
  <li><strong>Bookmark the portal</strong> or add it to your home screen — beware lookalike sites in search results; the official domain is <strong>bill.pitc.com.pk</strong>.</li>
  <li>Store the reference number in your contacts or notes app.</li>
  <li>If the bill image won't load, try disabling data saver / lite mode, or switch between Wi-Fi and mobile data — the portal occasionally rejects some carrier IP ranges temporarily.</li>
</ul>
""",
    faqs=[
        ("Is there an official SEPCO mobile app for bills?", "There is no dedicated SEPCO bill app. The web portal covers bill viewing, and PITC's AMAR app covers meter readings. Treat 'SEPCO bill' apps on the stores as unofficial."),
        ("Does checking the bill use much data?", "No — a bill check typically transfers well under 1 MB."),
        ("Can I check the bill by SMS?", "No public SMS bill-check service currently operates for SEPCO. The browser method is the reliable route on any phone with data."),
    ],
    related=["how-to-check-sepco-bill-online", "pay-sepco-bill-jazzcash-easypaisa", "how-to-download-duplicate-sepco-bill", "apna-meter-apni-reading-sepco", "sepco-online-bill-check", "common-sepco-bill-check-errors"],
),

"common-sepco-bill-check-errors": dict(
    title="SEPCO Bill Check Errors – 'No Record Found' & Fixes",
    desc="Fixes for every common SEPCO bill-check failure: no record found, wrong number length, portal not loading, old reference numbers and more.",
    h1="Common SEPCO Bill Check Errors and Fixes",
    intro="Nearly every failed bill check comes down to one of seven causes. Match your symptom in the table, then use the detailed fix below it.",
    body=f"""
<h2>Symptom &rarr; cause &rarr; fix</h2>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Most likely cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>"No record found"</td><td>Typo, or you entered the 10-digit consumer ID</td><td>Re-enter carefully — the portal needs the <strong>14-digit reference number</strong></td></tr>
<tr><td>Number is only 10 digits</td><td>That's the consumer ID</td><td>Find the 14-digit number on the bill (<a href="/sepco-consumer-id-vs-reference-number/">the difference</a>)</td></tr>
<tr><td>Worked before, now "no record"</td><td>Reference changed after meter/feeder restructuring</td><td>Check the newest paper bill for the current number</td></tr>
<tr><td>Page won't load / times out</td><td>Portal downtime or carrier IP block</td><td>Wait 30–60 min; switch Wi-Fi ↔ mobile data; try another browser</td></tr>
<tr><td>Bill loads but shows last month</td><td>New bill not generated yet</td><td>Wait a few days after your meter-reading date</td></tr>
<tr><td>Blank/broken bill image</td><td>Data saver or partial load</td><td>Disable lite/data-saver mode, reload, let it finish before printing</td></tr>
<tr><td>Amount looks wrong</td><td>Estimated reading, slab change, FPA</td><td>See below</td></tr>
</tbody></table></div>
<h2>When the amount itself looks wrong</h2>
<ol>
  <li>Compare the bill's <strong>present reading</strong> with your actual meter display. If the bill's reading is higher, it's likely estimated — complain at 118 or your subdivision office before paying, and start using the <a href="/apna-meter-apni-reading-sepco/">AMAR app</a>.</li>
  <li>Check whether you crossed <strong>200 units average</strong> — losing protected status can nearly double the rate on all units (<a href="/sepco-protected-vs-unprotected-tariff/">details</a>).</li>
  <li>Check the <strong>FPA line</strong> — a big positive adjustment reflects fuel costs from two months earlier (<a href="/sepco-fuel-price-adjustment-fpa/">how FPA works</a>).</li>
  <li>Sanity-check the math with the <a href="/sepco-bill-estimate-calculator-guide/">calculator</a>.</li>
</ol>
<div class="notice">Only trust <strong>bill.pitc.com.pk</strong> for the actual bill. Third-party "bill check" sites proxy the same data with ads in between — and some are outright fake. The official portal: <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</div>
""",
    faqs=[
        ("The portal rejects my correct 14-digit number every time. Now what?", "If the newest paper bill's number also fails after retries on different networks, contact your subdivision office — the connection record may have been migrated or suspended in the system."),
        ("Why do third-party bill sites show my bill when the official one is down?", "They cache previously fetched copies. That cached copy may be stale — don't rely on it for the current amount or due date."),
        ("Is it safe to enter my reference number on any site?", "The number alone can't be used to change your account, but fake sites use entered numbers for ad targeting and scams. Stick to the official portal."),
    ],
    related=["sepco-consumer-id-vs-reference-number", "where-to-find-sepco-reference-number", "sepco-bill-check-by-name", "sepco-bill-check-by-cnic", "apna-meter-apni-reading-sepco", "sepco-helpline-complaint-numbers"],
),

"faq-about-sepco-online-bill": dict(
    title="SEPCO Online Bill FAQs – 15 Quick Answers",
    desc="Quick answers to the most-asked SEPCO billing questions: checking bills, reference numbers, payments, complaints, tariffs and duplicate copies.",
    h1="SEPCO Online Bill — Frequently Asked Questions",
    intro="The fifteen questions we're asked most, answered in a paragraph each, with links to full guides where the detail matters.",
    body="",  # FAQ page: content lives in the faqs list
    faqs=[
        ("How do I check my SEPCO bill online?", 'Enter your 14-digit reference number at the official PITC portal, <a href="https://bill.pitc.com.pk/sepcobill" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>. It’s free, with no login. Full steps: <a href="/how-to-check-sepco-bill-online/">bill check walkthrough</a>.'),
        ("What is the SEPCO reference number?", 'A 14-digit code printed at the top-left of every bill that identifies your connection. It’s what portals and payment apps use. Details: <a href="/sepco-reference-number-guide/">reference number guide</a>.'),
        ("I lost all my bills — how do I find my reference number?", 'Old payment SMS, bank/wallet app history, or the subdivision office with your CNIC. Five routes: <a href="/where-to-find-sepco-reference-number/">finding your reference number</a>.'),
        ("What's the difference between consumer ID and reference number?", 'The consumer ID is 10 digits (account record); the reference number is 14 digits (used everywhere online). The portal only accepts the 14-digit number. <a href="/sepco-consumer-id-vs-reference-number/">Comparison</a>.'),
        ("How do I get a duplicate bill?", 'View it online and print or save as PDF — free and accepted by banks. Stamped copies come from the subdivision office. <a href="/sepco-duplicate-bill-guide/">Duplicate bill guide</a>.'),
        ("How can I pay my SEPCO bill from my phone?", 'JazzCash, Easypaisa, or any bank app: choose utility bills → electricity → SEPCO, enter the reference number, confirm. <a href="/pay-sepco-bill-jazzcash-easypaisa/">Two-minute guide</a>.'),
        ("What happens if I pay after the due date?", 'You pay the higher "payable after due date" amount, which includes roughly a 10% late payment surcharge; continued non-payment risks disconnection. <a href="/sepco-due-date-and-late-payment-guide/">Late payment guide</a>.'),
        ("What are the current electricity rates?", 'FY 2025-26 domestic rates run from Rs 3.95/unit (lifeline) to Rs 47.69/unit (above 700 units), plus surcharges and taxes. Full tables: <a href="/sepco-tariff-rates-2026/">tariff 2026</a>.'),
        ("What is a protected consumer?", 'A domestic consumer averaging 200 units or less over six months, billed at roughly half the rate with GST exemption. Cross the line and every unit gets pricier. <a href="/sepco-protected-vs-unprotected-tariff/">The 200-unit rule</a>.'),
        ("Why did my bill jump this month with the same usage?", 'Usually FPA (fuel price adjustment), a slab or protection-status change, or an estimated meter reading. <a href="/common-sepco-bill-check-errors/">Diagnosis checklist</a>.'),
        ("What is FPA on my bill?", 'A monthly adjustment for actual fuel generation costs two months prior — it can be positive or negative. <a href="/sepco-fuel-price-adjustment-fpa/">FPA explained</a>.'),
        ("How do I complain about a wrong bill or outage?", 'Call 118, SMS 8118, or visit your subdivision office; unresolved cases can be escalated to NEPRA. All contacts: <a href="/sepco-helpline-complaint-numbers/">helpline directory</a>.'),
        ("My paper bill never arrived — do I still have to pay on time?", 'Yes, the due date stands. Check the amount online and pay by app, then report the delivery problem. <a href="/sepco-bill-not-received-what-to-do/">Missing bill guide</a>.'),
        ("Can I submit my own meter reading?", 'Yes — PITC’s Apna Meter Apni Reading (AMAR) app lets you photograph your meter in the reading window to avoid estimated bills. <a href="/apna-meter-apni-reading-sepco/">AMAR setup guide</a>.'),
        ("Which areas does SEPCO cover?", 'Upper Sindh — including Sukkur, Ghotki, Khairpur, Shikarpur, Jacobabad, Kashmore, Larkana, Qambar Shahdadkot, Naushahro Feroze and Dadu districts. Other areas of Sindh are served by HESCO or K-Electric.'),
    ],
    related=["sepco-online-bill-check", "sepco-tariff-rates-2026", "sepco-bill-payment-methods-guide", "sepco-helpline-complaint-numbers", "sepco-bill-estimate-calculator-guide", "common-sepco-bill-check-errors"],
),
}
