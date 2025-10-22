import reflex as rx
from app.states.state import BaseState


def nav_item(item: dict[str, str], collapsed: rx.Var[bool]) -> rx.Component:
    is_active = rx.State.router.page.path == item["href"]
    return rx.el.a(
        rx.el.div(
            rx.icon(item["icon"], class_name="h-5 w-5 shrink-0"),
            rx.cond(
                ~collapsed,
                rx.el.span(
                    item["label"], class_name="truncate transition-opacity duration-200"
                ),
                None,
            ),
            class_name=rx.cond(
                collapsed,
                "flex h-9 w-9 items-center justify-center",
                "flex items-center gap-3 rounded-lg px-3 py-2",
            ),
        ),
        href=item["href"],
        class_name=rx.cond(
            is_active,
            "text-indigo-600 bg-indigo-50",
            "text-gray-500 hover:text-gray-900 hover:bg-gray-50",
        ),
        tooltip=rx.cond(collapsed, item["label"], ""),
        style={"transition": "color 150ms ease-out, background-color 150ms ease-out"},
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("hexagon", class_name="h-7 w-7 text-indigo-600"),
                    rx.cond(
                        ~BaseState.sidebar_collapsed,
                        rx.el.span("DE5", class_name="text-xl font-bold text-gray-900"),
                        None,
                    ),
                    href="/",
                    class_name="flex items-center gap-2 font-semibold",
                ),
                rx.el.button(
                    rx.icon(
                        "chevron-left",
                        class_name="h-5 w-5 transition-transform duration-300",
                        style=rx.cond(
                            BaseState.sidebar_collapsed,
                            {"transform": "rotate(180deg)"},
                            {},
                        ),
                    ),
                    on_click=BaseState.toggle_sidebar,
                    class_name="h-8 w-8 rounded-full flex items-center justify-center bg-gray-100 hover:bg-gray-200",
                ),
                class_name="flex h-16 items-center justify-between border-b px-4",
            ),
            rx.el.nav(
                rx.foreach(
                    BaseState.nav_items,
                    lambda item: nav_item(item, BaseState.sidebar_collapsed),
                ),
                class_name="flex flex-col gap-1.5 p-4 text-sm font-medium",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="https://api.dicebear.com/9.x/notionists/svg?seed=de5user",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.cond(
                    ~BaseState.sidebar_collapsed,
                    rx.el.div(
                        rx.el.p("User", class_name="font-semibold text-gray-800"),
                        rx.el.p("user@de5.fi", class_name="text-xs text-gray-500"),
                        class_name="flex flex-col",
                    ),
                    None,
                ),
                rx.cond(
                    ~BaseState.sidebar_collapsed,
                    rx.icon("send_horizontal", class_name="h-5 w-5 text-gray-500"),
                    None,
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="mt-auto border-t p-4",
        ),
        class_name=rx.cond(
            BaseState.sidebar_collapsed,
            "hidden md:flex flex-col w-20 border-r bg-white transition-width duration-300",
            "hidden md:flex flex-col w-64 border-r bg-white transition-width duration-300",
        ),
        style={"min-height": "100vh"},
    )