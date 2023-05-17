import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def press_wizzard_button(driver: webdriver.firefox.webdriver.WebDriver):
    string_json_path: str = os.path.join("content", "press_wizzard_button.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    wizard_open: bool = False
    found_element_list = driver.find_elements(By.TAG_NAME, "div")
    for i in found_element_list:
        if str(i.get_dom_attribute("id")) == string_dict["wizard_open"]:
            wizard_open = True
            break

    while wizard_open is False:
        found_element_list = driver.find_elements(By.TAG_NAME, "a")
        for i in found_element_list:
            temp_str = str(i.get_dom_attribute("title"))
            if temp_str.find(string_dict["wizard_button"]) != -1:
                i.click()
                break

        time.sleep(2)
        found_element_list: list = ["not empty"]  # type: ignore
        while len(found_element_list) > 0:
            found_element_list = driver.find_elements(By.TAG_NAME, "button")
            for i in found_element_list:
                temp_str = str(i.get_dom_attribute("class"))

                if temp_str.find(string_dict["wizard_button_close"]) != -1:
                    i.click()
                    found_element_list = ["not empty"]  # type: ignore
                    break
            time.sleep(1)
            found_element_list = []

        found_element_list = driver.find_elements(By.TAG_NAME, "div")
        for i in found_element_list:
            if str(i.get_dom_attribute("id")) == string_dict["wizard_open"]:
                wizard_open = True
                break
