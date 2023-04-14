import socket
import time
import requests
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import linecache

desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "app": "/Users/datax/alberto/Facebook.apk",
    "appium:appPackage": "com.facebook.katana",
    "appium:appActivity": "com.facebook.katana.LoginActivity",
    'unicodeKeyboard': True,  # enable Unicode keyboard
    # "udid": imei,
    # "udid": '358240051111110',
    'noReset': True,
    'fullReset': False,
    "networkConnectionEnabled": True,
    'autoGrantPermissions': True,
    "adbExecTimeout": 20000,   
}

# Create a new instance of the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 60)
# Create a new instance of TouchAction
actions = ActionChains(driver)
touch = TouchAction(driver)

def randomIMEI():
    # Open the file and get the total number of lines
    filename = 'imei.txt'
    with open(filename) as f:
        num_lines = sum(1 for line in f)

    # Get a random line number
    rand_line_num = random.randint(1, num_lines)

    # Get the random line using linecache
    imei = linecache.getline(filename, rand_line_num)
    return imei

def getComment():
    # Open the file and get the total number of lines
    filename = 'comments.txt'
    with open(filename) as f:
        num_lines = sum(1 for line in f)

    # Get a random line number
    rand_line_num = random.randint(1, num_lines)

    # Get the random line using linecache
    rand_line = linecache.getline(filename, rand_line_num)
    return rand_line

def detectApp(activity):

    if driver.current_activity == activity: 
        print('App is on top')
        status = 1
    else:
        print('App is not on top')
        status = 1

def rotateIP():
    #afcf3e522e2fedb25a3308bea3733873 - AdsPower
    #b60f35c853e9e30f - AstroProxy
    url = 'http://node-ru-160.astroproxy.com:10065/api/changeIP?apiToken=b60f35c853e9e30f'
    params = {'key': 'b60f35c853e9e30f'}

    response = requests.get(url)
    if response.status_code == 200:
        print('IP address rotated')
    else:
        print('Error rotating IP address:', response.text)

def rotateIP2():
    #afcf3e522e2fedb25a3308bea3733873 - AdsPower
    #b60f35c853e9e30f - AstroProxy
    url = 'https://airproxy.io/api/proxy/change_ip/?format=json&id=2011&key=0eiW2xiGcAmbPkZqDNmDWzEZqEekwlKi'
    params = {'key': 'b60f35c853e9e30f'}

    response = requests.get(url)
    if response.status_code == 200:
        print('IP address rotated')
    else:
        print('Error rotating IP address:', response.text)

def setProxy():
    # Set up the proxy server URL
    proxy_url = 'http://albertobattiato1792:a65d47@node-ru-160.astroproxy.com:10065'

    # Make an HTTP request through the proxy server
    response = requests.get('http://www.example.com', proxies={'http': proxy_url, 'https': proxy_url})

    while 1:
        if response.status_code == 200:
            print('Request successful')
            break
        else:
            print('Request failed')

    time.sleep(1)

def superProxy():
    #Start
    super_proxy = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.scheler.superproxy",
        "appium:appActivity": "com.scheler.superproxy.activity.MainActivity"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", super_proxy)
    wait = WebDriverWait(driver, 30)
    
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"))) #dldl
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    els1[0].click()

    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    els3[1].click()

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

    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@content-desc=\"Start\"]")))
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Start\"]")
    els2[0].click()

    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")
    els3[0].click()

def airProxy():
    #Start
    super_proxy = {
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.scheler.superproxy",
        "appium:appActivity": "com.scheler.superproxy.activity.MainActivity"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", super_proxy)
    wait = WebDriverWait(driver, 30)
    
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"))) #dldl
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    els1[0].click()

    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    els3[1].click()

    actions = ActionChains(driver)
    actions.send_keys("s4.airproxy.io")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1) 
    actions.send_keys(Keys.ENTER)
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()

    actions.send_keys("20209")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1) 
    actions.send_keys(Keys.TAB)
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()

    actions.send_keys("albydsq")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1) 
    actions.send_keys(Keys.ENTER)
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()

    actions.send_keys("5aLhh7kg4pELLx")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1) 
    actions.send_keys(Keys.ENTER)
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()

    els1 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
    els1[1].click()

    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@content-desc=\"Start\"]")))
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Start\"]")
    els2[0].click()

    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")
    els3[0].click()

def userLogin():
    print("Login in progress...")
# if driver.current_activity == ".EditText":
    # element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
    els1 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    els1[0].click()
    # if driver.current_activity == ".AutoCompleteTextView":
    # element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.AutoCompleteTextView")))
    # els1 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.AutoCompleteTextView")
    # els1[0].click()    
    #Email
    actions.send_keys("13152391975")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1) #Password
    actions.send_keys(Keys.DOWN)
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1)
    actions.send_keys("Jejelab")
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.perform()
    time.sleep(1)
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Log in\"]")
    els1[0].click()

def notNow():
    #Not now!
    print("Not now Starting")
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.View[@content-desc=\"Not now\"]')))
    els1 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=\"Not now\"]')
    els1[0].click()

def notif():
    #Notifications
    print("Notifications Starting")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]')))
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
    els1[0].click()

def location():
    #Location
    print("Location Starting")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc=\"Deny\"]')))
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Deny\"]")
    els2[0].click()

def menu():
    print("Menu")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.View[@content-desc=\"Menu, tab 6 of 6\"]')))
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Menu, tab 6 of 6\"]")
    els1[0].click()

def stories():
    print("Stories")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[15]/android.view.ViewGroup')))
    # touch = TouchAction(driver)
    touch.press(x=543, y=1821).move_to(x=560, y=436).release().perform()

def settings():
    print("Settings & privacy")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc=\"Settings & privacy, header. Section is collapsed. Double-tap to expand the section.\"]')))
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Settings & privacy, header. Section is collapsed. Double-tap to expand the section.\"]")
    els1[0].click()

def adsActivity():
    print("Recent Ads Activity")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]/android.view.ViewGroup')))
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]/android.view.ViewGroup")
    els2[0].click()

def saved():
    print("Saved")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]')))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]")
    els3[0].click()

def about():
    print("About this content")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="About this content"]')))
    touch.press(x=550, y=977).move_to(x=578, y=200).release().perform()

    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "finger"))
    # actions.w3c_actions.pointer_action.move_to_location(550, 977)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(578, 164)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform() #dodo

def ratings():
    print("About this...")
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[7]")
    els2[0].click()
    print("Exceeded1")
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[1]')))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[1]")
    els3[0].click()
    print("Exceeded2")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[2]")
    els3[0].click()
    print("Exceeded3")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[3]")
    els3[0].click()
    print("Exceeded4")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[4]")
    els3[0].click()
    print("Exceeded5")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[5]")
    els3[0].click()
    els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Next\"]")
    els1[0].click()

def feedback():
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText')))
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText")
    els2[0].click()
    comment = getComment()
    actions.send_keys(comment)
    actions.perform()
    # actions.w3c_actions.pointer_action.move_to_location(540, 2080)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()

# els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Skip\"]")
# els1[0].click()
#recentAd2 = /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[12]/android.view.ViewGroup
# randomIMEI()
# getComment()
# detectApp()
# rotateIP()
# detectApp()
# rotateIP()
# setProxy()
# superProxy()
# rotateIP()
# time.sleep(5)
# airProxy()
# rotateIP2()
# time.sleep(5)

# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

loginPage = "com.facebook.bloks.facebook.loggedout.FbExperimentalLoggedOutBloksActivity"
saveLogin = "com.facebook.account.switcher.nux.ActivateDeviceBasedLoginNuxActivity"
gps = "com.facebook.location.optin.DeviceLocationSettingsOptInActivity"
home = ".LoginActivity"
home2 = ".activity.FbMainTabActivity"
adActivity = "com.facebook.businessintegrity.mlex.adactivity.dashboard.AdActivityDashboardActivity"
GrantPermissionsActivity = "com.android.permissioncontroller.permission.ui.GrantPermissionsActivity"

while 1:
    if driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Log in"]') is not None:
        userLogin() #13152391975
        break
    else:
        current_activity = driver.current_activity
        print('Current activity:', current_activity)        
    time.sleep(1)

while 1:
    if driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=\"Not now\"]') is not None:
        notNow()
        break
    else:
        current_activity = driver.current_activity
        print('Current activity:', current_activity)   
    time.sleep(1)

quit()
notif()
location()
menu()
stories()
settings()
adsActivity()
saved()
about()
ratings()
feedback()

quit()

