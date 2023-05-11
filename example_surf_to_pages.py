import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import time

list_of_page_ids: list[int] = [59451, 59246]

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

for page_id in list_of_page_ids:
    print(f"Go to page {int(page_id)}")
    page_url: str = page_url_base + f"&id={int(page_id)}"
    driver.get(page_url)
    print("Wait for 5 sec")
    time.sleep(5)

print("Close shop")
driver.close()
driver.quit()
