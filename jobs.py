from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
url = "https://www.ziprecruiter.com/jobs-search?&search=software+intern&location=Los+Angeles%2C+CA&page="
profile_path = "C:\\Users\Hal\\Documents\\GitHub\\jobs-auto-apply\\profile\\aauwq980.default-release"

options = webdriver.FirefoxOptions()
options.set_preference("profile", profile_path)

options.add_argument("-profile")
options.add_argument(profile_path)

driver = webdriver.Firefox(options=options)


#apply_buttons = driver.find_elements(By.CLASS_NAME, "text-button-secondary-default-text")
#apply_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-button-secondary-default-text")))

def click(element):
    #element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", element)

for j in range(1, 100):
    driver.get( url + str(j))
    apply_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-button-secondary-default-text")))
    for i in range(0, len(apply_buttons)):
        text = apply_buttons[i].text
        if "1-Click Apply" in text:
            #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-button-secondary-default-text")))
            apply_buttons[i].send_keys(Keys.CONTROL)
            click(apply_buttons[i])
            print(apply_buttons[i].id + " clicked.\n")
            #apply_buttons[i].click()
    print("page " + str(j) + " done.")