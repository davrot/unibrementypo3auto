import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from content.get_content_list import get_content_list

page_id: int = 59451
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

# Jump to page
print(f"Go to page {int(page_id)}")
page_url: str = page_url_base + f"&id={int(page_id)}"
driver.get(page_url)

# Get content from page
content_id, content_type, urls = get_content_list(driver)

for i in range(0, len(content_id)):
    print(content_id[i])
    print(content_type[i])
    print(base_url + urls[i])
    print()

print("Close shop")
driver.close()
driver.quit()
