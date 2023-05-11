import json
from selenium import webdriver


def get_tree(
    driver: webdriver.firefox.webdriver.WebDriver,
    base_url: str,
) -> list:
    data_elements = str(driver.page_source).split('"')

    lost_and_found = []
    for element in data_elements:
        if (
            str(element).find(
                "index.php?route=%2Fajax%2Fpage%2Ftree%2FfetchData&token="
            )
            != -1
        ):
            lost_and_found.append(element)

    assert len(lost_and_found) == 1
    ajax_url = base_url + str(lost_and_found[0]).replace("\\", "")

    backup_url = driver.current_url
    driver.get(ajax_url)

    data = str(driver.page_source)
    data_lines = data.split('<div id="json">')

    assert len(data_lines) == 2
    data = data_lines[1]

    data_lines = data.split("</div>")
    assert len(data_lines) > 0
    data = data_lines[0]

    page_dict = json.loads(data)

    driver.get(backup_url)

    return page_dict
