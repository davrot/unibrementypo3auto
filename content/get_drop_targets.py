from selenium import webdriver
from selenium.webdriver.common.by import By


def get_drop_targets(
    driver: webdriver.firefox.webdriver.WebDriver,
) -> tuple[list[int], list[int], list[str]]:
    find_string_id_1: str = "colpos-"
    find_string_image_1: str = "actions-add.svg"

    found_element_list = driver.find_elements(By.TAG_NAME, "div")

    center_x: list[int] = []
    center_y: list[int] = []
    id_name: list[str] = []

    for i in found_element_list:
        if str(i.get_dom_attribute("id")).startswith(find_string_id_1):
            found_child_list = i.find_elements(By.TAG_NAME, "img")
            for j in found_child_list:
                src_info = j.get_dom_attribute("src")
                src_info = src_info.split("/")[-1]
                if str(src_info).startswith(find_string_image_1):
                    x = j.location["x"] + j.size["width"] // 2
                    y = j.location["y"] + j.size["height"] // 2
                    center_x.append(int(x))
                    center_y.append(int(y))
                    id_name.append(i.get_dom_attribute("id"))

    return center_x, center_y, id_name
