import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from content.change_url import change_url
from content.press_wizzard_button import press_wizzard_button
from content.get_list_wizard_sections import get_list_wizard_sections
from content.set_wizard_section import set_wizard_section
from content.get_list_wizard_sections_tools import get_list_wizard_sections_tools

page_id: int = 59492
base_url: str = "https://www.uni-bremen.de"

zfn_password: str = getpass()

with open("username.json", "r") as file:
    json_dict = json.load(file)
zfn_user: str = json_dict["zfn_user"]

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Login
if login(driver, base_url, zfn_user, zfn_password) is False:
    print("Login failed")
    exit(1)

# Get rid of the popup
close_login_popup(driver)

# Get the protected URL to the pages
page_url_base = get_layout_url(driver, base_url)

# Change to page
page_url: str = page_url_base + f"&id={int(page_id)}"
change_url(driver, page_url)

press_wizzard_button(driver)

active_element, labels = get_list_wizard_sections(driver)

for section_id in range(0, len(labels)):
    # Switch to Raster-Elemente
    set_wizard_section(driver, labels[section_id])

    center_x, center_y, content_name, image_name = get_list_wizard_sections_tools(
        driver
    )
    print(f"Tools in {labels[section_id]}")
    for i in range(0, len(center_x)):
        print(f"{content_name[i]} ({image_name[i]}) => ({center_x[i]},{center_y[i]})")
    print()

print("Close shop")
driver.close()
driver.quit()
