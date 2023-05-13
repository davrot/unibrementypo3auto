import time
from selenium import webdriver


def change_url(driver: webdriver.firefox.webdriver.WebDriver, new_url: str):
    # Login
    driver.get(new_url)
    print_new_line: bool = False
    while driver.current_url != new_url:
        print(".", end="")
        time.sleep(1)
        print_new_line = True

    if print_new_line is True:
        print()
    time.sleep(1)
