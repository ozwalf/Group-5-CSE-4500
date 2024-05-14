import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Returns true or false on whether a keyword exists
'''
def findKeyword(driver, keyword)->bool:
    if keyword.lower() in driver.page_source.lower():
        # print(driver.page_source)
        return True
    else:
        return False

'''
Returns number of images given tag_name
'''
def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

'''
Rewards via keyword or image based on action
action : KEYWORD, IMAGE, LINK
driver : web driver
reward_time : value to wait on site
req_list : list of either keyword or element tag
'''
def useActions(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
            for keyword in req_list:
                if findKeyword(driver, keyword):
                    print("found", keyword)
                    time.sleep(reward_time)
                    total_reward_time += reward_time
                else:
                    print("not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)

    return total_reward_time


def userAction(driver):
    reward_time = 2
    total_reward_time = useActions("KEYWORD", driver, reward_time, ["Guatemala", "Spanish", "Japanese"])
    tag_name = ["img"]
    total_reward_time += useActions("IMAGE", driver, reward_time, tag_name)
    print("Present Time:", total_reward_time, "seconds")

if __name__ == "__main__":
    main()
