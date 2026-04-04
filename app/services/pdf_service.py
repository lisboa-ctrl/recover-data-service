from datetime import date

from jinja2 import Environment, PackageLoader, select_autoescape
from weasyprint import HTML

jinja_env = Environment(
    loader=PackageLoader("app", "templates"),
    autoescape=select_autoescape(["html"]),
)


def render_report_html(start_date: date, end_date: date) -> str:
    template = jinja_env.get_template("base_report.html")
    return template.render(start_date=start_date, end_date=end_date)


def generate_pdf(html: str) -> bytes:
    return HTML(string=html).write_pdf()
