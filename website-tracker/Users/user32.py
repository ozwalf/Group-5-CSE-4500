import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def userAction(driver):

    metrics = []
    num_clicks = 0
    # Track presence time
    start_time = time.time()
    presence_time = start_time
    end_time = 10
    clicked = False
    wordFound = False
    imageBool = False
    while int(presence_time) < end_time: # seconds
        #track time
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        print(f"End time: {end_time} seconds")
        time.sleep(10)
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")

        if current_scroll > 500:
            end_time = end_time + 10

        try:
            images = driver.find_elements(By.TAG_NAME, 'img')

            if imageBool == False:
                print(f"Image count: {len(images)}")
                if len(images) == 1:
                    end_time = end_time + end_time
                end_time = end_time * len(images)
                time.sleep(end_time)
                imageBool = True
        except NoSuchElementException:
            print("Images not found")

        try:
            element = driver.find_element(By.XPATH, "//h2[contains(text(), 'Nature')]")

            if wordFound == False:
                if element.text == 'Nature':
                    end_time = end_time + 10
                    wordFound = True
                    time.sleep(end_time)
                    print("Nature was found")
        except NoSuchElementException:
            print("Nature not found")



        try:
            link = driver.find_element(By.TAG_NAME, 'a')

            if clicked == False:
                link.click()
                if link.is_displayed():
                    print(f"LINK CLICKED AND TIME EXTENDED")
                    end_time = end_time + 10
                    clicked = True
                    time.sleep(end_time) 
        except NoSuchElementException:
            print("Link not found")
