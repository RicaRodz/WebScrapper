import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_table(driver):
    
    # Locate the table on the page
    table = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )

    rows = []
    if table:
        # then we can iterate through each row and extract either header or row values:
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            rows.append([el.text.strip() for el in row.find_elements(By.TAG_NAME, 'td')])

        # Create a CSV file and write data
        with open('test.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)   
         

    else:
        print('table was not found')


def scrape_card(driver):

    # Locate Card to scrape
    card_group_presence = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-group'))
    )

    card_group = driver.find_element(By.CLASS_NAME, 'card-group')
    
    cards = card_group.find_elements(By.TAG_NAME, 'div')
    ctr = 1
    rows = []
    for card in cards:
        if card.get_attribute("class") == 'col-12 col-lg-6 m-b-lg':
            print("Found card", ctr)
            row = []
            ctr+=1
            a_links = card.find_elements(By.TAG_NAME, 'a')
            for a in a_links:
                if a.get_attribute('class') == 'white w-500 m-b-0 nullref':
                    row.append(a.text.strip())
                    break
            information = card.find_elements(By.TAG_NAME, 'p')
            p12counter = 0
            for p in information:
                if (p.get_attribute('class') in ['p-v2 p-12 p-icon-press', 'p-v2 p-11 p-icon-press', 'p-13 m-h-0 p-r-sm']):
                    if p.text.strip() == 'MÉTRICAS SEO':
                        break
                    else:
                        row.append(p.text.strip())
            rows.append(row)
                    

    with open('Card_Data_Test.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)

    # Print the final result after the outer loop
    

            

