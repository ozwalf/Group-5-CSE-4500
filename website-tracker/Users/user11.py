import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv

def countElem(driver, tag_name)->int:
    
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def findKeyword(driver, keyword)->bool:
    
    return keyword.lower() in driver.page_source.lower()

def clickLink(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    clickCount = 0
    for link in links:
        
        link.click()
        clickCount += 1
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return clickCount

def useAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findKeyword(driver, keyword):
                print("Found: ", keyword)
                total_reward_time += reward_time
                time.sleep(reward_time)
            else:
                print("Not found: ", keyword)
    elif action.upper() == "IMAGES":
        for tag in req_list:
            num_images = countElem(driver, tag)
            total_reward_time += reward_time * num_images
            time.sleep(total_reward_time)
    elif action.upper() == "LINK":
        num_link = clickLink(driver)
        total_reward_time += reward_time * num_link
    return total_reward_time



def userAction(driver):
    reward_time = 10
    reward_per_word = 1
    reward_per_link = 3

    keywords = ["student", "music", "games"]
    tags = ["img"]

    total_reward_time = useAction("KEYWORD", driver, reward_time, keywords)
    total_reward_time += useAction("IMAGES", driver, reward_time, tags)
    total_reward_time += useAction("LINK", driver, reward_per_link, "")

    print("Presence Time:", total_reward_time, " seconds.")