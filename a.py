from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Set up desired capabilities
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '37J9K22916020862'
desired_caps['appPackage'] = 'com.facebook.katana' # package name for Facebook app
desired_caps['appActivity'] = 'com.facebook.katana.LoginActivity' # activity name for Facebook app

# Set up Appium server URL
appium_url = 'http://localhost:4723/wd/hub'

# Create Appium driver instance
driver = webdriver.Remote(appium_url, desired_caps)

# time.sleep(20)
# assume you have created an instance of Appium webdriver as 'driver'
element = driver.find_element("email")
driver.send_keys("user@example.com")

# # create a TouchAction object
# touch_action = TouchAction(driver)

# # move the mouse to the center of the element
# touch_action.move_to(element).perform()

# # perform a click on the element
# touch_action.tap().perform()

# # # Wait for Facebook app to load
# # login_button = driver.find_element('com.facebook.katana:id/1c693ab7-4adc-4f60-93e5-07a84fc5167d')
# # login_button.click()

# # # Enter login credentials
# # username_field = driver.find_element('com.facebook.katana:id/login_username')
# # username_field.send_keys('YOUR_USERNAME')
# # password_field = driver.find_element('com.facebook.katana:id/login_password')
# # password_field.send_keys('YOUR_PASSWORD')
# # login_button = driver.find_element('com.facebook.katana:id/login_login')
# # login_button.click()

# # # Wait for Facebook feed to load
# # feed_element = driver.find_element('com.facebook.katana:id/news_feed_tab')
