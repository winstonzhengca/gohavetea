(function () {
  "use strict";
  var builder = document.getElementById("cup-builder");
  if (!builder) return;

  var fill = document.getElementById("cup-fill");
  var pearls = document.getElementById("cup-pearls");
  var summary = document.getElementById("cup-summary");
  var form = document.getElementById("cup-options");
  var prefix = summary.textContent;

  function update() {
    var picks = [];
    var fieldsets = form.querySelectorAll("fieldset");
    fieldsets.forEach(function (fs) {
      var checked = fs.querySelector("input:checked");
      if (!checked) return;
      picks.push(checked.value);
      if (fs.dataset.group === "base" && checked.dataset.color) {
        fill.style.background = checked.dataset.color;
      }
      if (fs.dataset.group === "topping") {
        pearls.classList.toggle("is-visible", checked.dataset.pearls !== "none");
      }
    });
    summary.textContent = prefix + " " + picks.join(" · ");
  }

  form.addEventListener("change", update);
  update();
})();
