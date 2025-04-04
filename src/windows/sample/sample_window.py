from __future__ import annotations

import dearpygui.dearpygui as dpg


def sample_window() -> None:
    with dpg.window(label="クトゥルフツール", width=400, height=300):
        dpg.add_text("クトゥルフツール")
