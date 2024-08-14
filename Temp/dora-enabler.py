from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Path to your ChromeDriver
webdriver_path = '/usr/local/bin/chromedriver'

# List of websites and credentials
websites = [
    {'url': 'https://app.datadoghq.com/account/login', 'username': 'jf7r3lqrm7@ddtraining.datadoghq.com', 'password': 'd9a1b@78cD'},
    # Add more websites and credentials as needed
]

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

for site in websites:
    driver.get(site['url'])
    
    # Example login process
    username_field = driver.find_element(By.ID, 'username') 
    password_field = driver.find_element(By.ID, 'password')  
    login_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in']") 

    username_field.send_keys(site['username'])
    password_field.send_keys(site['password'])
    login_button.click()
    
    time.sleep(5)  # Wait for the login process to complete

    new_url = driver.current_url
    print(f"Current URL: {new_url}")

    if "quick_start" in new_url: 
        print("Login successful, redirected to dashboard.")
    else:
        print("Login might have failed, still on the login page.")
    
    dora_url = "https://app.datadoghq.com/ci/dora/settings"

    # Click on datadog-ci CLI / API buttons
    buttons = driver.find_element(By.XPATH, "(//button[.//div[contains(text(), 'datadog-ci CLI / API')]])")
    if buttons:
        print(f"There are {len(buttons)} buttons found.")
        button[0].click()
    else:  
        print("No buttons found.")
    
    # Click on Save & View Metrics buttons
    button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Save & View Metrics']")
    button.click()
    time.sleep(2)  # Wait for the action to complete or for the page to load

# Close the driver
driver.quit()