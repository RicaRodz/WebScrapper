import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password):
    # Navigate to the login page
    driver.get('https://www.publisuites.com/en/login/')  # Replace with the actual login page URL
    time.sleep(5)  # Add a delay to let the page load

    # Check if a pop-up is present (replace with the actual conditions for your pop-up)
    try:
        pop_up = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'didomi-popup'))
        )

        # Handle the pop-up (replace with the actual actions you want to perform)
        accept_button = pop_up.find_element(By.ID, 'didomi-notice-agree-button')
        accept_button.click()
        

    except:
        pass # No pop-up found or timed out waiting for the pop-up


    # Find the username and password input fields and submit button
    username_field = driver.find_element(By.NAME, 'email')  
    password_field = driver.find_element(By.NAME, 'password')  
    submit_button = driver.find_element(By.CLASS_NAME, "submitbuttonadvertisers")  
    
    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the submit button
    submit_button.click()

    # Wait for the login to complete (you might need to adjust the conditions)
    WebDriverWait(driver, 10).until(
        # Replace with the URL that changes after successful login
        EC.url_changes('https://www.publisuites.com/advertisers/')
    )

    time.sleep(5)


def click_specific_sidebar_element(target_href):
    time.sleep(5)
    # Look for the specific link where the table is, by gathering all 'a' elements
    a_elements = driver.find_elements(By.TAG_NAME, 'a')

    for a_element in a_elements:
        if a_element.get_attribute('href') == target_href:
            a_element.click()
            break

    # Wait for url to change
    WebDriverWait(driver, 10).until(
        EC.url_to_be(target_href)
    )

    # Open table for scraping
    table_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'fa-grip-lines'))
        )
    table_button.click()
    time.sleep(5)
    

def scrape_table():
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # try chatch error -- Must continue/wait for table to load
    # Locate the table on the page
    table = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'table')))

    
    rows = []
    if table:
        # then we can iterate through each row and extract either header or row values:
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            rows.append([el.text.strip() for el in row.find_elements(By.TAG_NAME, 'td')])
        

        # Scrape pop up information
        a_elements = driver.find_elements(By.TAG_NAME, 'a')
        for a in a_elements:
            if a.get_attribute('class') == 'btn btn-black-v2 btn-xs blank pointer':
                try:
                    a.click()
                    # Wait for pop up to load
                    pop_up = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'modal-content'))
                    )
                except:
                    pass

        # Scrape all 'p' elements
        pop_up = driver.find_element(By.CLASS_NAME, 'modal-content')
        info = pop_up.find_elements(By.TAG_NAME, 'p')
        for text in info:
            print(text.text())
            # Description
            # if text.get_attribute("class") == 'p-v2 p-11' or text.get_attribute("class") == 'p-v2 p-11 m-b-0' or text.get_attribute("class") == 'p-v2 p-11 p-icon-press' or text.get_attribute("class") == 'p-v2 p-12 p-icon-press':
            #    rows.append(text.text())
                # print(text.text())


        # Country and Language
        # Links:
            # Max Links
            # Sponsored
            # Follow
        # Places of Publication:
            # Main Page
            # Related Categories
        # Max Number of Images
        


        # Categories
        # Topics not Accepted

        # Extend info to rows



        # Create a CSV file and write data
        # with open('test.csv', 'a', newline='', encoding='utf-8') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerows(rows)        

    else:
        print('table was not found')




# Set the initial URL
base_url = 'https://www.publisuites.com/advertisers/en/'
login_username = 'gserangelo@gmail.com'
login_password = 'rl2023'

# Set up the Safari webdriver (replace '/path/to/safaridriver' with the actual path)
driver = webdriver.Safari()
driver.set_window_size(1400, 900)

# Log in to the website
login(login_username, login_password)

# Access table page
target_href = 'https://www.publisuites.com/advertisers/websites/'
click_specific_sidebar_element(target_href)

scrape_table()

# # Stopped at 358
# for number in range(2, 5):
#     time.sleep(5)
#     scrape_table()
#     pages = driver.find_elements(By.CLASS_NAME, 'page-item')
#     for page in pages:
#         if page.text == str(number):
#             print("page clicked", " ", number)

#             # Click on the link
#             tag = page.find_element(By.TAG_NAME, 'a')
#             tag.click()

#             break

#     time.sleep(5)


# driver.quit()

