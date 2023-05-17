from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def action_chain_drag_and_drop(
    driver: webdriver.firefox.webdriver.WebDriver,
    x_from: int,
    y_from: int,
    x_to: int,
    y_to: int,
):
    actions = ActionChains(driver)
    actions.move_by_offset(x_from, y_from)
    actions.click_and_hold()
    actions.move_by_offset(x_to - x_from, y_to - y_from)
    actions.release()
    actions.perform()
