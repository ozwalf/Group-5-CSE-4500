import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def findText(driver, keyword)->bool:
     if keyword.lower() in driver.page_source.lower():
        return True
     else:
        return False 
    
def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count 

'''
Rewards via keyword or image based on action
action : KEYWORD, IMAGE, LINK
driver : wed driver
reward_time : value to wait on site
req_list : list of either keyword or element tag
'''

def Actions(action, driver, reward_time, req_list)->float:
    total_reward_time=0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("found",keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)

    return total_reward_time 

# wrapper/helper function
def userAction(driver):
    reward_time = 10
    total_reward_time = 0
    keyword = ["major", "year"]
    tag_name = ['img']

    total_reward_time = Actions("KEYWORD", driver, reward_time, keyword)
    total_reward_time += Actions("IMAGE", driver, reward_time, tag_name)

    time.sleep(total_reward_time)
    print("Presence Time", total_reward_time)

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    
    userAction(driver)
    
    driver.quit()

if __name__ == "__main__":
    main()