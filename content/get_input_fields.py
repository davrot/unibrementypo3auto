from selenium import webdriver
from selenium.webdriver.common.by import By


def get_input_fields(
    driver: webdriver.firefox.webdriver.WebDriver,
) -> tuple[list, list]:
    extract_list: list[str] = ["header", "date", "header_link", "subheader"]
    results: list = [None] * len(extract_list)
    found_element_list = driver.find_elements(By.TAG_NAME, "input")

    for i in found_element_list:
        value = str(i.get_attribute("value"))
        temp_str = i.get_dom_attribute("data-formengine-input-name")
        if temp_str is not None:
            data_lines = temp_str.split("[")
            if len(data_lines) > 0:
                data = data_lines[-1]
                if len(data) > 1:
                    data = data[:-1]
        else:
            data = None

        try:
            idx = extract_list.index(data)
        except ValueError:
            idx = None

        if idx is not None:
            results[idx] = value

    return extract_list, results
