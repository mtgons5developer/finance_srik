from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# initialize Safari driver
driver = webdriver.Safari()
driver.set_window_size(1920, 1200)

# wait for the Expand Detail View button to appear and click it
expand_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'more-data sal-mds-link')]"))
)
expand_button.click()

# # wait for the Export Data button to appear and click it
# expand_button = WebDriverWait(driver, 3).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'segment-band__tabs')]"))
# )
# expand_button.click()

# dcec09d8-2675-c888-95f3-12f28e52590c
# # Find the span element by its class name
# span_element = driver.find_element_by_class_name("mds-button__sal mds-button--secondary__sal mds-button--small__sal")
# # span_element = driver.find_element_by_css_selector(".mds-button__sal mds-button--secondary__sal mds-button--small__sal")
# # Click the span element
# span_element.click()

# element = driver.find_element_by_css_selector("button.mds-button__sal.mds-button--secondary__sal.mds-button--small__sal span")
# element.click()


# # select CSV format for the exported data
# csv_option = driver.find_element("xpath", "//a[contains(@class, 'csv')]")
# csv_option.click()

# # choose where to save the exported file and click save
# save_button = driver.find_element("xpath", "//button[contains(@class, 'save')]")
# save_button.click()

# close the Safari window
driver.quit()
