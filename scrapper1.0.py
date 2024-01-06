import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password):
    # Navigate to the login page
    driver.get('https://www.publisuites.com/advertisers/en/')  # Replace with the actual login page URL
    time.sleep(2)  # Add a delay to let the page load

    # Find the username and password input fields and submit button

    # Replace with the actual name attribute of the username field
    username_field = driver.find_element(By.NAME, 'email')  
    # Replace with the actual name attribute of the password field
    password_field = driver.find_element(By.NAME, 'password')  
    # Replace with the actual name attribute of the submit button
    submit_button = driver.find_element(By.CLASS_NAME, "btn")  
    

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

    new_url = 'https://www.publisuites.com/advertisers/websites/'
    driver.get(new_url)
    
    time.sleep(5)
    
    # # Navigate to the table to scrape
    # target_href = "https://www.publisuites.com/advertisers/websites/"
    # click_specific_sidebar_element(target_href)





def click_specific_sidebar_element(target_href):
    # Replace with the logic to locate and click on the specific sidebar element
    # ul_list = driver.find_element(By.CLASS_NAME, 'app-menu')
    li_elements = driver.find_elements(By.CLASS_NAME, 'has-submenu')

    for li_element in li_elements:
        print(li_element)

        # a_element = li_element.find_element(By.CSS_SELECTOR, 'a')
        # if a_element.get_attribute('href') == target_href:
        #     a_element.click()
        #     print('element found')
        #     break



def scrape_table():

    soup = BeautifulSoup(driver.page_source, 'html.parser')
     
    # Locate the table on the page
    table = driver.find_element(By.CLASS_NAME, 'table')

    if table:
        # Extract data from the entire table, including the header and body
        data = []
        for row in table.find_all('tr'):
            columns = row.find_all(['th', 'td'])  # Include both th (header) and td (body) elements
            row_data = [column.text.strip() for column in columns]
            data.append(row_data)

        # Create a CSV file and write data
        with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(data)
    else:
        print('table was not found')




# Set the initial URL
base_url = 'https://www.publisuites.com/advertisers/en/'
login_username = 'gserangelo@gmail.com'
login_password = 'rl2023'

# Set up the Safari webdriver (replace '/path/to/safaridriver' with the actual path)
driver = webdriver.Safari()

# Log in to the website
login(login_username, login_password)



driver.quit()

