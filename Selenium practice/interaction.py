import selenium as sel
from selenium.webdriver.common.by import By

driver = sel.webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
val = driver.find_element(By.ID, 'mwDw')
print(val.text)



driver.close()
driver.quit()