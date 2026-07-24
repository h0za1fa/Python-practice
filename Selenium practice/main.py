import selenium as sel
from selenium.webdriver.common.by import By
from pprint import pprint

driver = sel.webdriver.Chrome()
driver.get("https://www.python.org/")

# element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]/time")

date = [driver.find_elements(By.XPATH, f"/html/body/div/div[{i}]/div/section/div[2]/div[2]/div/ul/li/time") for i in range(1, 6)]
dates = [date[2][i] for i in range(len(date[2]))]

name = [driver.find_elements(By.XPATH, f"/html/body/div/div[{i}]/div/section/div[2]/div[2]/div/ul/li/a") for i in range(1, 6)]
names = [name[2][i] for i in range(len(name[2]))]

driver.close()
driver.quit()

result = {i: {'Date': dates[i].text, 'Name': names[i].text} for i in range(len(dates))}
pprint(result)
