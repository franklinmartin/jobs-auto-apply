import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

search_job_title = sys.argv[1]
search_job_title = search_job_title.split(" ")
search_location = sys.argv[2]
search_location = search_location.split(",")
search_location_city = search_location[0].strip()
search_location_state = search_location[1].strip()

def assign_url(search_job_title, search_location_city, search_location_state):
    sjt = search_job_title[0]
    for i in range(1, len(search_job_title)):
        if i == len(search_job_title):
            break
        sjt += "+" + search_job_title[i]
    url = "https://www.ziprecruiter.com/jobs-search?search="
    url += sjt + "&location=" + search_location_city + "%2C+" + search_location_state + "&page="
    return url

sjt = assign_url(search_job_title=search_job_title,
                 search_location_city=search_location_city,
                 search_location_state=search_location_state)
url = sjt
#url = "https://www.ziprecruiter.com/jobs-search?&search=software&location=Los+Angeles%2C+CA&page="
#url = "https://www.ziprecruiter.com/jobs-search?search=software&location=remote&page="
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

for j in range(1, 100000):
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