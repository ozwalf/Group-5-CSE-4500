
from selenium import webdriver
import time

'''
Returns true or false on whether a keyword exists
Capitalization should not matter (e.g will detect "Student" on a page as "student" and vice versa)
Will detect super word in page (e.g. will detect "students" on a page as "student" )
'''
def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        # print(driver.page_source)
        return True
    else:
        return False
'''
driver: driver
helper attributes and reward_time must be hardcoded
'''
def userAction(driver):
    reward_time = 10
    helper = ["students", "another"]
    print("in userAction")
    for item in helper:
        if findText(driver, item):
            time.sleep(reward_time)


def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    keywords = ["student","another"]
    print("IN KEYWORD USER")
    for keyword in keywords:
        if findText(driver, keyword):
            print("found",keyword)
            time.sleep(reward_time)
            total_reward_time += reward_time
        else:
            print("not found")
    driver.quit()

    print("Presence Time",total_reward_time)


if __name__ == "__main__":
    main()
