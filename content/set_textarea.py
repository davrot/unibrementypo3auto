import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


def set_textarea(
    driver: webdriver.firefox.webdriver.WebDriver, content_id: int, new_text: str | None
):
    if new_text is None:
        return

    string_json_path: str = os.path.join("content", "set_textarea.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    target_textarea: str = (
        f"{string_dict['segment_pre']}{content_id}{string_dict['segment_post']}"
    )
    found_element_list = driver.find_elements(By.TAG_NAME, "textarea")

    for i in found_element_list:
        temp_str = str(i.get_dom_attribute("title"))

        if temp_str.find(target_textarea) != -1:
            while i.get_attribute("value") != new_text:
                i.clear()
                i.send_keys(new_text)
            break

    return
