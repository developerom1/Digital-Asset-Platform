import reflex as rx
from app.components.layout import main_layout
from app.states.state import PortfolioState


def holding_row(holding: rx.Var[dict]) -> rx.Component:
    asset = holding["asset"]
    change_24h = asset["change_24h"]
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(src=asset["logo_url"], class_name="h-9 w-9 rounded-full"),
                rx.el.div(
                    rx.el.p(asset["name"], class_name="font-semibold text-gray-900"),
                    rx.el.p(asset["symbol"], class_name="text-sm text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.p(f"${asset['price']:.2f}", class_name="text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon(
                    rx.cond(change_24h >= 0, "trending-up", "trending-down"),
                    class_name="h-4 w-4",
                ),
                rx.el.span(f"{change_24h:.2f}%"),
                class_name=rx.cond(
                    change_24h >= 0,
                    "flex items-center gap-1 text-green-600",
                    "flex items-center gap-1 text-red-600",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.p(holding["amount"].to_string(), class_name="text-gray-900"),
            rx.el.p(asset["symbol"], class_name="text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.p(
                f"${holding['value_usd']:.2f}", class_name="font-semibold text-gray-900"
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.button(
                "Trade",
                class_name="px-3 py-1 text-xs font-semibold text-indigo-600 bg-indigo-50 rounded-md hover:bg-indigo-100",
            ),
            rx.el.button(
                "Details",
                class_name="ml-2 px-3 py-1 text-xs font-semibold text-gray-600 bg-gray-100 rounded-md hover:bg-gray-200",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name="hover:bg-gray-50",
    )


def portfolio_page() -> rx.Component:
    return main_layout(
        "Portfolio",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Total Balance", class_name="text-sm font-medium text-gray-500"
                    ),
                    rx.el.p(
                        f"${PortfolioState.total_portfolio_value:.2f}",
                        class_name="mt-1 text-3xl font-semibold text-gray-900",
                    ),
                    class_name="p-6 bg-white border rounded-xl shadow-sm",
                ),
                rx.el.div(
                    rx.el.h3(
                        "24h Change", class_name="text-sm font-medium text-gray-500"
                    ),
                    rx.el.div(
                        rx.icon(
                            rx.cond(
                                PortfolioState.overall_24h_change >= 0,
                                "arrow-up-right",
                                "arrow-down-right",
                            ),
                            class_name="h-5 w-5",
                        ),
                        rx.el.span(f"{PortfolioState.overall_24h_change:.2f}%"),
                        class_name=rx.cond(
                            PortfolioState.overall_24h_change >= 0,
                            "mt-1 flex items-baseline gap-2 text-3xl font-semibold text-green-600",
                            "mt-1 flex items-baseline gap-2 text-3xl font-semibold text-red-600",
                        ),
                    ),
                    class_name="p-6 bg-white border rounded-xl shadow-sm",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Asset",
                                    scope="col",
                                    class_name="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6",
                                ),
                                rx.el.th(
                                    "Price",
                                    scope="col",
                                    class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                ),
                                rx.el.th(
                                    "24h Change",
                                    scope="col",
                                    class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                ),
                                rx.el.th(
                                    "Holdings",
                                    scope="col",
                                    class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                ),
                                rx.el.th(
                                    "Value",
                                    scope="col",
                                    class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                ),
                                rx.el.th(
                                    rx.el.span("Actions", class_name="sr-only"),
                                    scope="col",
                                    class_name="relative py-3.5 pl-3 pr-4 sm:pr-6",
                                ),
                            ),
                            class_name="bg-gray-50",
                        ),
                        rx.el.tbody(
                            rx.foreach(PortfolioState.holdings, holding_row),
                            class_name="divide-y divide-gray-200 bg-white",
                        ),
                        class_name="min-w-full divide-y divide-gray-300",
                    ),
                    class_name="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg",
                ),
                class_name="flow-root",
            ),
            class_name="w-full",
        ),
    )