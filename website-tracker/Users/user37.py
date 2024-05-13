from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
def userActions(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time * num_images
        time.sleep(total_reward_time)
    elif action.upper() == "LINK":
        num_link = countTagElem(driver, "a")
        total_reward_time = reward_time * num_link
        time.sleep(total_reward_time)
        clickLink(driver)

    return total_reward_time

# function to click link
def clickLink(driver):
    # find link
    link = driver.find_element(By.TAG_NAME, "a")
    # only clicks first link
    link.click()

def userAction(driver):
    reward_time = 10
    tag_name = "img"
    # update total reward time when user detects an image(s)
    total_reward_time = userActions("IMAGE", driver, reward_time, [tag_name])
    # update total reward time when user detects a link(s)
    total_reward_time += userActions("LINK", driver, reward_time, [])

    time.sleep(total_reward_time)
    # add string "seconds" so programmer knows presence time is measured in seconds
    print("Presence Time", total_reward_time,"seconds")

if __name__ == "__main__":
    main()
