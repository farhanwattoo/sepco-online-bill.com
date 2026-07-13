# The five "check bill by X" articles (URLs inherited from main's content work).
from template import OFFICIAL

PAGES_C = {

"sepco-bill-check-by-reference-number": dict(
    title="SEPCO Bill Check by Reference Number – The Standard Way",
    desc="Checking a SEPCO bill by reference number is the only method the official portal supports. Entry tips, format rules, and fixes when the number is rejected.",
    h1="SEPCO Bill Check by Reference Number",
    intro="The 14-digit reference number is the only identifier the official SEPCO bill portal accepts — every other method (name, CNIC, meter number) ultimately routes back to it. Here's how to use it correctly and what to do when it's rejected.",
    body=f"""
<h2>The method</h2>
<ol>
  <li>Copy the <strong>14-digit reference number</strong> from any SEPCO bill — top-left, in a row of boxed digits. It's the same every month.</li>
  <li>Open <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> and enter the digits with no spaces, dashes, or letters.</li>
  <li>Submit — the current bill loads with the amount, due date, readings, and history.</li>
</ol>
<h2>Entry rules that trip people up</h2>
<ul>
  <li><strong>Exactly 14 digits.</strong> Ten digits means you're holding the customer ID, not the reference number (<a href="/sepco-bill-check-by-customer-id/">what to do then</a>).</li>
  <li><strong>Include leading zeros.</strong> If the printed number starts with 0, type it — dropping it shortens the number and fails.</li>
  <li><strong>Copy from the newest bill</strong> if an old saved number stopped working; references occasionally change after meter or feeder restructuring.</li>
</ul>
<h2>If the number is rejected</h2>
<p>Re-typed carefully and still "no record found"? Work through the <a href="/common-sepco-bill-check-errors/">error checklist</a> — the causes in order of likelihood are a digit typo, the wrong identifier, a changed reference after reconnection, or portal downtime. If the newest paper bill's own number fails on multiple networks, the record needs attention at your subdivision office.</p>
<h2>Beyond checking</h2>
<p>The same number drives everything else: <a href="/pay-sepco-bill-jazzcash-easypaisa/">app payments</a>, <a href="/sepco-helpline-complaint-numbers/">complaints</a>, and <a href="/apna-meter-apni-reading-sepco/">self meter readings</a>. Save it once in your phone and payment apps, and you'll never need the paper bill again.</p>
""",
    faqs=[
        ("Where do I find the reference number if I have no bill at all?", 'Payment SMS history, bank/wallet app transaction records, or the subdivision office with your CNIC — five routes are detailed in <a href="/where-to-find-sepco-reference-number/">finding your reference number</a>.'),
        ("Does the reference number expire?", "No. It identifies the connection permanently and only changes if the connection itself is restructured."),
        ("Can I check multiple properties?", "Yes — each connection has its own reference number, checked one at a time on the portal."),
    ],
    related=["sepco-online-bill-check", "where-to-find-sepco-reference-number", "sepco-reference-number-guide", "common-sepco-bill-check-errors", "sepco-bill-check-by-customer-id", "sepco-bill-check-by-meter-number"],
),

"sepco-bill-check-by-customer-id": dict(
    title="SEPCO Bill Check by Customer ID – Why It Fails & the Fix",
    desc="The 10-digit SEPCO customer ID is not accepted on the bill portal. What the customer ID is for, and how to get the 14-digit reference number from it.",
    h1="SEPCO Bill Check by Customer ID",
    intro="Many people try their 10-digit customer (consumer) ID on the bill portal and hit 'no record found'. That's expected — the portal only accepts the 14-digit reference number. Here's what the customer ID actually does, and how to get from one number to the other.",
    body=f"""
<h2>Why the customer ID doesn't work online</h2>
<p>PITC's public bill portal indexes bills by <strong>reference number</strong> — the code that locates your connection in the distribution network. The customer ID is an <strong>account-level identifier</strong> used inside SEPCO's commercial system for things like name transfers and account corrections. It was never wired into the public lookup, so a 10-digit entry can't match anything.</p>
<h2>Getting the reference number when you only have the customer ID</h2>
<ol>
  <li><strong>Check the same document again.</strong> Wherever the customer ID is printed (an old bill, a connection order), the 14-digit reference number is almost always printed alongside it.</li>
  <li><strong>Payment trails:</strong> old bank receipts and JazzCash/Easypaisa SMS confirmations carry the reference number.</li>
  <li><strong>Subdivision office:</strong> staff can convert a customer ID to the matching reference number in the billing system on the spot — bring your CNIC.</li>
</ol>
<h2>When the customer ID is the number you need</h2>
<ul>
  <li>Ownership/name transfer of the connection.</li>
  <li>Correcting the registered name, address, or tariff category.</li>
  <li>Some legacy complaint records at the office.</li>
</ul>
<p>Full side-by-side comparison of the two identifiers: <a href="/sepco-consumer-id-vs-reference-number/">consumer ID vs reference number</a>. Once you have the 14-digit number, the <a href="{OFFICIAL}" target="_blank" rel="noopener">official portal</a> shows your bill instantly.</p>
""",
    faqs=[
        ("Is the customer ID ever accepted anywhere online?", "Some other DISCOs' portals and apps accept customer IDs, which causes the confusion — SEPCO's public bill lookup does not."),
        ("Are the customer ID and reference number related mathematically?", "No — you can't derive one from the other. They're separate keys in the billing system, linked only through your account record."),
        ("Which number should I save for everyday use?", "The 14-digit reference number. It covers bill checking, payments, complaints, and the AMAR app — the customer ID is only needed for occasional account paperwork."),
    ],
    related=["sepco-consumer-id-vs-reference-number", "sepco-bill-check-by-reference-number", "where-to-find-sepco-reference-number", "common-sepco-bill-check-errors", "sepco-online-bill-check", "sepco-helpline-complaint-numbers"],
),

"sepco-bill-check-by-cnic": dict(
    title="SEPCO Bill Check by CNIC – Is It Possible in 2026?",
    desc="You cannot check a SEPCO bill by CNIC online — no DISCO portal offers it. What your CNIC is actually used for, and the fastest real alternatives.",
    h1="Can You Check a SEPCO Bill by CNIC?",
    intro="No — there is no online SEPCO (or any Pakistani DISCO) bill check by CNIC, and any website claiming to offer one is not pulling real data. Here's why the option doesn't exist, what your CNIC actually does in SEPCO's system, and the fastest real routes to your bill.",
    body=f"""
<h2>Why CNIC lookup doesn't exist</h2>
<ul>
  <li><strong>Connections aren't keyed to CNICs.</strong> Bills attach to premises via the reference number; many connections still carry a previous owner's or a landlord's name, and one person may hold several connections.</li>
  <li><strong>Privacy:</strong> a public CNIC search would let anyone enumerate a person's properties and bills. The public portal deliberately asks only for a reference number.</li>
</ul>
<h2>What your CNIC is actually used for</h2>
<ul>
  <li><strong>New connection applications</strong> on the ENC portal (<a href="/sepco-new-connection-guide/">guide</a>).</li>
  <li><strong>Tracing a lost reference number</strong> at the subdivision office — staff verify you against the address and account record.</li>
  <li><strong>Name transfer / ownership changes</strong> and installment approvals.</li>
  <li><strong>Filer status</strong> for advance income tax on large bills (FBR matches through account data, not the bill portal).</li>
</ul>
<h2>The real routes to your bill</h2>
<ol>
  <li>Find the 14-digit reference number — any old bill, payment SMS, or app history (<a href="/where-to-find-sepco-reference-number/">five recovery routes</a>).</li>
  <li>Enter it at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</li>
  <li>No number recoverable at home? The subdivision office traces it from your <strong>CNIC + address</strong> in minutes — that's the one place CNIC genuinely helps with bill lookup.</li>
</ol>
<div class="notice">Sites advertising "SEPCO bill check by CNIC" either redirect you to the normal reference-number search or harvest CNIC numbers. Never enter your CNIC on unofficial bill websites.</div>
""",
    faqs=[
        ("A website asked for my CNIC to show my bill — is it legit?", "No. The official portal never asks for a CNIC. Treat any such site as a data-harvesting risk and close it."),
        ("Can the 118 helpline look up my bill from my CNIC?", "Phone agents work from the reference number. Identity-based tracing happens at the subdivision office where documents can be verified."),
        ("I bought a property — how do I get its bills with my CNIC?", "Take your CNIC and ownership documents to the subdivision office: they'll give you the reference number immediately, and you can file the name-transfer there too."),
    ],
    related=["where-to-find-sepco-reference-number", "sepco-bill-check-by-reference-number", "sepco-bill-check-by-name", "sepco-new-connection-guide", "sepco-helpline-complaint-numbers", "sepco-online-bill-check"],
),

"sepco-bill-check-by-name": dict(
    title="SEPCO Bill Check by Name – Why It's Not Offered",
    desc="There is no SEPCO bill search by name online. Why the portal doesn't offer it, and the quickest ways to find your bill without the paper copy.",
    h1="Can You Check a SEPCO Bill by Name?",
    intro="No online name search exists for SEPCO bills — and it wouldn't work well if it did, since thousands of consumers share names and many connections are still registered to previous occupants. Here's the reality and the quickest workarounds.",
    body=f"""
<h2>Why name search isn't offered</h2>
<ul>
  <li><strong>Names aren't unique:</strong> a district has hundreds of consumers with identical names; matching would be guesswork.</li>
  <li><strong>Registered names go stale:</strong> connections commonly remain in a previous owner's, a deceased relative's, or a landlord's name for years — the current occupant's name often isn't in the system at all.</li>
  <li><strong>Privacy:</strong> exposing bills by name would let anyone browse a neighbour's finances.</li>
</ul>
<h2>What to do instead</h2>
<ol>
  <li><strong>Hunt for the reference number, not the name.</strong> Any old bill, bank receipt, or wallet-app payment record for the property contains the 14-digit number (<a href="/where-to-find-sepco-reference-number/">where to look</a>).</li>
  <li><strong>Ask whoever paid before you.</strong> For rentals, the landlord or previous tenant almost always has the number in a payment app's saved billers.</li>
  <li><strong>Subdivision office:</strong> with your CNIC and the exact address, staff trace the connection regardless of whose name it carries.</li>
</ol>
<h2>Once you have the number</h2>
<p>Check the bill at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a> — the displayed bill shows the registered name, which is how you confirm you've traced the right connection. If you want the record to carry <em>your</em> name going forward, file a name transfer at the office (CNIC + ownership/tenancy proof).</p>
""",
    faqs=[
        ("The bill shows someone else's name — can I still pay it?", "Yes. Payment credits the connection, not the named person. The name only matters for account paperwork like transfers and legal use."),
        ("Can I search by address instead of name?", "Not on the public portal. Address-based tracing is exactly what the subdivision office does — it's an in-person service."),
        ("Someone is using my name on their connection — what can I do?", "Raise it at the subdivision office with your CNIC; name corrections and disputes are handled at account level with documentary proof."),
    ],
    related=["sepco-bill-check-by-cnic", "where-to-find-sepco-reference-number", "sepco-bill-check-by-reference-number", "sepco-helpline-complaint-numbers", "sepco-online-bill-check", "sepco-duplicate-bill-guide"],
),

"sepco-bill-check-by-meter-number": dict(
    title="SEPCO Bill Check by Meter Number – What Works Instead",
    desc="The SEPCO portal doesn't accept meter numbers. Meter number vs reference number, when the meter number matters, and how to trace your bill from it.",
    h1="SEPCO Bill Check by Meter Number",
    intro="The number stamped on your meter can't be entered on the bill portal — it identifies the physical device, not the billing account. But if the meter number is all you have, it can still lead you to your bill. Here's how.",
    body=f"""
<h2>Meter number vs reference number</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Meter number</th><th>Reference number</th></tr></thead>
<tbody>
<tr><td>What it identifies</td><td>The physical meter (device serial)</td><td>Your billing connection</td></tr>
<tr><td>Where it appears</td><td>Stamped/printed on the meter; also printed on the bill's reading block</td><td>Top-left of the bill, 14 boxed digits</td></tr>
<tr><td>Bill portal</td><td>Not accepted</td><td>Required</td></tr>
<tr><td>Changes when…</td><td>The meter is replaced</td><td>Rarely (network restructuring)</td></tr>
</tbody></table></div>
<h2>From meter number to bill</h2>
<ol>
  <li><strong>Write down the meter number</strong> from the device (and photograph the display while you're there).</li>
  <li>Take it to your <strong>subdivision office</strong> with your CNIC — the billing system maps meter numbers to reference numbers, so staff can retrieve yours quickly. This is the standard route after moving into a property with no paperwork.</li>
  <li>Save the reference number and check the bill at <a href="{OFFICIAL}" target="_blank" rel="noopener">bill.pitc.com.pk/sepcobill</a>.</li>
</ol>
<h2>When the meter number actually matters</h2>
<ul>
  <li><strong>Meter replacement:</strong> your bill's reading block shows the old and new meter numbers in the transition month — check both readings were billed correctly.</li>
  <li><strong>Defective/burnt meter complaints:</strong> quote the meter number on 118 alongside your reference number.</li>
  <li><strong>Reading disputes:</strong> a photo showing the meter number + display is the strongest evidence (<a href="/apna-meter-apni-reading-sepco/">AMAR app</a> formalises exactly this).</li>
</ul>
""",
    faqs=[
        ("My meter was replaced — did my reference number change?", "Usually not; the billing connection continues with the new device mapped to it. If your saved number stops working after a replacement, confirm the current number on the next printed bill."),
        ("Can 118 trace my account from the meter number?", "Phone agents may manage for fault complaints, but for retrieving your reference number reliably, the subdivision office lookup is the dependable route."),
        ("The meter shows a different number than my bill's meter field — problem?", "Yes, worth reporting: it can mean a mis-mapped meter (you may be billed on someone else's readings). Take photos of the meter and your bill to the subdivision office."),
    ],
    related=["sepco-bill-check-by-reference-number", "sepco-reference-number-guide", "apna-meter-apni-reading-sepco", "how-to-read-a-sepco-electricity-bill", "common-sepco-bill-check-errors", "sepco-helpline-complaint-numbers"],
),
}
