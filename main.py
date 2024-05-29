# Import and Setup Drivers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Navigate to Steam Store page
driver.maximize_window()
driver.get("https://store.steampowered.com/sale/steamdeckrefurbished/")

assert "steam" in driver.current_url

print("Application title is ", driver.title)
print("Application url is", driver.current_url)

# Check all three stock statuses (64, 256 & 512gb)
elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "I_6PnNNc2kMM38zamMgjd.CartBtn")))

if len(elements) == 3:
    models = ["64GB", "256GB", "512GB"]
    stockStatus = []

    for i in range(0,len(elements)):
        if "Out of stock" in elements[i].text:
            stockStatus.append("Out of Stock")
        else:
            stockStatus.append("In Stock")
    
    for i in range(0,len(elements)):
        print(models[i], " is ", stockStatus[i])

driver.quit()