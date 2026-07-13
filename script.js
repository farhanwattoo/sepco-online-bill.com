/* SEPCO bill estimator — FY 2025-26 domestic base tariff (effective 1 July 2025).
   Rates are the NEPRA-notified uniform national tariff; actual bills also carry
   monthly FPA, quarterly adjustments and rounding, so results are estimates. */

const TARIFF = {
  lifeline: [
    { upTo: 50, rate: 3.95 },
    { upTo: 100, rate: 7.74 }
  ],
  protected: [
    { upTo: 100, rate: 10.54 },
    { upTo: 200, rate: 13.01 }
  ],
  unprotected: [
    { upTo: 100, rate: 22.44 },
    { upTo: 200, rate: 28.92 },
    { upTo: 300, rate: 33.10 },
    { upTo: 400, rate: 38.00 },
    { upTo: 500, rate: 40.21 },
    { upTo: 600, rate: 41.63 },
    { upTo: 700, rate: 42.77 },
    { upTo: Infinity, rate: 47.69 }
  ]
};

/* Monthly fixed charge for non-protected domestic consumers by slab */
const FIXED_CHARGES = [
  { upTo: 300, amount: 0 },
  { upTo: 400, amount: 200 },
  { upTo: 500, amount: 400 },
  { upTo: 600, amount: 600 },
  { upTo: 700, amount: 800 },
  { upTo: Infinity, amount: 1000 }
];

const FC_SURCHARGE = 3.23;   // financing cost surcharge, Rs/unit
const ELECTRICITY_DUTY = 0.015; // 1.5% of variable charges (Sindh)
const GST_RATE = 0.18;       // 18% sales tax (non-protected domestic)
const TV_FEE = 35;           // PTV licence fee, domestic

function slabFor(slabs, units) {
  return slabs.findIndex((s) => units <= s.upTo);
}

/* Domestic consumers retain the benefit of one previous slab only:
   units up to the previous slab ceiling are billed at the previous
   slab rate, the remainder at the current slab rate. */
function energyCharge(slabs, units) {
  if (units <= 0) return 0;
  const i = slabFor(slabs, units);
  if (i <= 0) return units * slabs[0].rate;
  const prevCeiling = slabs[i - 1].upTo;
  return prevCeiling * slabs[i - 1].rate + (units - prevCeiling) * slabs[i].rate;
}

function fixedCharge(units) {
  return FIXED_CHARGES.find((f) => units <= f.upTo).amount;
}

function rs(amount) {
  return "Rs " + new Intl.NumberFormat("en-PK", { maximumFractionDigits: 0 }).format(Math.round(amount));
}

const billForm = document.getElementById("billForm");

if (billForm) {
  const billStatus = document.getElementById("billStatus");
  const billPreview = document.getElementById("billPreview");
  const billPrint = document.getElementById("billPrint");

  billForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const refInput = document.getElementById("billRef").value.replace(/\D/g, "");
    const units = Math.max(0, Math.floor(Number(document.getElementById("billUnits").value || 0)));
    let category = document.getElementById("billCategory").value;
    const fpaPerUnit = Number(document.getElementById("billFpa").value || 0);

    if (refInput.length > 0) {
      const ok = refInput.length === 14;
      billStatus.textContent = ok ? "Valid 14-digit format" : "Reference needs 14 digits (" + refInput.length + " entered)";
      billStatus.classList.toggle("tone-good", ok);
      billStatus.classList.toggle("tone-warn", !ok);
    } else {
      billStatus.textContent = "No reference entered";
      billStatus.classList.remove("tone-good", "tone-warn");
    }

    let categoryNote = "";
    if (category === "lifeline" && units > 100) {
      category = "unprotected";
      categoryNote = "Lifeline rates only apply up to 100 units, so the non-protected tariff was used.";
    }
    if (category === "protected" && units > 200) {
      category = "unprotected";
      categoryNote = "Protected rates only apply up to 200 units, so the non-protected tariff was used.";
    }

    const energy = energyCharge(TARIFF[category], units);
    const isSubsidised = category === "lifeline" || category === "protected";
    const fcSurcharge = isSubsidised ? 0 : units * FC_SURCHARGE;
    const fixed = isSubsidised ? 0 : fixedCharge(units);
    const fpa = units * fpaPerUnit;
    const variable = energy + fcSurcharge + fpa;
    const duty = variable * ELECTRICITY_DUTY;
    const gst = isSubsidised ? 0 : (variable + fixed + duty) * GST_RATE;
    const total = variable + fixed + duty + gst + TV_FEE;

    const rows = [
      ["Energy charge (" + units + " units)", energy],
      ["FC surcharge (Rs " + FC_SURCHARGE + "/unit)", fcSurcharge],
      ["Fuel price adjustment", fpa],
      ["Fixed charge", fixed],
      ["Electricity duty (1.5%)", duty],
      ["GST (18%)", gst],
      ["TV licence fee", TV_FEE]
    ];

    billPreview.innerHTML =
      '<div class="summary-card">' +
      "<strong>Estimated SEPCO bill — " + (category === "unprotected" ? "non-protected" : category) + " domestic</strong>" +
      '<table><tbody>' +
      rows.map((r) => "<tr><td>" + r[0] + "</td><td style=\"text-align:right\">" + rs(r[1]) + "</td></tr>").join("") +
      '<tr><td><strong>Estimated total</strong></td><td style="text-align:right"><strong>' + rs(total) + "</strong></td></tr>" +
      "</tbody></table>" +
      (categoryNote ? '<p class="note">' + categoryNote + "</p>" : "") +
      '<p class="note">Estimate based on the FY 2025-26 base tariff. Your actual bill also includes quarterly adjustments and that month’s FPA — always confirm on the official portal at bill.pitc.com.pk/sepcobill.</p>' +
      "</div>";
  });

  if (billPrint) {
    billPrint.addEventListener("click", () => window.print());
  }
}
