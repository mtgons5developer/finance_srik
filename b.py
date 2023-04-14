from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

# # Set desired capabilities for the Facebook app
desired_caps = {
    "platformName": "Android",
    "appPackage": "com.facebook.katana",
    "appActivity": "com.facebook.katana.LoginActivity",
    # "deviceName": "37J9K22916020862"
    "deviceName": "emulator-5554",
}

# Create an instance of the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Wait for the login page to appear
# email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
# ["xpath","//android.widget.EditText[contains(@text, 'Phone or email')]","c325076e-87aa-4dce-b022-7b2ddf40fb73"]
wait = WebDriverWait(driver, 20)
email_field = driver.find_element(by=MobileBy.XPATH, value=["xpath","//android.widget.EditText[contains(@text, 'Phone or email')]","c325076e-87aa-4dce-b022-7b2ddf40fb73"])

# element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))
# element.find_element(By.XPATH, "//input[@name='myInput']").click()

# Enter your email address into the field
email_field.send_keys("your_email_address@example.com")

# ====

# desired_caps = {
#   "platformName": "Android",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.facebook.katana",
#   "appActivity": "com.facebook.katana.LoginActivity",
#   "automationName": "UiAutomator2",
# }

# driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# time.sleep(20)
# # Find and interact with the email field
# # email_field = driver.find_element_by_xpath("//android.widget.EditText[contains(@text, 'Email address or phone number')]")
# # email_field = driver.find_element_by_xpath("//android.widget.EditText[contains(@text, 'Mobile number or email')]")
# email_field = driver2.find_element(by=MobileBy.XPATH, value="")

# email_field.send_keys("user@example.com")

