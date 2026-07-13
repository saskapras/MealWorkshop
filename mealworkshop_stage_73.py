# === Stage 73: Add a lightweight HTML report export ===
# Project: MealWorkshop
def export_html_report(self, path="mealworkshop_report.html"):
        from html import escape
        lines = []
        for r in self.recipes.values():
            lines.append(f"<div class='recipe'><h3>{escape(r.name)}</h3>")
            if hasattr(r, 'ingredients'):
                lines.append("<ul>" + "".join(
                    f"<li><b>{escape(i)}:</b> {i.quantity} x {i.unit}</li>"
                    for i in r.ingredients
                ) + "</ul>")
            if hasattr(r, 'cost') and r.cost is not None:
                lines.append(f"<p class='price'>Cost: ${r.cost:.2f}</p>")
            lines.append("</div>")
        menu = self.menus[-1] if self.menus else "No active menu"
        lines.insert(0, f"<h1>MealWorkshop Report</h1><p>Menu: {escape(menu)}</p>")
        with open(path, "w") as f:
            f.write("<html><body>" + "\n".join(lines) + "</body></html>")
