import time
from selenium import webdriver


def findKeyword(driver, keyword)->bool:
    print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()
def userAction(driver):

    reward_time = 10
    total_reward_time = 0
    keywords = ["student", "test"]
    for key in keywords:
        if findKeyword(driver, key):
            total_reward_time += reward_time
            time.sleep(reward_time)

    print("Presence Time:", total_reward_time)

if __name__=="__main__":
    main()
