import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

def userActions(action, driver, reward_time, req_list)->float:
    total_reward_time=0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("found",keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
    elif action.upper() == "PARAGRAPHS":
        num_paragraphs = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_paragraphs
        time.sleep(total_reward_time)
    elif action.upper() == "DIVIDERS":
        num_paragraphs = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_paragraphs
        time.sleep(total_reward_time)
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)

    return total_reward_time

def userAction(driver):
    reward_time = 10
    total_reward_time = userActions("KEYWORD", driver, reward_time, ["CSUSB"])
    tag_name = ["p"]
    total_reward_time += userActions("PARAGRAPHS", driver, reward_time, tag_name)
    tag_name = ["div"]
    total_reward_time += userActions("DIVIDERS", driver, reward_time, tag_name)
    tag_name = ["img"]
    total_reward_time += userActions("IMAGE", driver, reward_time, tag_name)
    print("Presence Time", total_reward_time)

if __name__ == "__main__":
    main()
