from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback


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
wait = WebDriverWait(driver, 10)

# List of websites and credentials
site = {'url': 'https://app.datadoghq.com/ci/dora/settings', 'username': 'jf7r3lqrm7@ddtraining.datadoghq.com', 'password': 'd9a1b@78cD'}

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

if "/ci/dora/settings" in new_url: 
    print("Login successful... We are on the DORA Setting Page.")
else:
    print("Login might have failed, still on the login page.")

# Click the two datadog-ci CLI / API buttons
try:
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="single-page-app_layout_page__main-content"]/div/div/div[2]/div/div[1]/div[2]/button')))
    print(button)
    button.click()

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="single-page-app_layout_page__main-content"]/div/div/div[4]/div/div[1]/div[2]/button')))
    print(button)
    button.click()

    # Click on Save & View Metrics buttons
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="single-page-app_layout_page__main-content"]/div/div/div[5]/button')))
    print(button)
    button.click()

    new_url = driver.current_url
    print(f"Current URL: {new_url}")

    if "settings" not in new_url: 
        print("DORA Settings Applied Successfully!")
    else:
        print("Failed applying DORA Settings!")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

# Close the driver
driver.quit()