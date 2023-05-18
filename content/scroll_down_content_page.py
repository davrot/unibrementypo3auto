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

    max_height_per_step = driver.execute_script("return document.body.scrollHeight")

    final_y: int = 0
    while final_y == 0:
        element = driver.find_elements(By.TAG_NAME, "div")[-1]
        # final_x = element.location["x"]
        final_y = element.location["y"]

    found_element_list = driver.find_elements(By.TAG_NAME, "h2")
    found_element = None
    for element in found_element_list:
        if element.text == string_dict["Tag"]:
            found_element = element
            break
    assert found_element is not None
    # start_x = found_element.location["x"]
    start_y = found_element.location["y"]

    print(start_y)
    print(final_y)
    print(max_height_per_step)
    print("----")
    to_scroll = final_y - start_y
    try:
        if to_scroll > 0:
            actions = ActionChains(driver)
            if to_scroll > max_height_per_step:
                actions.scroll_from_origin(
                    ScrollOrigin.from_element(found_element), 0, max_height_per_step
                )
                to_scroll -= max_height_per_step

                while to_scroll > 0:
                    if to_scroll > max_height_per_step:
                        actions.scroll_by_amount(0, max_height_per_step)
                        to_scroll -= max_height_per_step
                    else:
                        actions.scroll_by_amount(0, to_scroll)
                        to_scroll -= to_scroll
            else:
                actions.scroll_from_origin(
                    ScrollOrigin.from_element(found_element), 0, to_scroll
                )
            actions.perform()
    except selenium.common.exceptions.MoveTargetOutOfBoundsException:
        pass
