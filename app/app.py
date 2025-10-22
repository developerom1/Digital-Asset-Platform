import reflex as rx
from app.pages.dashboard import dashboard_page
from app.pages.marketplace import marketplace_page
from app.pages.portfolio import portfolio_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(dashboard_page, route="/", title="DE5 | Dashboard")
app.add_page(marketplace_page, route="/marketplace", title="DE5 | Marketplace")
app.add_page(portfolio_page, route="/portfolio", title="DE5 | Portfolio")