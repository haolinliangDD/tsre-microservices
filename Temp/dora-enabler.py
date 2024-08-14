from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


# Initialize the WebDriver
webdriver_path = '/usr/local/bin/chromedriver'
service = Service(webdriver_path)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging

driver = webdriver.Chrome(service=service, options=chrome_options)

# List of websites and credentials
site = {'url': 'https://app.datadoghq.com/account/login', 'username': 'jf7r3lqrm7@ddtraining.datadoghq.com', 'password': 'd9a1b@78cD'}

driver.get(site['url'])

# Example login process
username_field = driver.find_element(By.ID, 'username') 
password_field = driver.find_element(By.ID, 'password')  
login_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in']") 

username_field.send_keys(site['username'])
password_field.send_keys(site['password'])
login_button.click()

time.sleep(2)  # Wait for the login process to complete

new_url = driver.current_url
print(f"Current URL: {new_url}")

if "quick_start" in new_url: 
    print("Login successful, redirected to dashboard.")
else:
    print("Login might have failed, still on the login page.")

dora_url = "https://app.datadoghq.com/ci/dora/settings"

print(f"Switching to DORA Setting Page: {dora_url}")
driver.get(dora_url)

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