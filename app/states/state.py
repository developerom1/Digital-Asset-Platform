import reflex as rx
from typing import TypedDict


class Asset(TypedDict):
    id: str
    name: str
    symbol: str
    price: float
    change_24h: float
    volume_24h: float
    market_cap: float
    logo_url: str


class PortfolioHolding(TypedDict):
    asset: Asset
    amount: float
    value_usd: float


class NavItem(TypedDict):
    label: str
    icon: str
    href: str


class BaseState(rx.State):
    """The base state for the app, shared across all pages."""

    sidebar_collapsed: bool = False
    nav_items: list[NavItem] = [
        {"label": "Dashboard", "icon": "layout-grid", "href": "/"},
        {"label": "Marketplace", "icon": "store", "href": "/marketplace"},
        {"label": "Portfolio", "icon": "wallet", "href": "/portfolio"},
        {"label": "AI Agent", "icon": "bot", "href": "#"},
        {"label": "Analytics", "icon": "bar-chart-3", "href": "#"},
        {"label": "Education", "icon": "book-open", "href": "#"},
    ]

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed


class DashboardState(BaseState):
    """State for the main dashboard page."""

    pass


class MarketplaceState(BaseState):
    """State for the marketplace page."""

    assets: list[Asset] = [
        {
            "id": "bitcoin",
            "name": "Bitcoin",
            "symbol": "BTC",
            "price": 68123.45,
            "change_24h": 2.5,
            "volume_24h": 45000000000,
            "market_cap": 1300000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=bitcoin",
        },
        {
            "id": "ethereum",
            "name": "Ethereum",
            "symbol": "ETH",
            "price": 3545.67,
            "change_24h": -1.2,
            "volume_24h": 22000000000,
            "market_cap": 425000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=ethereum",
        },
        {
            "id": "solana",
            "name": "Solana",
            "symbol": "SOL",
            "price": 167.89,
            "change_24h": 5.8,
            "volume_24h": 3500000000,
            "market_cap": 75000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=solana",
        },
        {
            "id": "cardano",
            "name": "Cardano",
            "symbol": "ADA",
            "price": 0.45,
            "change_24h": 0.5,
            "volume_24h": 500000000,
            "market_cap": 16000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=cardano",
        },
        {
            "id": "ripple",
            "name": "Ripple",
            "symbol": "XRP",
            "price": 0.52,
            "change_24h": -3.1,
            "volume_24h": 1200000000,
            "market_cap": 28000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=ripple",
        },
        {
            "id": "dogecoin",
            "name": "Dogecoin",
            "symbol": "DOGE",
            "price": 0.16,
            "change_24h": 10.2,
            "volume_24h": 2100000000,
            "market_cap": 23000000000,
            "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=dogecoin",
        },
    ]
    search_query: str = ""
    sort_by: str = "market_cap_desc"

    @rx.var
    def filtered_and_sorted_assets(self) -> list[Asset]:
        """Filters and sorts assets based on search query and sort option."""
        assets = self.assets
        if self.search_query:
            query = self.search_query.lower()
            assets = [
                asset
                for asset in assets
                if query in asset["name"].lower() or query in asset["symbol"].lower()
            ]
        if self.sort_by == "market_cap_desc":
            return sorted(assets, key=lambda a: a["market_cap"], reverse=True)
        if self.sort_by == "price_desc":
            return sorted(assets, key=lambda a: a["price"], reverse=True)
        if self.sort_by == "change_desc":
            return sorted(assets, key=lambda a: a["change_24h"], reverse=True)
        if self.sort_by == "change_asc":
            return sorted(assets, key=lambda a: a["change_24h"])
        return assets

    @rx.event
    def set_sort_by(self, value: str):
        self.sort_by = value


class PortfolioState(BaseState):
    """State for the portfolio page."""

    holdings: list[PortfolioHolding] = [
        {
            "asset": {
                "id": "bitcoin",
                "name": "Bitcoin",
                "symbol": "BTC",
                "price": 68123.45,
                "change_24h": 2.5,
                "volume_24h": 45000000000,
                "market_cap": 1300000000000,
                "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=bitcoin",
            },
            "amount": 0.5,
            "value_usd": 34061.73,
        },
        {
            "asset": {
                "id": "ethereum",
                "name": "Ethereum",
                "symbol": "ETH",
                "price": 3545.67,
                "change_24h": -1.2,
                "volume_24h": 22000000000,
                "market_cap": 425000000000,
                "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=ethereum",
            },
            "amount": 10,
            "value_usd": 35456.7,
        },
        {
            "asset": {
                "id": "solana",
                "name": "Solana",
                "symbol": "SOL",
                "price": 167.89,
                "change_24h": 5.8,
                "volume_24h": 3500000000,
                "market_cap": 75000000000,
                "logo_url": "https://api.dicebear.com/9.x/icons/svg?seed=solana",
            },
            "amount": 100,
            "value_usd": 16789.0,
        },
    ]

    @rx.var
    def total_portfolio_value(self) -> float:
        """Calculates the total value of the portfolio."""
        return sum((h["value_usd"] for h in self.holdings))

    @rx.var
    def overall_24h_change(self) -> float:
        """Calculates the weighted average 24h change for the portfolio."""
        if not self.total_portfolio_value:
            return 0.0
        total_change_value = sum(
            (h["value_usd"] * (h["asset"]["change_24h"] / 100) for h in self.holdings)
        )
        return total_change_value / self.total_portfolio_value * 100