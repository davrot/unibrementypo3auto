import json
from login.login import login
from login.close_login_popup import close_login_popup

from get_tree.get_layout_url import get_layout_url

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService


from webdriver_manager.firefox import GeckoDriverManager
from content.change_url import change_url

from content.get_xy_singlegrid import get_xy_singlegrid
from content.get_xy_tab import get_xy_tab
from content.get_xy_textmedia import get_xy_textmedia

from content.get_drop_targets import get_drop_targets
from content.make_drop_map import make_drop_map
from content.get_content_list import get_content_list
from content.press_save_button import press_save_button
from content.press_close_button import press_close_button
from content.set_input_field import set_input_field
from content.scroll_down_content_page import scroll_down_content_page
from content.action_chain_drag_and_drop import action_chain_drag_and_drop

import numpy as np

import time


def main(
    driver: webdriver.firefox.webdriver.WebDriver,
    zfn_user: str,
    zfn_password: str,
    page_id: int,
    base_url: str,
):
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

    # ###########################################################
    # Make outer grid
    # ###########################################################

    scroll_down_content_page(driver)
    x_from, y_from = get_xy_singlegrid(driver)
    center_x, center_y, _ = get_drop_targets(driver)
    organization_matrix = make_drop_map(center_x, center_y)
    # Last line
    temp = organization_matrix[-1, :]
    # first element
    idx = np.where(temp >= 0)[0]
    id = temp[idx][0]
    action_chain_drag_and_drop(driver, x_from, y_from, center_x[id], center_y[id])
    time.sleep(1)

    # ###########################################################
    # Make tab
    # ###########################################################

    scroll_down_content_page(driver)
    x_from, y_from = get_xy_tab(driver)
    center_x, center_y, _ = get_drop_targets(driver)
    organization_matrix = make_drop_map(center_x, center_y)
    # 2. last line
    temp = organization_matrix[-2, :]
    # first element
    idx = np.where(temp >= 0)[0]
    id = temp[idx][0]
    action_chain_drag_and_drop(driver, x_from, y_from, center_x[id], center_y[id])
    time.sleep(1)

    # ###########################################################
    # Make textmedia elements
    # ###########################################################

    with open("types_db.json", "r") as file:
        type_dict = json.load(file)

    for t_element in type_dict.keys():
        assert len(type_dict[t_element]) == 3

        # Make textmedia
        content_id_pre, _, _ = get_content_list(driver)
        scroll_down_content_page(driver)
        x_from, y_from = get_xy_textmedia(driver)
        center_x, center_y, _ = get_drop_targets(driver)
        organization_matrix = make_drop_map(center_x, center_y)

        # 2. last line
        temp = organization_matrix[-3, :]
        # first element
        idx = np.where(temp >= 0)[0]
        id = temp[idx][0]
        action_chain_drag_and_drop(driver, x_from, y_from, center_x[id], center_y[id])
        time.sleep(2)

        the_length: int = 0
        while the_length == 0:
            content_id_post, content_type, urls = get_content_list(driver)
            new_item_list = list(set(content_id_post) - set(content_id_pre))
            the_length = len(new_item_list) == 1
            if the_length != 1:
                time.sleep(1)
                print(".")

        idx_id: int = content_id_post.index(new_item_list[0])
        assert content_type[idx_id] == "textmedia"
        change_url(driver, base_url + urls[idx_id])

        new_header_text: str | None = type_dict[t_element][1]
        set_input_field(driver, str("header"), new_header_text)
        # Press save button
        time.sleep(1)
        press_save_button(driver)

        # Press close button
        time.sleep(1)
        press_close_button(driver)

        time.sleep(1)

    # ###########################################################


page_id: int = 59285
base_url: str = "https://www.uni-bremen.de"

zfn_password: str = getpass()

with open("username.json", "r") as file:
    json_dict = json.load(file)
zfn_user: str = json_dict["zfn_user"]


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

main(
    driver,
    zfn_user,
    zfn_password,
    page_id,
    base_url,
)

print("Close shop")
driver.close()
driver.quit()
