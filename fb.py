import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options with proxy
chrome_options = Options()
chrome_options.add_argument("http://albydsq:5aLhh7kg4pELLx@s4.airproxy.io:20209")

# Set up Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Facebook login page
driver.get('https://www.facebook.com/login')

# Wait for the email input to become visible
email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="email"]')))

# Enter email and password and submit the login form
email_input.send_keys("13152391975")
password_input = driver.find_element(By.CSS_SELECTOR, '[id="pass"]')
password_input.send_keys('Jejelab')
login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
login_button.click()

driver.implicitly_wait(10)
# Verify that login was successful
assert "Facebook" in driver.title
time.sleep(200)
driver.quit()
