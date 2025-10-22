import reflex as rx
from app.components.layout import main_layout
from app.states.state import DashboardState, PortfolioState


def info_card(
    icon_name: str, title: str, value: rx.Var[str], change: rx.Var[float]
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(title, class_name="text-sm font-medium text-gray-500"),
            rx.icon(icon_name, class_name="h-5 w-5 text-gray-400"),
            class_name="flex items-center justify-between",
        ),
        rx.el.div(
            rx.el.p(value, class_name="text-2xl font-semibold text-gray-900"),
            rx.el.div(
                rx.icon(
                    rx.cond(change >= 0, "arrow-up-right", "arrow-down-right"),
                    class_name="h-4 w-4",
                ),
                rx.el.span(f"{change:.2f}%"),
                class_name=rx.cond(
                    change >= 0,
                    "flex items-center text-sm font-medium text-green-600",
                    "flex items-center text-sm font-medium text-red-600",
                ),
            ),
            class_name="flex items-baseline gap-2 mt-2",
        ),
        class_name="rounded-xl border bg-white p-5 shadow-sm hover:shadow-md transition-shadow",
    )


def dashboard_page() -> rx.Component:
    return main_layout(
        "Dashboard",
        rx.el.div(
            rx.el.div(
                info_card(
                    "wallet",
                    "Portfolio Value",
                    f"${PortfolioState.total_portfolio_value:.2f}",
                    PortfolioState.overall_24h_change,
                ),
                info_card("activity", "24h Volume", "$68.7B", rx.Var.create(3.1)),
                info_card(
                    "candlestick-chart", "Market Cap", "$1.9T", rx.Var.create(1.8)
                ),
                info_card("users", "Active Traders", "1.2M", rx.Var.create(0.5)),
                class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Welcome to DE5 Digital Asset Platform",
                        class_name="text-2xl font-bold text-gray-900",
                    ),
                    rx.el.p(
                        "Your self-directed journey into the world of digital assets starts here. Explore markets, manage your portfolio, and leverage our AI for insights.",
                        class_name="mt-2 text-gray-600",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Important Disclaimers",
                        class_name="text-lg font-semibold text-gray-800 mb-2",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            "DE5 is a technology platform and not a broker, financial advisor, or asset manager."
                        ),
                        rx.el.li(
                            "All trades and investments are self-directed. You are in complete control of your assets and decisions."
                        ),
                        rx.el.li(
                            "Digital asset investments are inherently risky. The value of assets can be volatile, and you may lose your entire investment."
                        ),
                        rx.el.li(
                            "All assets are issued by third parties. DE5 does not issue or endorse any specific digital asset."
                        ),
                        class_name="list-disc list-inside space-y-1 text-sm text-gray-500",
                    ),
                    class_name="p-6 bg-white rounded-xl border border-yellow-200 bg-yellow-50",
                ),
                class_name="mt-8 p-8 bg-white rounded-xl border shadow-sm",
            ),
            class_name="flex flex-col gap-6",
        ),
    )