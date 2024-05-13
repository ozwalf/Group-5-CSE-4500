import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False

def countTagElem(driver, tag_name):
    count = 0
    for tag in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tag))
    return count

def userAction(driver):
    reward_time = 10
    total_reward_time = 0

    # Prompt user for action type
    action_type = "BUTTON"

    if action_type.upper() == "KEYWORD":
        for keyword in ["steven", "game", "anime", "movie", "sports"]:
            if findText(driver, keyword):
                print("found", keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("not found")
    elif action_type.upper() == "IMAGE":
        num_images = countTagElem(driver, ["img"])
        total_reward_time += reward_time * num_images
        time.sleep(total_reward_time)
    elif action_type.upper() == "LINK":
        num_link = countTagElem(driver, ["a"])
        total_reward_time += reward_time * num_link
        time.sleep(total_reward_time)
    elif action_type.upper() == "BUTTON":
        num_button = countTagElem(driver, ["button"])
        total_reward_time += reward_time * num_button
        time.sleep(total_reward_time)

    return total_reward_time

def main():
    # Initialize browser
    driver = webdriver.Chrome()
    # Navigate to your website
    driver.get("http://localhost:3000/")

    total_reward_time = userAction(driver)
    driver.quit()

    print("Presence Time", total_reward_time)

if __name__ == "__main__":
    main()
