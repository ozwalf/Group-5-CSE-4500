import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def count_elem(driver, tag_name):
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def userAction(driver):

    
    # Define the tag names to search for
    tags = ["button"]
    
    total_reward_time = 0
    
    # Reward time for each tag
    reward_time = 30
    
    # Iterate through each tag and count its occurrences
    for tag in tags:
        num_tags = count_elem(driver, tag)
        total_reward_time += reward_time * num_tags
    
    # Simulate user presence for the total reward time
    time.sleep(total_reward_time)

    
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()
