import time
import requests
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
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
        driver.launch_app()
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
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")

    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    if len(els3) > 0:
        els3[1].click()
    else:
        print("Error")


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

    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
    if len(els3) > 0:
        els3[1].click()
    else:
        print("Error")


    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@content-desc=\"Start\"]")))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Start\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


    element = wait.until(EC.visibility_of_element_loca5ted((By.XPATH, "//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")))
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Logging\nTab 2 of 3\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def userLogin():
    print("Login in progress...")
    time.sleep(1)
    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")
 
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
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Log in\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def notNow():
    #Not now!
    print("Not now Starting")
    time.sleep(1)
    els3 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=\"Not now\"]')
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def notif():
    #Notifications
    print("Notifications Starting")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def location():
    #Location
    print("Location Starting")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Deny\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def menu():
    print("Menu")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Menu, tab 6 of 6\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def feeds():
    print("Feeds")
    # touch = TouchAction(driver)
    touch.press(x=543, y=1821).move_to(x=560, y=436).release().perform()

def settings():
    print("Settings & privacy")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Settings & privacy, header. Section is collapsed. Double-tap to expand the section."]')
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def adsActivity():
    print("Recent Ads Activity")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]/android.view.ViewGroup")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def saved():
    print("Saved")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")


def about():
    print("About this content")
    actions.w3c_actions.pointer_action.move_to_location(550, 977)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(578, 164)
    actions.w3c_actions.pointer_action.release()
    actions.perform()    

def ratings():
    print("Ratings")
    els3 = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.view.ViewGroup")
    els3[16].click()

def exceed():
    print("Exceeded1")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[1]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")

    print("Exceeded2")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[2]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")
    print("Exceeded3")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[3]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")
    
    print("Exceeded4")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[4]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")

    print("Exceeded5")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[5]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")

    print("Next")
    els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Next\"]")
    if len(els3) > 0:
        els3[0].click()
    else:
        print("Error")

def feedback():
    print("Feedback")
    comment = getComment()
    actions.send_keys(comment)
    actions.perform()
    touch.press(x=540, y=2080).release().perform()

# randomIMEI()
# getComment()
# detectApp()
# rotateIP()
# detectApp()
# rotateIP()
# setProxy()
# rotateIP()
# time.sleep(5)
# airProxy()
# rotateIP2()
# time.sleep(5)

loginPage = "com.facebook.bloks.facebook.loggedout.FbExperimentalLoggedOutBloksActivity"
saveLogin = "com.facebook.account.switcher.nux.ActivateDeviceBasedLoginNuxActivity"
gps = "com.facebook.location.optin.DeviceLocationSettingsOptInActivity"
home = ".LoginActivity"
home2 = ".activity.FbMainTabActivity" #com.facebook.katana.LoginActivity
adActivity = "com.facebook.businessintegrity.mlex.adactivity.dashboard.AdActivityDashboardActivity"
GrantPermissionsActivity = "com.android.permissioncontroller.permission.ui.GrantPermissionsActivity"
status = 0
done = 0

while 1:
    
    element1 = driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Log in"]')
    element2 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=\"Not now\"]')
    element3 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]')
    element4 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc=\"Deny\"]')
    element5 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc=\"Menu, tab 6 of 6\"]')
    element6 = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.LinearLayout')
    element7 = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Settings & privacy, header. Section is collapsed. Double-tap to expand the section."]')
    element8 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]/android.view.ViewGroup')
    element9 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]')
    elementA = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup')

    elementB = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[4]')
    # elementB = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[8]')
    elementC = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText')
    elementD = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Photo/Video"]')
    elementE = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup')
    elementF = driver.find_elements(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@content-desc=\"Exceeded\"])[1]')
                              
    if 'element' in str(element1):
        userLogin() #13152391975

    elif 'element' in str(element2):
        notNow()

    elif 'element' in str(element3):
        notif()

    elif 'element' in str(element4):
        location()

    elif 'element' in str(element5) and 'element' in str(elementD):
        menu()
        time.sleep(2)
        feeds()

    elif 'element' in str(element7):
        settings()

    elif 'element' in str(element8):
        adsActivity()
        done == 0

    elif 'element' in str(element9) and done == 0:
        saved()
        time.sleep(2)
        about()
        ratings()

    elif 'element' in str(elementF):
        exceed()              
        time.sleep(2)
        feedback()  
        done = 1

    else: 
        print('Waiting')

    time.sleep(1)

    if driver.current_activity == loginPage or driver.current_activity == saveLogin or driver.current_activity == gps or driver.current_activity == home or driver.current_activity == adActivity or driver.current_activity == GrantPermissionsActivity or driver.current_activity == home2: 
        status = 0
    else:
        print('App is not on top')
        status += 1
        print(status)
        if status >= 5:
            driver.launch_app()
