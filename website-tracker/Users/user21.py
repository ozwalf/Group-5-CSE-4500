import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def userAction(driver):
    try:
        # find buttons
        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button, input[type='button'], input[type='submit'], input[type='reset'], a.btn, a.button")))
        print(f"Found {len(buttons)} buttons.")

        presence_time = (len(buttons) // 2) * 15  # add 15 seconds for every 2 buttons
        time.sleep(presence_time)
        print(f"Total presence time based on button count: {presence_time} seconds")

    except Exception as e:
        print(f"No buttons were found.")
