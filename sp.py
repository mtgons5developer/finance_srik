import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Start
super_proxy = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.scheler.superproxy",
    "appium:appActivity": "com.scheler.superproxy.activity.MainActivity"
}

xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
id = "element-6066-11e4-a52e-4f735466cecf"
# Create a new instance of the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", super_proxy)

# elements = driver.find_elements("class name", "android.widget.Button")
# print(elements[0])
# my_string = str(elements[0])
# substring = "element="

# index = my_string.find(substring)

# if index != -1:
#     print("Substring found at index:", index)
#     new_string = my_string[index+9:]
#     new_string = new_string[:-3]
#     els1 = driver.find_elements(by=AppiumBy.ID, value=new_string)
#     els2 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
#     els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
#     els4 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
#     els4[0].click()

# else:
#     print("Substring not found.")

els1 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
els1[0].click()

els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]")
els3[0].click()

actions = ActionChains(driver)
actions.send_keys("node-ru-160.astroproxy.com")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1) 
actions.send_keys(Keys.ENTER)
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()

actions.send_keys("10065")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1) 
actions.send_keys(Keys.TAB)
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()

actions.send_keys("albertobattiato1792")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1) 
actions.send_keys(Keys.ENTER)
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()

actions.send_keys("a65d47")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1) 
actions.send_keys(Keys.ENTER)
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()

els1 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
els1[1].click()

els1 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
els1[2].click()

time.sleep(10)
