import reflex as rx
from app.states.state import BaseState


def header(title: str) -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.h1(
                title, class_name="text-2xl font-bold text-gray-900 tracking-tight"
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    placeholder="Search...",
                    type="search",
                    class_name="w-full bg-white pl-8 md:w-[200px] lg:w-[336px] border border-gray-200 rounded-lg py-2 text-sm focus:ring-indigo-500 focus:border-indigo-500",
                ),
                rx.icon(
                    "search",
                    class_name="absolute left-2.5 top-2.5 h-4 w-4 text-gray-500",
                ),
                class_name="relative flex-1",
            ),
            rx.el.button(
                rx.icon("bell", class_name="h-5 w-5"),
                class_name="h-9 w-9 rounded-full flex items-center justify-center bg-white border border-gray-200 text-gray-600 hover:bg-gray-50",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="sticky top-0 z-10 flex h-16 shrink-0 items-center gap-x-6 border-b border-gray-200 bg-white/75 backdrop-blur-sm px-4 sm:px-6 lg:px-8",
    )