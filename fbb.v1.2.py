
# proxy.http_proxy = "http://albydsq:5aLhh7kg4pELLx@s4.airproxy.io:20209"
import time
import requests
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

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

options = {
    'proxy': {
        'http': 'http://albydsq:5aLhh7kg4pELLx@s4.airproxy.io:20209',
        'https': 'http://albydsq:5aLhh7kg4pELLx@s4.airproxy.io:20209',
        'no_proxy': 'localhost,127.0.0.1' # excludes
    }
}

# rotateIP2()
# time.sleep(5)
# driver = webdriver.Chrome(seleniumwire_options=options)
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="email"]')))
email_input.send_keys("13152391975")
password_input = driver.find_element(By.CSS_SELECTOR, '[id="pass"]')
password_input.send_keys('Jejelab')
login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
login_button.click()
driver.implicitly_wait(10)
print("Welcome")
time.sleep(5)
driver.get("https://www.facebook.com")

close = 0
hide_it = 0 
action = 0
ignore_it = 0

while True:
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    time.sleep(1)

    if hide_it == 0 and action == 0:
        hides = driver.find_elements(By.XPATH, '//*[@aria-label]')
        aria_labels = []
        for hide in hides:
            aria_label = hide.get_attribute("aria-label")
            aria_labels.append(aria_label)
            try:
                # if 'Close' in str(aria_labels) and close == 0:
                #     print('Close')
                #     # hide.click()
                #     driver.execute_script("arguments[0].click();", hide)
                #     time.sleep(5)
                #     close = 1

                if 'hide post' in str(aria_labels) and hide_it == 0:
                    print('hide post')
                    # hide.click()
                    driver.execute_script("arguments[0].click();", hide)
                    hide_it = 1
                    time.sleep(5)
                    break
                else:
                    print("Searching...")

            except WebDriverException as e:
                print("An exception occurred: {}".format(e))
            # time.sleep(1)

    if action == 0 and hide_it == 1:
        posts = driver.find_elements(By.XPATH, '//*[@aria-label]')
        aria_labels = []
        for post in posts:
            aria_label = post.get_attribute("aria-label")
            aria_labels.append(aria_label)

            try:
                if 'Actions for this post' in str(aria_labels) and action == 0:
                    print('Actions for this post')
                    # post[0].click()
                    driver.execute_script("arguments[0].click();", post)
                    action = 1
                    time.sleep(5)
                    break

            except WebDriverException as e:
                print("An exception occurred: {}".format(e))

    if action == 1 and hide_it == 1 and ignore_it == 0:
        # ignores = driver.find_elements(By.XPATH, '//a[contains(@class, "Save link")]')
        # aria_labels = []

        try:
            popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@aria-label, "Actions for this post")]')))
            print(popup)
            # save_link = WebDriverWait(popup, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "Save link")]')))
            save_link = driver.find_elements(By.XPATH, '//div[contains(@dir, "auto")]')
            print(save_link)
            # save_link[0].click()
            popup.execute_script("arguments[0].click();", save_link)
        except WebDriverException as e:
            print("An exception occurred: {}".format(e))

        # for ignore in ignores:
        #     aria_label = post.get_attribute("#text")
        #     aria_labels.append(aria_label)

        #     try:
        #         if 'Save link' in str(aria_labels) and ignore_it == 0:
        #             print('Save link')
        #             # post[0].click()
        #             driver.execute_script("arguments[0].click();", ignore)
        #             ignore_it = 1
        #             time.sleep(200)
        #             break
        #         else:
        #             print("Searching Save link...")

        #     except WebDriverException as e:
        #         print("An exception occurred: {}".format(e))
            
        #     time.sleep(1)
        #     print(aria_label)

    # Print the list of aria-label values
    # print(aria_labels)
    
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    if action == 1 and hide_it == 1 and ignore_it == 1:
        driver.quit()

# time.sleep(200000)


# ['Back to previous page', 'Facebook', 'Exit typeahead', 'Search Facebook', 'Facebook', 'Home', 'Friends', 'Groups', 
#  'More', 'Account Controls and Settings', 'Your profile', 'Notifications', 'Notifications', 'Messenger', 'Messenger', 
#  'Menu', 'Create', 'Facebook', 'Stories', 'Previous items', 'stories tray', 'Create story', 'Next items', 'Create a post', 
#  "Phoemela Cristjana Quiambao's Timeline", 'Sadtitle', '4d', 'Actions for this post', 'hide post', 'See who reacted to this', 
#  'Love: 14K people', 'Like: 7.9K people', 'Care: 2.7K people', 'Like', 'React', 'Leave a comment', 
#  'Send this to friends or post it on your timeline.', 'Erboristeria gaeta', 'Sponsored (demo)', 
#  'Actions for this post', 'Learn more', 'See who reacted to this', 'Like: 1.2K people', 'Like', 
#  'React', 'Leave a comment', 'Send this to friends or post it on your timeline.', 'Mommy Anne’s Lechon House', 
#  'Actions for this post', 'hide post', 'See who reacted to this', 'Love: 2.1K people', 'Like: 1.8K people', 
#  'Wow: 265 people', 'Like', 'React', 'Leave a comment', 'Send this to friends or post it on your timeline.', 
#  'Jawo Motovlog', 'February 5', 'Actions for this post', 'hide post', 'Play video', 'Play', 'Change Position', 
#  'Change Position', 'Settings', 'Open in Watch', 'Continue watching while you browse Facebook.', 'Change volume', 
#  'Unmute', 'See who reacted to this', 'Like: 54K people', 'Love: 23K people', 'Like', 'React', 'Leave a comment', 
#  'Send this to friends or post it on your timeline.', 'බඩජාරියා', 'Actions for this post', 'hide post', 
#  'See who reacted to this', 'Like: 9.2K people', 'Love: 6K people', 'Like', 'React', 'Leave a comment', 
#  'Send this to friends or post it on your timeline.', 'Ref Egay Mix TV', 'February 8', 'Actions for this post', 
#  'hide post', 'Translation Preferences', 'Play video', 'Play', 'Change Position', 'Change Position', 'Settings', 
#  'Open in Watch', 'Continue watching while you browse Facebook.', 'Change volume', 'Unmute', 'See who reacted to this', 
#  'Like: 25K people', 'Love: 5.3K people', 'Like', 'React', 'Leave a comment', 'Send this to friends or post it on your timeline.', 
#  'Loading...', 'Loading...', 'New call', 'Search by name or group', 'Options', 'New message']