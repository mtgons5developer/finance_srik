import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define proxy server settings
proxy_username = "albydsq"
proxy_password = "5aLhh7kg4pELLx"
proxy_server = "s4.airproxy.io:20209"

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

# Define Facebook login credentials
setProxy()
email = "13152391975"
password = "Jejelab"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server={}'.format(proxy_server))
# chrome_options.add_argument('--proxy-auth={}:{}'.format(proxy_username, proxy_password))

# Create webdriver object with ChromeOptions and navigate to Facebook login page
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com/login')

# Wait for the email input to become visible
email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="email"]')))

# Enter email and password and submit the login form
email_input.send_keys(email)
password_input = driver.find_element(By.CSS_SELECTOR, '[id="pass"]')
password_input.send_keys('Jejelab')
login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
login_button.click()

driver.implicitly_wait(10)
# Verify that login was successful
assert "Facebook" in driver.title
time.sleep(200)
driver.quit()
