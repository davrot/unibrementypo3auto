import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def login(
    driver: webdriver.firefox.webdriver.WebDriver,
    base_url: str,
    zfn_user: str,
    zfn_password: str,
) -> bool:
    assert len(base_url) > 0
    assert len(zfn_user) > 0
    assert len(zfn_password) > 0

    string_json_path: str = os.path.join("login", "login.json")

    with open(string_json_path, "r") as file:
        string_dict = json.load(file)

    login_url: str = base_url + string_dict["login_url"]

    # Login
    driver.get(login_url)
    print_new_line: bool = False
    while driver.current_url != login_url:
        print(".", end="")
        time.sleep(1)
        print_new_line = True

    if print_new_line is True:
        print()

    login_name_list = driver.find_elements(By.ID, string_dict["user_name_id"])
    login_password_list = driver.find_elements(By.ID, string_dict["user_password_id"])
    login_button_list = driver.find_elements(By.ID, string_dict["user_button_id"])

    if (
        (len(login_name_list) != 1)
        and (len(login_password_list) != 1)
        and (len(login_button_list) != 1)
    ):
        return False

    login_name = login_name_list[0]
    login_password = login_password_list[0]
    login_button = login_button_list[0]

    while (login_name.get_attribute("value") != zfn_user) or (
        login_password.get_attribute("value") != zfn_password
    ):
        login_name.clear()
        login_password.clear()
        login_name.send_keys(zfn_user)
        login_password.send_keys(zfn_password)
        time.sleep(1)

    login_button.click()
    while driver.current_url == login_url:
        print(".", end="")
        time.sleep(1)
        print_new_line = True

    if print_new_line is True:
        print()

    if str(driver.current_url).startswith(base_url + string_dict["bad_url"]) is True:
        return False

    return True
