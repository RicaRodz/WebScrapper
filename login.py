import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password, driver):
    # Navigate to the login page
    driver.get('https://www.publisuites.com/en/login/')  # Replace with the actual login page URL
    time.sleep(5)  # Add a delay to let the page load

    # Check if a pop-up is present (replace with the actual conditions for your pop-up)
    try:
        pop_up = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'didomi-popup'))
        )

        # Handle the pop-up (replace with the actual actions you want to perform)
        accept_button = pop_up.find_element(By.ID, 'didomi-notice-agree-button')
        accept_button.click()
        

    except:
        # No pop-up found or timed out waiting for the pop-up
        pass


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
    WebDriverWait(driver, 20).until(
        # Replace with the URL that changes after successful login
        EC.url_changes('https://www.publisuites.com/advertisers/')
    )

    time.sleep(10)
