# Kevin Kim 0074611110
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

def findKeyword(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False 

def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

def countElem(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findKeyword(driver, keyword):
                print("found", keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("not found!")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)

def userAction(driver):
    total_reward_time = 0
    reward_time = 10
    keyword = ["student", "CSUSB", "Major", "Computer Science"]
    tag = ["img"]
    print("in userAction")
    for item in keyword:
        findKeyword(driver, item)
        total_reward_time += reward_time
        time.sleep(reward_time)
    for item in tag:
        num_img = countElem(driver, item)
        total_reward_time += reward_time * num_img
        time.sleep(reward_time)
    

def clickLink(driver):
    count = 0
    links = driver.find_elements(By.TAG_NAME, "a")
    if links:
        for link in links:
            count += 1
            link.click()
    return count

def main():
    # Initialize browser
    driver = webdriver.Edge()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    reward_time = 10
    total_reward_time = 0

    keywords = ["student", "CSUSB", "Major", "Computer Science"]
    tags = ["img"]

    total_reward_time = userAction("KEYWORD", driver, reward_time, keywords)
    total_reward_time += userAction("IMAGE", driver, reward_time, tags)
    if clickLink(driver) > 0:
        clickLink(driver)
        total_reward_time += reward_time
        time.sleep(reward_time)    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    total_reward_time += reward_time
    driver.execute_script("window.scrollTo(0, 0)")
    total_reward_time += reward_time
    time.sleep(reward_time)
    driver.quit()

    print("Presence Time: ", total_reward_time)    

if __name__ == "__main__":
    main()