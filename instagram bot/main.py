import time
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config =dotenv.dotenv_values('instagram bot/constants.env')
username = config.get('USERNAME')
password = config.get('PASSWORD')

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/')

wait = WebDriverWait(driver, 10)

driver.find_element(By.NAME, 'email').send_keys(username)
driver.find_element(By.NAME, 'pass').send_keys(password)

driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span').click()

wait = WebDriverWait(driver, 5)

time.sleep(10)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//svg[@aria-label="Search"]')))
except:
    print("please provide human input")
    input()
    

driver.find_element(By.CSS_SELECTOR, "[aria-label='Search']").click()


input('Enter to quit')
driver.quit()