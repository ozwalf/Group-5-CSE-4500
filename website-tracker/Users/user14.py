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
    total_reward_time = 0
    reward_time = 10
    helper = ["students", "another"]
    print("in userAction")
    for actions in helper:
        actions = [
            ("IMAGE", ["img"]),
            ("BUTTON", ["button"])
        ]
        for action_type, req_list in actions:
            if action_type.upper() == "IMAGE":
                num_images = countTagElem(driver, req_list)
                total_reward_time += reward_time * num_images
                time.sleep(total_reward_time)
            elif action_type.upper() == "BUTTON":
                num_button = countTagElem(driver, req_list)
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
