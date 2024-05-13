from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import re
def keywordCounter(driver, keyword)->int:
    return len(re.findall(f'(?=({keyword.lower()}))', driver.page_source.lower()))

def userAction(driver):

    rewardTime = 1
    keyword = "game"


    # Website with keyword
    totalRewardTime = keywordCounter(driver, keyword) * rewardTime
    time.sleep(totalRewardTime)
    print("Page 1: " + str(totalRewardTime) + " seconds")
