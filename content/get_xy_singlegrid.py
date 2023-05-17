from selenium import webdriver
from content.press_wizzard_button import press_wizzard_button
from content.get_list_wizard_sections import get_list_wizard_sections
from content.set_wizard_section import set_wizard_section
from content.get_list_wizard_sections_tools import get_list_wizard_sections_tools


def get_xy_singlegrid(driver: webdriver.firefox.webdriver.WebDriver):
    press_wizzard_button(driver)

    _, labels = get_list_wizard_sections(driver)

    raster_tools: str = labels[-1]
    raster_tool_id_singlegrid: int = 7
    set_wizard_section(driver, raster_tools)

    center_x, center_y, _, _ = get_list_wizard_sections_tools(driver)

    x = center_x[raster_tool_id_singlegrid]
    y = center_y[raster_tool_id_singlegrid]

    return x, y
