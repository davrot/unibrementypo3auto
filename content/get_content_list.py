from selenium import webdriver
from selenium.webdriver.common.by import By


def get_content_list(
    driver: webdriver.firefox.webdriver.WebDriver,
) -> tuple[list, list, list]:
    find_string_1: str = "/typo3/index.php?route=%2Frecord%2Fedit&token="
    find_string_2: str = "#element-tt_content-"
    find_string_3: str = "element-tt_content-"

    lost_and_found: list = []
    content_id: list = []
    urls: list = []
    found_element_list = driver.find_elements(By.TAG_NAME, "a")
    for found_element in found_element_list:
        if (
            (found_element.get_dom_attribute("href") is not None)
            and (
                str(found_element.get_dom_attribute("href")).startswith(find_string_1)
                is True
            )
            and (str(found_element.get_dom_attribute("href")).find(find_string_2) != -1)
        ):
            lost_and_found.append(found_element)
            data = str(found_element.get_dom_attribute("href")).split(find_string_2)
            assert len(data) == 2
            content_id.append(int(data[1]))
            urls.append(str(found_element.get_dom_attribute("href")))

    content_type: list = [None] * len(content_id)

    found_element_list = driver.find_elements(By.TAG_NAME, "div")
    for found_element in found_element_list:
        if (
            (found_element.get_dom_attribute("id") is not None)
            and (
                str(found_element.get_dom_attribute("id")).startswith(find_string_3)
                is True
            )
            and (found_element.get_dom_attribute("data-ctype") is not None)
        ):
            id = str(found_element.get_dom_attribute("id")).split(find_string_3)
            assert len(id) == 2
            found_id = int(id[1])
            idx = content_id.index(found_id)
            content_type[idx] = str(found_element.get_dom_attribute("data-ctype"))

    assert len(content_id) == len(content_type)
    assert len(content_id) == len(urls)

    return (content_id, content_type, urls)
