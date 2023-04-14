from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

def setProxy():
    # Set up the proxy server URL
    proxy_url = 'http://albydsq:5aLhh7kg4pELLx@s4.airproxy.io:20209'

    # Make an HTTP request through the proxy server
    response = requests.get('http://www.example.com', proxies={'http': proxy_url, 'https': proxy_url})

    while 1:
        if response.status_code == 200:
            print('Request successful')
            break
        else:
            print('Request failed')

    time.sleep(1)

# Set proxy information
PROXY_HOST = "s4.airproxy.io"
PROXY_PORT = "20209"
PROXY_USER = "albydsq"
PROXY_PASS = "5aLhh7kg4pELLx"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s:%s' % (PROXY_HOST, PROXY_PORT))

# Set up proxy authentication
credentials = f"{PROXY_USER}:{PROXY_PASS}"
chrome_options.add_argument('--proxy-auth={}'.format(credentials))

# Set up Selenium Chrome webdriver with options
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to the Facebook login page
driver.get('https://www.facebook.com/login')
time.sleep(200)

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
