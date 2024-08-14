from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# Path to your ChromeDriver
webdriver_path = '/path/to/chromedriver'

# List of websites and credentials
websites = [
    {'url': 'http://example1.com', 'username': 'user1', 'password': 'pass1'},
    {'url': 'http://example2.com', 'username': 'user2', 'password': 'pass2'},
    # Add more websites and credentials as needed
]

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

for site in websites:
    driver.get(site['url'])
    
    # Example login process
    username_field = driver.find_element(By.ID, 'username')  # Adjust the selector to match your website
    password_field = driver.find_element(By.ID, 'password')  # Adjust the selector to match your website
    login_button = driver.find_element(By.ID, 'login')  # Adjust the selector to match your website

    username_field.send_keys(site['username'])
    password_field.send_keys(site['password'])
    login_button.click()
    
    time.sleep(2)  # Wait for the login process to complete

    # Example button click process
    button = driver.find_element(By.ID, 'button_id')  # Adjust the selector to match the button you want to click
    button.click()
    
    time.sleep(2)  # Wait for the action to complete or for the page to load

# Close the driver
driver.quit()