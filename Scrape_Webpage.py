import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_source(url):
    driver = selenium.webdriver.Chrome()  # Chrome driver is being used.
    print("Requesting URL: " + url)

    driver.get(url)  # URL requested in browser.
    print("Webpage found ...")

    element_xpath = '//*[@id="left-side--wrapper"]/div[2]'  # First box with relevant flight data.

    # Wait until the first box with relevant flight data appears on Screen
    element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    # Scroll the page till bottom to get full data available in the DOM.
    print("Scrolling document upto bottom ...")
    for j in range(1, 100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    body = driver.page_source

    print("Closing Chrome ...")  # No more usage needed.
    driver.quit()  # Browser Closed.

    return body
