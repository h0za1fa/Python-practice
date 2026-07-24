import selenium as sel
from selenium.webdriver.common.by import By
import time
import pprint as pp

start_time = time.perf_counter()

driver = sel.webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

driver.implicitly_wait(10)

powerups = [driver.find_elements(By.XPATH, f"/html/body/div[3]/div[5]/div/div[{i}]/b")[0].text for i in range(1,8)]
for i in range(len(powerups)):
    powerups_ = [power for power in powerups]
power_prices = {
    powerups[i].split(" - ")[0]: int(powerups[i].split(" - ")[1].replace(",", "")) for i in range(len(powerups))
}
print(power_prices)

while True:
    driver.find_element(By.ID, "cookie").click()
    if int(time.perf_counter() - start_time) % 10 == 0:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        for power, price in reversed(power_prices.items()):
            if money > price:
                # print(f"Buying {power} for {price} cookies.")
                try:
                    driver.find_element(By.XPATH, f"//b[contains(text(), '{power}')]").click()
                    break
                except:
                    time.sleep(0.1)
                
