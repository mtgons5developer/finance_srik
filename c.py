import base64
import cv2
import pytesseract
import numpy as np
from appium import webdriver
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.mobileby import MobileBy, AppiumBy
from selenium.webdriver.common.keys import Keys

import time

# Set up desired capabilities
desired_caps = {
    # "platformName": "Android",
    # "appPackage": "com.facebook.katana",
    # "appActivity": "com.facebook.katana.LoginActivity",
    # "deviceName": "emulator-5554"
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "app": "/Users/datax/alberto/Facebook.apk",
    "appium:appPackage": "com.facebook.katana",
    "appium:appActivity": "com.facebook.katana.LoginActivity"    
}

# Create a new instance of the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def detectApp():

    if driver.current_activity == '.LoginActivity': 
        print('App is on top')
        status = 1
    else:
        print('App is not on top')
        status = 1

# try:
#     # Wait until element is visible
#     wait = WebDriverWait(driver, 30)
#     element = wait.until(EC.visibility_of_element_located((By.ID, '00000000-0000-0609-ffff-ffff00000012')))
#     print('Element is visible')
# except TimeoutException:
#     print('Element was not visible within 30 seconds')

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= 60:
        print("Error loading Login...")
        # driver.launch_app()
    elif elapsed_time > 5:
        #================================================================================================
        # Take a screenshot of the current screen
        screenshot = driver.get_screenshot_as_png()
        # Convert the screenshot to a NumPy array
        screenshot_array = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        # Crop a region of interest from the screenshot
        x, y, w, h = 55, 860, 500, 100
        roi = screenshot_array[y:y+h, x:x+w]
        # Apply some image processing to enhance the text
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        blurred = cv2.GaussianBlur(thresholded, (3, 3), 0)
        # Use Tesseract OCR to recognize the text in the region of interest
        text = pytesseract.image_to_string(blurred, lang='eng')
        # Tap on an element
        actions = ActionChains(driver)

        substring = "Mobile"

        if substring in text:
            print(text)
            print("Passed")
            actions.w3c_actions.pointer_action.move_to_location(x+430, y+40)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            break
        else:
            current_activity = driver.current_activity
            print("Current activity:", current_activity)   
            if driver.current_activity == 'com.facebook.account.login.activity.SimpleLoginActivity': 
                print('App is on top')
            else:
                print('App is not on top')
                driver.launch_app()
                time.sleep(3)
    else:
        print("Loading Login...")
    
    time.sleep(5)  # Pause for 1 second before next iteration

# Create a new instance of TouchAction
touch = TouchAction(driver)
time.sleep(5) #Email
actions.send_keys("09363312415")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1) #Password
actions.send_keys(Keys.DOWN)
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1)
actions.send_keys("potpot1234")
actions.w3c_actions.pointer_action.pause(0.1)
actions.perform()
time.sleep(1)
actions.w3c_actions.pointer_action.move_to_location(560, 956)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("Not now Starting")
actions.w3c_actions.pointer_action.move_to_location(555, 2040)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= 60:
        print("Error loading Not now...")
        # driver.launch_app()
    elif elapsed_time > 5:
        #================================================================================================
        # Take a screenshot of the current screen
        screenshot = driver.get_screenshot_as_png()
        # Convert the screenshot to a NumPy array
        screenshot_array = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        # Crop a region of interest from the screenshot
        x, y, w, h = 77, 1771, 415, 50
        roi = screenshot_array[y:y+h, x:x+w]
        # Apply some image processing to enhance the text
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        blurred = cv2.GaussianBlur(thresholded, (3, 3), 0)
        # Use Tesseract OCR to recognize the text in the region of interest
        text = pytesseract.image_to_string(blurred, lang='eng')
        # Tap on an element
        actions = ActionChains(driver)

        substring = "Not"

        if substring in text:
            print(text)
            print("Not now Passed")
            actions.w3c_actions.pointer_action.move_to_location(555, 2040)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            break
        else:
            current_activity = driver.current_activity
            print("Current activity:", current_activity)                 
            if driver.current_activity == 'com.facebook.bloks.facebook.loggedout.FbExperimentalLoggedOutBloksActivity': 
                print('App is on top')
                print(text)
            else:
                print('App is not on top')
                # driver.launch_app()
                # time.sleep(3)
    else:
        print("Loading Not now...")
        print(text)
    
    time.sleep(5)  # Pause for 1 second before next iteration


start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= 60:
        print("Error loading Notification...")
        # driver.launch_app()
    elif elapsed_time > 5:
        #================================================================================================
        # Take a screenshot of the current screen
        screenshot = driver.get_screenshot_as_png()
        # Convert the screenshot to a NumPy array
        screenshot_array = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        # Crop a region of interest from the screenshot
        x, y, w, h = 150, 1130, 415, 50
        roi = screenshot_array[y:y+h, x:x+w]
        # Apply some image processing to enhance the text
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        blurred = cv2.GaussianBlur(thresholded, (3, 3), 0)
        # Use Tesseract OCR to recognize the text in the region of interest
        text = pytesseract.image_to_string(blurred, lang='eng')
        # Tap on an element
        actions = ActionChains(driver)

        substring = "Deny"

        if substring in text:
            print(text)
            print("Notification Passed")
            actions.w3c_actions.pointer_action.move_to_location(540, 1400)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            break
        else:
            current_activity = driver.current_activity
            print("Current activity:", current_activity)     
            quit()              
            print('Notification error.')
            if driver.current_activity == '.LoginActivity': 
                print('App is on top')
            else:
                print('App is not on top')
                driver.launch_app()
                time.sleep(3)
    else:
        print("Loading Notification...")
    
    time.sleep(5)  # Pause for 1 second before next iteration

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= 60:
        print("Error loading Location...")
        # driver.launch_app()
    elif elapsed_time > 5:
        #================================================================================================
        # Take a screenshot of the current screen
        screenshot = driver.get_screenshot_as_png()
        # Convert the screenshot to a NumPy array
        screenshot_array = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        # Crop a region of interest from the screenshot
        x, y, w, h = 150, 1130, 415, 50
        roi = screenshot_array[y:y+h, x:x+w]
        # Apply some image processing to enhance the text
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        blurred = cv2.GaussianBlur(thresholded, (3, 3), 0)
        # Use Tesseract OCR to recognize the text in the region of interest
        text = pytesseract.image_to_string(blurred, lang='eng')
        # Tap on an element
        actions = ActionChains(driver)

        if text is not None:
            print(text)
            print("Location Passed")
            actions.w3c_actions.pointer_action.move_to_location(666, 1400)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            break
        else:
            print('Location error.')
            driver.launch_app()
            # quit()
    else:
        print("Loading Location...")
    
    time.sleep(5)  # Pause for 1 second before next iteration

quit()
# time.sleep(5) #GPS 85, 1970
actions.w3c_actions.pointer_action.move_to_location(659, 1465)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2) #OPTIONS
detectApp()
actions.w3c_actions.pointer_action.move_to_location(994, 317)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)
detectApp()
actions.w3c_actions.pointer_action.move_to_location(544, 1348)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(572, 279)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)
detectApp()
actions.w3c_actions.pointer_action.move_to_location(544, 1991)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)
detectApp()
actions.w3c_actions.pointer_action.move_to_location(508, 1747)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)
detectApp()
actions.w3c_actions.pointer_action.move_to_location(805, 681)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)
detectApp()
actions.w3c_actions.pointer_action.move_to_location(533, 1566)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(544, 428)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2) #FEEDBACK

while detectApp == "On Top":
    detectApp()

# driver.launch_app()

# Close app
# driver.close_app()

# Close the driver
driver.quit()