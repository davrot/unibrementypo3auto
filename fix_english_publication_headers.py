import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from content.get_content_list import get_content_list
from content.is_english_content import is_english_content
from content.change_url import change_url
from content.press_close_button import press_close_button
from content.get_input_fields import get_input_fields
from content.set_input_field import set_input_field
from content.press_save_button import press_save_button

import time

page_id: int = 59285
base_url: str = "https://www.uni-bremen.de"

zfn_password: str = getpass()

with open("username.json", "r") as file:
    json_dict = json.load(file)
zfn_user: str = json_dict["zfn_user"]

with open("types_db.json", "r") as file:
    type_dict = json.load(file)

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
time.sleep(1)

# Get content from page
content_id, content_type, urls = get_content_list(driver)

interesting_content_ids: list = []
for i in range(0, len(content_type)):
    if content_type[i] == "textmedia":
        interesting_content_ids.append(content_id[i])

time.sleep(1)
english_ids: list = []
for id in interesting_content_ids:
    if is_english_content(driver, id) is True:
        english_ids.append(id)

to_modify: str = str("header")

for id in english_ids:
    print(id)
    idx = content_id.index(id)
    assert idx is not None
    change_url(driver, base_url + urls[idx])

    extract_list, results = get_input_fields(driver)
    idx = extract_list.index(to_modify)
    value = results[idx]

    new_value: str | None = None
    for t_id in type_dict.keys():
        assert len(type_dict[t_id]) == 3
        if value == type_dict[t_id][1]:
            new_value = type_dict[t_id][2]

    if new_value is not None:
        set_input_field(driver, to_modify, new_value)

        # Press save button
        time.sleep(1)
        press_save_button(driver)

    # Press close button
    time.sleep(1)
    press_close_button(driver)
    print("Wait for 2 sec")
    time.sleep(2)

print("Close shop")
driver.close()
driver.quit()
