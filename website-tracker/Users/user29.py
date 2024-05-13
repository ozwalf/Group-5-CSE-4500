import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False

def findKeyword(driver, keyword) -> bool:
    return keyword.lower() in driver.page_source.lower()

def countTagElem(driver, tag_name) -> int:
    print("Tag name:", tag_name)  # Print tag name for debugging
    count = 0
    count += len(driver.find_elements(By.TAG_NAME, tag_name))
    return count



def checkLink(driver, reward_time) -> float:
    links = driver.find_elements(By.TAG_NAME, "a")
    total_reward_time = 0

    for link in links:
        link.click()
        print("Link found and clicked")
        total_reward_time += reward_time
        time.sleep(reward_time)

    return total_reward_time

def userActions(action, driver, reward_time, req_list) -> float:
    total_reward_time = 0

    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("Keyword found:", keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("Keyword not found:", keyword)

    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        print("Number of images found:", num_images)
        total_reward_time = reward_time * num_images
        time.sleep(total_reward_time)

    elif action.upper() == "LINK":
        total_reward_time += checkLink(driver, reward_time)

    return total_reward_time

def userAction(driver):
    reward_time = 10
    total_reward_time = 0

    # Check for keywords
    total_reward_time += userActions("KEYWORD", driver, reward_time, [])

    # Check for images
    total_reward_time += userActions("IMAGE", driver, reward_time, "img")


    # Check for links
    total_reward_time += userActions("LINK", driver, reward_time, [])
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    # Run against a website with links
    main("http://localhost:3000/")
