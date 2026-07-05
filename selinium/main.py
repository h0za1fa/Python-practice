from selenium import webdriver

driver = webdriver.Chrome()
result = driver.get("https://www.amazon.com")

print(result) 

