import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def media_btn(target_href, driver):
    # Look for the specific link where the table is, by gathering all 'a' elements
    a_elements = driver.find_elements(By.TAG_NAME, 'a')

    for a_element in a_elements:
        if a_element.get_attribute('href') == target_href:
            a_element.click()
            break

    # time.sleep(10)
    # # Open table for scraping
    # table_button = driver.find_element(By.CLASS_NAME, 'fa-grip-lines')
    # table_button.click()

    # time.sleep(5)
    