import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.states.state import BaseState


def main_layout(page_title: str, content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(title=page_title),
            rx.el.main(content, class_name="p-4 sm:p-6 lg:p-8"),
            class_name=rx.cond(
                BaseState.sidebar_collapsed,
                "flex flex-col flex-1 transition-margin duration-300 md:ml-20",
                "flex flex-col flex-1 transition-margin duration-300 md:ml-64",
            ),
        ),
        class_name="flex min-h-screen w-full bg-gray-50 font-['Open_Sans']",
    )