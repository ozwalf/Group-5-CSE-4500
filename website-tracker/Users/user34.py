import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def countElem(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def userAction(driver):
    reward_time = 10
    total_reward_time  = 0
    tags = ["button"]
    for tag in tags:
        num_buttons = countElem(driver, tag)
        total_reward_time += reward_time*num_buttons
        time.sleep(reward_time)


    print("Presence Time:", total_reward_time, "seconds")

if __name__ == "__main__":
    main()
