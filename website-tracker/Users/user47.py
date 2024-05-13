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
    for tag in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tag))
    return count

def userActions(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "LINK":
        num_link = countTagElem(driver, "a")
        total_reward_time = reward_time*num_link
        time.sleep(total_reward_time)
    elif action.upper() == "BUTTON":
        num_button = countTagElem(driver, ["button"])
        total_reward_time = reward_time*num_button
        time.sleep(total_reward_time)

    return total_reward_time

def userAction(driver):
    reward_time = 10;
    total_reward_time = userActions("LINK", driver, reward_time, [])
    total_reward_time += userActions("BUTTON", driver, reward_time, [])

    print("Presence Time",total_reward_time)

if __name__ == "__main__":
    main()
