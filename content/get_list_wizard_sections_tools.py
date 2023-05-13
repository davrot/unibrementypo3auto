from selenium import webdriver
from selenium.webdriver.common.by import By


def get_list_wizard_sections_tools(
    driver: webdriver.firefox.webdriver.WebDriver,
) -> tuple[list[int], list[int], list[str], list[str]]:
    center_x: list[int] = []
    center_y: list[int] = []
    content_name: list[str] = []
    image_name: list[str] = []

    found_element_list = driver.find_elements(By.TAG_NAME, "div")
    for i in found_element_list:
        if str(i.get_dom_attribute("class")).startswith("tab-pane active"):
            found_child_list = i.find_elements(By.TAG_NAME, "span")

            for j in found_child_list:
                if str(j.get_dom_attribute("class")).find("t3js-icon") != -1:
                    content = str(j.get_dom_attribute("class"))
                    content = content.split(" ")[-1]
                    content_name.append(content)

                    found_img_list = j.find_elements(By.TAG_NAME, "img")
                    assert len(found_img_list) == 1
                    found_img = found_img_list[0]
                    src_info = found_img.get_dom_attribute("src")
                    src_info = src_info.split("/")[-1]
                    image_name.append(src_info)

                    x = found_img.location["x"] + found_img.size["width"] // 2
                    y = found_img.location["y"] + found_img.size["height"] // 2
                    center_x.append(int(x))
                    center_y.append(int(y))

    return center_x, center_y, content_name, image_name
