from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

ADDR_URL = 'https://www.linkedin.com/'
GMAIL = 'rafet.uregen7@gmail.com'
PASSWORD = "secret"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url=ADDR_URL)
time.sleep(2)

email_input = driver.find_element(By.ID, value="session_key")
email_input.send_keys(GMAIL)

password_input = driver.find_element(By.ID, value="session_password")
password_input.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
sign_in_button.click()
time.sleep(2)
JOB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3830970915&f_AL=true&f_WT=2&geoId=102257491&keywords=data%20scientist&location=B%C3%BCy%C3%BCk%20Londra%2C%20%C4%B0ngiltere%2C%20Birle%C5%9Fik%20Krall%C4%B1k&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R"

driver.get(url=JOB_URL)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


for listing in all_listings:
    listing.click()
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_button.click()






