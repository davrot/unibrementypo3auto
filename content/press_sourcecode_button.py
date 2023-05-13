import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def press_sourcecode_button(driver: webdriver.firefox.webdriver.WebDriver):
    string_json_path: str = os.path.join("content", "press_sourcecode_button.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    # Press source code button
    found_element_list = driver.find_elements(By.TAG_NAME, "a")
    for i in found_element_list:
        temp_str = str(i.get_dom_attribute("title"))
        if temp_str.find(string_dict["lable_for_source_code_button"]) != -1:
            while (
                str(i.get_dom_attribute("class")).find(
                    string_dict["end_state_button_class"]
                )
                == -1
            ):
                i.click()
            break
