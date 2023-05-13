from selenium import webdriver
from selenium.webdriver.common.by import By


def set_input_field(
    driver: webdriver.firefox.webdriver.WebDriver,
    field_name: str | None,
    new_text: str | None,
):
    if (field_name is None) or (new_text is None):
        return

    found_element_list = driver.find_elements(By.TAG_NAME, "input")
    for i in found_element_list:
        temp_str = i.get_dom_attribute("data-formengine-input-name")
        if temp_str is not None:
            data_lines = temp_str.split("[")
            if len(data_lines) > 0:
                data = data_lines[-1]
                if len(data) > 1:
                    data = data[:-1]
        else:
            data = None
        if data == field_name:
            while i.get_attribute("value") != new_text:
                i.clear()
                i.send_keys(new_text)
            break

    return
