
# //check for the word "pet" on the page
# //check for images on the page
# //check for links on the page
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def userAction(driver):
    # Track presence time
    start_time = time.time()
    presence_time = start_time
    end_time = 10
    check = False
    imageBool = False
    linkchecker = False
    while int(presence_time) <= int(end_time): # seconds
        #track time
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        print(f"End time: {end_time} seconds")
        time.sleep(10)

        try:
            divs = driver.find_elements(By.TAG_NAME, 'img')

            if imageBool == False:
                print(f"Img count: {len(divs)}")
                if len(divs) == 1:
                    end_time = end_time + end_time
                end_time = end_time * len(divs)
                time.sleep(end_time)
                imageBool = True
        except NoSuchElementException:
            print("imges not found")

        try:
            links = driver.find_elements(By.TAG_NAME, 'a')

            if linkchecker == False:
                print(f"Link count: {len(links)}")
                if len(links) == 1:
                    end_time = end_time + end_time
                end_time = end_time * len(links)
                time.sleep(end_time)
                linkchecker = True
        except NoSuchElementException:
            print("links not found")

        try:

            paragraphs = driver.find_elements(By.TAG_NAME, 'p')
            count = 0
            if (check == False):
                for e in paragraphs:
                    par = e.text
                    for i in par:
                        if (i == "."):
                            count = count + 1
                            end_time = end_time + 10
                            check = True
                            time.sleep(end_time)
                print(f"There is {count} periods's")


            # if imageBool == False:
            #     print(f"Div count: {len(number7)}")
            #     if len(number7) == 1:
            #         end_time = end_time + end_time
            #     end_time = end_time * len(number7)
            #     imageBool = True
        except NoSuchElementException:
            print("no number 7s not found")
