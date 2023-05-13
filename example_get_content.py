import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from content.get_content_list import get_content_list
from content.press_sourcecode_button import press_sourcecode_button
from content.change_url import change_url
from content.get_textarea import get_textarea
from content.press_close_button import press_close_button
from content.get_input_fields import get_input_fields


page_id: int = 59451
content_id: int = 517807
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
change_url(driver, page_url)

# Get content from page
content_id_list, content_type, urls = get_content_list(driver)

try:
    idx = content_id_list.index(content_id)
except ValueError:
    idx = None

print(f"Go to content {content_id}")

assert idx is not None
change_url(driver, base_url + urls[idx])

# Press source button
press_sourcecode_button(driver)

# Get content
testarea = get_textarea(driver, content_id)

print("Text found:")
print(testarea)

extract_list, results = get_input_fields(driver)
assert len(extract_list) == len(results)
for i in range(0, len(results)):
    print(f"{extract_list[i]}: {results[i]}")

# Press close button
press_close_button(driver)

print("Close shop")
driver.close()
driver.quit()
