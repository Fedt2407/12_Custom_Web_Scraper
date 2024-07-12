# Description: This script scrapes the Diesel website for denim products and prints the name and price of each product.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configura Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get('https://it.diesel.com/it/uomo/abbigliamento/')

# Wait for the page to load
time.sleep(3)

# Prepare the CSV file
csv_file = './csv_data/diesel_products.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Name', 'Price'])

    # Find the search input field
    containers = driver.find_elements(By.CSS_SELECTOR, '.container-price-name-carousel')
    for container in containers:
        try:
            # Find the name of the product
            name_element = container.find_element(By.CSS_SELECTOR, '.product-tile-body__link')
            name = name_element.text
            
            # Find the price of the product
            price_element = container.find_element(By.CSS_SELECTOR, '.product-tile-body__price .value')
            price = price_element.text
            
            # Write the product details to the CSV file
            writer.writerow([name, price])
        except Exception as e:
            print(f'Error: {e}')

# Close the browser
driver.quit()

