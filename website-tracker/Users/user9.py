import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
import csv

def findKeyword(driver, keyword):
    
    if keyword.lower() in driver.page_source.lower():
        return True
    
    else:
        return False

def countElements(driver, tag_name)->int:

    count = 0

    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))

    return count

def makeAction(action, driver, reward_time, req_list)->float:
    
    total_reward_time = 0
    
    if action.upper() == "KEYWORD":

        for keyword in req_list:

            if findKeyword(driver, keyword):
                print("found", keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time

            else:
                print("not found")
    
    elif action.upper() == "IMAGE":
        
        num_images = countElements(driver, req_list)
        total_reward_time = reward_time * num_images
        time.sleep(total_reward_time)

    elif action.upper() == "LINK":

        num_links = countElements(driver, req_list)
        total_reward_time = reward_time * num_links
        clickLink(driver)
        time.sleep(total_reward_time)

    elif action.upper() == "BUTTON":
        
        for button_name in req_list:
            num_buttons = countElements(driver, button_name)
            total_reward_time = reward_time * num_buttons
            clickButton(driver, button_name)
            time.sleep(total_reward_time)

    return total_reward_time

def clickLink(driver):
    
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        link.click()

def clickButton(driver, button_name):
    
    buttons = driver.find_elements(By.ID, button_name)

    for button in buttons:
        button.click()

def userAction(driver):
    
    reward_time = 10

    keywords = ["Magic", "bass", "Music"]
    tags = ["img"]
    links = ["a"]
    buttons = ["tab1", "tab2", "tab3", "tab4"]

    total_reward_time = makeAction("KEYWORD", driver, reward_time, keywords)
    total_reward_time += makeAction("BUTTON", driver, reward_time, buttons)
    total_reward_time += makeAction("IMAGE", driver, reward_time, tags)
    total_reward_time += makeAction("LINK", driver, reward_time, links)

    print("Presence Time: ", total_reward_time, "seconds")