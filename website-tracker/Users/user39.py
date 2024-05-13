import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

def userAction(driver):
    start_time = time.time()

    time.sleep(random.uniform(5, 10))  # Random sleep to simulate reading time

    # Check for images on the page
    images = driver.find_elements(By.TAG_NAME, "img")
    if not images:  # If there are no images, reduce the base presence time
        print(f"No images found. Reducing presence time.")
        base_presence_time = 5  # Reduced base presence time
    else:
        base_presence_time = 10  # Default base presence time if images are found

    time.sleep(base_presence_time)  # Sleep for base presence time
