import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
import os
import json


def scroll_down_content_page(driver: webdriver.firefox.webdriver.WebDriver):
    string_json_path: str = os.path.join("content", "scroll_down_content_page.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    height = driver.execute_script("return document.body.scrollHeight")

    found_element_list = driver.find_elements(By.TAG_NAME, "h2")
    found_element = None
    for element in found_element_list:
        if element.text == string_dict["Tag"]:
            found_element = element
            break
    assert found_element is not None

    try:
        actions = ActionChains(driver)
        actions.scroll_from_origin(ScrollOrigin.from_element(found_element), 0, height)
        actions.perform()
    except selenium.common.exceptions.MoveTargetOutOfBoundsException:
        pass
