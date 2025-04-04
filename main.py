from __future__ import annotations

import dearpygui.dearpygui as dpg

from src.windows.sample.sample_window import sample_window


def dpg_init() -> None:
    """
    DearPyGuiのセットアップを行う関数
    """
    dpg.create_context()  # dearpyguiを使う宣言
    dpg.create_viewport()  # viewportという描画スペースの宣言
    dpg.setup_dearpygui()  # セットアップ（必須）
    font_file = "./src/fonts/NotoSansJP-Black.ttf"
    with dpg.font_registry():
        with dpg.font(font_file, 20) as default_font:
            dpg.add_font_range(0x0800, 0xFFFF)
    dpg.bind_font(default_font)


def main() -> None:
    dpg_init()

    sample_window()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

    return None


if __name__ == "__main__":
    main()
