import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_list_wizard_sections(
    driver: webdriver.firefox.webdriver.WebDriver,
) -> tuple[int | None, list[str]]:
    string_json_path: str = os.path.join("content", "get_list_wizard_sections.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    found_element_list = driver.find_elements(By.TAG_NAME, "li")
    active_element: None | int = None
    labels: list[str] = []

    for i in found_element_list:
        if str(i.get_dom_attribute("class")).startswith(string_dict["tabmenu-item"]):
            if str(i.get_dom_attribute("class")).find(string_dict["active-item"]) != -1:
                active_element = len(labels)
            labels.append(i.text)

    return active_element, labels
