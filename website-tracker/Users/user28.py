## tranlate this code from python to javascript
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def findKeyword(driver, keyword)->bool:
    ## print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()

## save elements
def countElem(driver, tag_name)->int:
    ## print(driver.page_source.lower())
    ## tag_name = "img"
    return len(driver.find_elements(By.TAG_NAME, tag_name))

# find back ground color
def findColor(driver, color)->bool:
    ## print(driver.page_source.lower())
    return color.lower() in driver.page_source.lower()

'''
Rewards via keyword, image, or link based on action
action : KEYWORD, IMAGE
driver : web driver
reward_time : value to wait on site
req_list : list of either keyword or element tag
'''
def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findKeyword(driver, keyword):
                print("found",keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print (keyword, " not found")

    elif action.upper() == "IMAGE":
        num_images = countElem(driver, req_list[0])
        total_reward_time = reward_time * num_images
        time.sleep(total_reward_time)

    elif action.upper() == "COLOR":
        for color in req_list:
            if findColor(driver, color):
                print("found",color)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print ("The %o was not found", color)

    return total_reward_time

def clickLink(driver, reward_time):
    total_reward_time = 0
    # find all anchor elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    # only clicks the first link
    for link in links:
        # link.click()
        time.sleep(reward_time)
        total_reward_time += reward_time
    return total_reward_time

def userAction(driver):
    reward_time = 10
    total_reward_time = userAction("KEYWORD", driver, reward_time, ["batman","game"])
    tag_name = ["img"]
    total_reward_time += userAction("IMAGE", driver, reward_time, tag_name)
    total_reward_time += userAction("COLOR", driver, reward_time, ['background-color: rgb(223, 207, 190);'])
    total_reward_time += clickLink(driver, reward_time),


    print("Presence Time:" , total_reward_time)

if __name__== "__main__":
    main()
