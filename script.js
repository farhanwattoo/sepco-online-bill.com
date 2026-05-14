const billForm = document.getElementById("billForm");
const billStatus = document.getElementById("billStatus");
const billPreview = document.getElementById("billPreview");
const billPrint = document.getElementById("billPrint");

function formatCurrency(amount) {
  return new Intl.NumberFormat("en-PK", { maximumFractionDigits: 2 }).format(amount);
}

billForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const ref = document.getElementById("billRef").value.replace(/\D/g, "");
  const name = document.getElementById("billName").value.trim() || "Consumer";
  const units = Number(document.getElementById("billUnits").value || 0);
  const rate = Number(document.getElementById("billRate").value || 0);
  const tax = Number(document.getElementById("billTax").value || 0);
  const dueDays = Number(document.getElementById("billDueDays").value || 0);
  const subtotal = units * rate;
  const total = subtotal + tax;
  const dueDate = new Date();
  dueDate.setDate(dueDate.getDate() + dueDays);
  const isValid = ref.length === 14;
  billStatus.textContent = isValid ? "Valid format" : "Needs 14 digits";
  billStatus.classList.toggle("tone-good", isValid);
  billStatus.classList.toggle("tone-warn", !isValid);
  billPreview.innerHTML = `
    <div class="summary-card">
      <strong>SEPCO Online Bill</strong>
      <p><b>Name:</b> ${name}</p>
      <p><b>Reference:</b> ${ref || "Not entered"}</p>
      <p><b>Units:</b> ${units}</p>
      <p><b>Energy charges:</b> PKR ${formatCurrency(subtotal)}</p>
      <p><b>Taxes and fees:</b> PKR ${formatCurrency(tax)}</p>
      <p><b>Estimated total:</b> PKR ${formatCurrency(total)}</p>
      <p><b>Due date:</b> ${dueDate.toLocaleDateString("en-PK", { year: "numeric", month: "short", day: "numeric" })}</p>
      <p class="note">This preview is a local helper. Use the official Sukkur Electric Power Company portal for live billed amounts.</p>
    </div>
  `;
});

billPrint.addEventListener("click", () => window.print());
