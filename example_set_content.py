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
from content.set_textarea import set_textarea
from content.press_save_button import press_save_button
from content.press_close_button import press_close_button
from content.set_input_field import set_input_field

import time

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

new_text: str | None = "A new Text for the textarea"
# "new_text = None" for do nothing
set_textarea(driver, content_id, new_text)

# field_name = None, "header", "subheader" (haven't tested "date", "header_link")
new_header_text: str | None = "A new header"
set_input_field(driver, str("header"), new_header_text)

new_header_text = "A new subheader"
set_input_field(driver, str("subheader"), new_header_text)


# Press save button
time.sleep(1)
press_save_button(driver)

# Press close button
time.sleep(1)
press_close_button(driver)

time.sleep(1)
print("Close shop")
driver.close()
driver.quit()
