import time
# import keyboard
import duration
from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import AppiumBy

fb_caps  = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "emulator-5554",
    "appium:appPackage": "com.android.chrome",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.google.android.apps.chrome.Main"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", fb_caps)
actions = ActionChains(driver)
touch = TouchAction(driver)
print("Launching Chrome")

def loginFB():
    login = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.widget.Button")
    if len(login) > 0:
        login[0].click()
    else:
        print("Error")

searchTitle = 'Erboristeria gaeta'
mmenu = 0
login = 0

while 1:

    menu = driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="More options"]')
    done = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.app.Dialog/android.view.View[3]/android.view.View')
    storeLink = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View')
    cookies = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.widget.Button[2]')
    checkBox = driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Turn off Request desktop site"]')
    checkBox2 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[10]/android.widget.ImageView')
    NotNow = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
    element1 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.Button[1]')
    element2 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText')
    element3 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
    notif = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.Button[1]')
    element5 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[6]/android.widget.Button')
    element6 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button')
    agree = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Button')
    noTnx = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]')

    if 'element' in str(element1):
        print("Google Start")
        if len(element1) > 0:
            element1[0].click()
            time.sleep(2)
        else:
            print("Loading...")

    elif 'element' in str(agree):
        print('agree')
        if len(agree) > 0:
            agree[0].click()
        else:
            print("Loading...")

    elif 'element' in str(noTnx):
        print('noTnx')
        if len(noTnx) > 0:
            noTnx[0].click()
        else:
            print("Loading...")

    elif 'element' in str(done):
        print('done')
        if len(done) > 0:
            done[0].click()
            time.sleep(2)        
        else:
            print("Loading...")

    elif 'element' in str(storeLink):
        print('storeLink')
        if len(storeLink) > 0:
            storeLink[0].click()
            time.sleep(2)
            actions.w3c_actions.pointer_action.move_to_location(490, 2063)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()            
        else:
            print("Loading...")

    elif 'element' in str(menu) and mmenu == 0:
        print('Menu')
        if len(menu) > 0:
            menu[0].click()
            mmenu = 1
        else:
            print("Loading...")

    elif 'element' in str(checkBox2):
        print('checkBox2')
        if len(checkBox2) > 0:
            time.sleep(2)
            actions.w3c_actions.pointer_action.move_to_location(974, 1227)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.5)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(2)
            driver.get("https://www.facebook.com")            
        else:
            print("Loading...")

    elif 'element' in str(cookies):
        print('Cookies')
        if len(cookies) > 0:
            cookies[0].click()
        else:
            print("Loading...")

    elif 'element' in str(NotNow):
        print('NotNow')
        if len(NotNow) > 0:
            NotNow[0].click()
        else:
            print("Loading...")

    elif 'element' in str(element2) and login == 0:
        print('Login')
        if len(element2) > 0:
            element2[0].send_keys("13152391975")
            password = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText')
            password[0].send_keys("Jejelab")
            loginFB()
            login = 1
        else:
            print("Loading...")   

    elif 'element' in str(element3):
        print('Not now')
        if len(element3) > 0:
            element3[0].click()
        else:
            print("Loading...") 

    elif 'element' in str(notif):
        print('Notification')
        if len(notif) > 0:
            notif[0].click()
        else:
            print("Loading...") 

    # elif 'element' in str(element5):
    #     print('Home')
    #     if len(element5) > 0:
    #         driver.get("https://fb.me/1ZPUT58hdRiZBW4")
    #         # break
    #     else:
    #         print("Loading...") 

    # elif 'element' in str(element6):
    #     print('Ads')
    #     while 1:
    #         pageTitle = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="' & searchTitle & '"]/android.widget.TextView')
    #         dot3 = driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.view.View')

    #         if searchTitle in pageTitle:
    #             dot3[0].click()
    #             break
    #         else:
    #             print("Scrollin...")
    #             touch.press(x=563, y=1583).move_to(x=563, y=553).release().perform()

        time.sleep(1)

    else:
        print('Waiting...')
        # break
    time.sleep(1)

