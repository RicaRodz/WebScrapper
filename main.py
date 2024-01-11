from buttons import media_btn
import time
from login import login
from scrapper import scrape_table, scrape_card
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the initial URL
base_url = 'https://www.publisuites.com/advertisers/en/'
login_username = 'gserangelo@gmail.com'
login_password = 'rl2023'

# Set up the Safari webdriver (replace '/path/to/safaridriver' with the actual path)
driver = webdriver.Safari()
driver.set_window_size(1400, 900)

# Log in to the website
login(login_username, login_password, driver)

# Access table page
target_href = 'https://www.publisuites.com/advertisers/websites/'
media_btn(target_href, driver)

# Scrape Cards
for number in range(2, 515):
    scrape_card(driver)
    pages = driver.find_elements(By.CLASS_NAME, 'page-item')
    for page in pages:
        if page.text == str(number):
            print("page scraped", " ", number)
            # Click on the link
            tag = page.find_element(By.TAG_NAME, 'a')
            tag.click()
            time.sleep(2)

            break



# Scrape Table

# for skip in range(2, 299):

#     page_list = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'page-item'))
#     )

#     pages = driver.find_elements(By.CLASS_NAME, 'page-item')
#     time.sleep(2)
#     for page in pages:
#         if page.text == str(skip):
#             print("page skipped", " ", skip)
#             # Click on the link
#             tag = page.find_element(By.TAG_NAME, 'a')
#             tag.click()

#             break


# for number in range(2,515):
    
#     scrape_table(driver)
#     pages = driver.find_elements(By.CLASS_NAME, 'page-item')
#     for page in pages:
#         if page.text == str(number):
#             print("page scraped", " ", number-1)
#             # Click on the link
#             tag = page.find_element(By.TAG_NAME, 'a')
#             tag.click()
#             break

#     time.sleep(2)

    


driver.quit()

