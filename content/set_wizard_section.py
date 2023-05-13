from selenium import webdriver
from selenium.webdriver.common.by import By
from content.get_list_wizard_sections import get_list_wizard_sections
import time


def set_wizard_section(
    driver: webdriver.firefox.webdriver.WebDriver, target: str | None
):
    if target is None:
        return

    active_element, labels = get_list_wizard_sections(driver)
    while labels[active_element] != target:
        found_element_list = driver.find_elements(By.TAG_NAME, "a")
        for i in found_element_list:
            if i.text == target:
                i.click()
                time.sleep(1)
                break

        active_element, labels = get_list_wizard_sections(driver)

    return
