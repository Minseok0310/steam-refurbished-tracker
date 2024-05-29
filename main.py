# Import and Setup packages for Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import packages for email
import smtplib
import ssl

def sendEmail(model, status):
   port = 465
   smtp_server = "smtp.gmail.com"
   sender_email = "x@gmail.com"  # Email address removed for privacy
   receiver_email = "x@gmail.com"  # Email address removed for privacy
   password = "" # Password removed for privacy
   
   subject = f"Refurbished Steam Deck Stock Update"
   body = f"Refurbished Steamdeck {model} is now {status}, you can go purchase it at this link: https://store.steampowered.com/sale/steamdeckrefurbished/"
   
   message = f"""\
    Subject: {subject}

    {body}"""
   
   context = ssl.create_default_context()
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

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

stockDict = {"64GB": "", "256GB": "", "512GB": ""}

# Iterate through each element and see if they are in stock
if len(elements) == 3:
  models = list(stockDict.keys())
  for index, model in enumerate(models):
    # If they are out of stock, do nothing
    if "Out of stock" in elements[index].text:
        stockDict[model] = "Out of Stock"        

    else:
       # If they are in stock, send an email
       stockDict[model] = "In Stock"
       sendEmail(model, stockDict[model])

print(stockDict)

driver.quit()