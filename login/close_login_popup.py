import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def close_login_popup(driver: webdriver.firefox.webdriver.WebDriver):
    string_json_path: str = os.path.join("login", "close_login_popup.json")

    time.sleep(1)

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    evil_element_found: bool = True
    while evil_element_found is True:
        found_element_list = driver.find_elements(By.TAG_NAME, "button")
        evil_element_found = False
        for found_element in found_element_list:
            if found_element.get_dom_attribute("class") == string_dict["button_class"]:
                evil_element_found = True
                found_element.click()
                time.sleep(1)
                break
