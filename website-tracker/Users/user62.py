from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
import csv
import time

def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False
    
def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

def useAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("found",keyword)
                time.sleep(10)
                total_reward_time += reward_time
            else:
                print("not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(10)
    elif action.upper() == "PARAGRAPH":
        num_para = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_para
        time.sleep(10)
    
    return total_reward_time

def userAction(driver):
    reward_time = 10
    total_reward_time = 0
    total_reward_time = useAction("KEYWORD", driver, reward_time, ["sports", "games"])
    tag_name = ["img"]
    total_reward_time += useAction("IMAGE", driver, reward_time, tag_name)
    tag_name = ["p"]
    total_reward_time += useAction("PARAGRAPH", driver, reward_time, tag_name)
    total_reward_time += clickLink(driver, reward_time)

    print("Presence Time: ", total_reward_time)

    

def clickLink(driver, reward_time):
    count = -1
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        # link.click()
        count += 1
    reward_time += reward_time*count
    return reward_time
