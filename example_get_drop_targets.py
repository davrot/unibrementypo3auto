import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from content.change_url import change_url
from content.get_drop_targets import get_drop_targets

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

# Extract the + target images
center_x, center_y, id_name = get_drop_targets(driver)

for i in range(0, len(id_name)):
    print(f"{id_name[i]} => ({center_x[i]}, {center_y[i]})")


print("Close shop")
driver.close()
driver.quit()
