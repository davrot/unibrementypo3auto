from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import json


def is_english_content(
    driver: webdriver.firefox.webdriver.WebDriver, content_id: int
) -> bool:
    string_json_path: str = os.path.join("content", "is_english_content.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    print(f"Is english? Check {content_id}")

    found_element_list = driver.find_elements(By.TAG_NAME, "div")

    for element in found_element_list:
        if str(element.get_dom_attribute("data-table")) == "tt_content":
            if str(element.get_dom_attribute("data-ctype")) == "textmedia":
                if str(element.get_dom_attribute("data-uid")) == str(content_id):
                    sub_element_list = element.find_elements(By.TAG_NAME, "img")
                    for sub_element in sub_element_list:
                        img_name = str(sub_element.get_dom_attribute("src"))
                        if img_name.endswith(string_dict["search_for_string"]):
                            return True

    return False
