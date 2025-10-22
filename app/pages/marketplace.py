import reflex as rx
from app.components.layout import main_layout
from app.states.state import MarketplaceState


def asset_card(asset: rx.Var[dict]) -> rx.Component:
    change_24h = asset["change_24h"]
    return rx.el.div(
        rx.el.div(
            rx.image(src=asset["logo_url"], class_name="h-10 w-10 rounded-full"),
            rx.el.div(
                rx.el.p(asset["name"], class_name="font-semibold text-gray-900"),
                rx.el.p(asset["symbol"], class_name="text-sm text-gray-500"),
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.p(
                f"${asset['price'].to_string()}",
                class_name="text-lg font-medium text-gray-800",
            ),
            rx.el.div(
                rx.icon(
                    rx.cond(change_24h >= 0, "trending-up", "trending-down"),
                    class_name="h-4 w-4",
                ),
                rx.el.span(f"{change_24h.to_string()}%"),
                class_name=rx.cond(
                    change_24h >= 0,
                    "flex items-center gap-1 text-sm font-medium text-green-600",
                    "flex items-center gap-1 text-sm font-medium text-red-600",
                ),
            ),
            class_name="text-right",
        ),
        rx.el.button(
            "Trade",
            class_name="w-full mt-4 py-2 px-4 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-75 transition-colors",
        ),
        class_name="flex flex-col justify-between p-5 bg-white border rounded-xl shadow-sm hover:shadow-lg transition-all duration-200",
    )


def marketplace_page() -> rx.Component:
    return main_layout(
        "Marketplace",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        placeholder="Search by name or symbol...",
                        on_change=MarketplaceState.set_search_query,
                        class_name="w-full md:w-80 bg-white pl-4 pr-4 py-2 border border-gray-200 rounded-lg text-sm focus:ring-indigo-500 focus:border-indigo-500",
                    ),
                    class_name="relative flex-1",
                ),
                rx.el.div(
                    rx.el.select(
                        rx.el.option("Sort by Market Cap", value="market_cap_desc"),
                        rx.el.option("Sort by Price", value="price_desc"),
                        rx.el.option("Top Gainers 24h", value="change_desc"),
                        rx.el.option("Top Losers 24h", value="change_asc"),
                        on_change=MarketplaceState.set_sort_by,
                        default_value=MarketplaceState.sort_by,
                        class_name="w-full md:w-auto bg-white border border-gray-200 rounded-lg py-2 pl-3 pr-8 text-sm focus:ring-indigo-500 focus:border-indigo-500",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-6",
            ),
            rx.el.div(
                rx.foreach(MarketplaceState.filtered_and_sorted_assets, asset_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4",
            ),
            class_name="w-full",
        ),
    )