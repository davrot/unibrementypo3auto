from selenium import webdriver


def get_layout_url(
    driver: webdriver.firefox.webdriver.WebDriver,
    base_url: str,
) -> str:
    data_elements = str(driver.page_source).split('"')

    lost_and_found = []
    for element in data_elements:
        if str(element).find("index.php?route=%2Fweb%2Flayout%2F&token=") != -1:
            lost_and_found.append(element)

    assert len(lost_and_found) > 0
    page_url = base_url + str(lost_and_found[0]).replace("\\", "")

    return page_url
