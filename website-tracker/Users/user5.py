import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = input("Enter the URL: ")

driver.get(url)
wait = WebDriverWait(driver, 30)  

def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False

def userAction(driver):
    reward_time = 10
    helper = ["students", "another"]
    print("in userAction")
    for item in helper:
        if findText(driver, item):
            time.sleep(reward_time)

            # if i did this wrong for whatever reason lmk
            # dm me licet torres in the class discord

def button_interactions(url):
    try:
        # find buttons
        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button, input[type='button'], input[type='submit'], input[type='reset'], a.btn, a.button")))
        print(f"Found {len(buttons)} buttons.")

        additional_time = (len(buttons) // 2) * 15  # add 15 seconds for every 2 buttons 
        presence_time = 10 + additional_time

        print(f"Total presence time based on button count: {presence_time} seconds")

    except Exception as e:
        print(f"No buttons were found.")
        presence_time = 10

    print(f"Presence time: {presence_time} seconds")        

button_interactions(url)
driver.quit()
