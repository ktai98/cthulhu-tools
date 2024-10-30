from __future__ import annotations

import dearpygui.dearpygui as dpg


def main() -> None:
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()
    with dpg.window(label="Window Title"):
        dpg.add_text("Hello DearPyGui.")
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    return


if __name__ == "__main__":
    main()
