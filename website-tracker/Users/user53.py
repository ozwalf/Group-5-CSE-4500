import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False

def clickLink(driver,reward_time):
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        link.click()
        time.sleep(reward_time)
        total_reward_time += reward_time

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
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)
    elif action.upper() == "HEADERS":
        num_headers = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_headers
        time.sleep(total_reward_time)

    elif action.upper() == "LINK":
        num_links = countTagElem(driver, "a")
        total_reward_time = reward_time*num_links
        time.sleep(total_reward_time)

    return total_reward_time

def userAction(driver):
    reward_time = 10
    total_reward_time = userActions("KEYWORD", driver, reward_time, ["programming", "major", "CSUSB"])
    total_reward_time += userActions("LINK", driver, reward_time, "a")
    tag_name = ["h1", "h2", "h3"]
    total_reward_time += userActions("HEADERS", driver, reward_time, tag_name)
    print("Presence Time", total_reward_time)


if __name__ == "__main__":
    main()
