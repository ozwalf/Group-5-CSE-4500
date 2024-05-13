#Unique User with helper function...

from selenium import webdriver
from selenium.webdriver.common.by import By

import re

#allows selenium to use a chain of actions (will be used to open links in another tab)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#used to keep track of presence time of the unique_user
import time


#userAction needs to be explicit for others to run.
#NOTE: Removed a lot of other functions from this file since not needed.
def userAction(driver):
    reward_time = 10
    keywords = ["food", "foods", "game", "games", "book", "books", "class", "classes" ]
    imgTag = "img"
    linkTag = "a"

    total_reward_time = userActions("KEYWORD", driver, reward_time, keywords)
    total_reward_time += userActions("IMAGE", driver, reward_time, imgTag)
    total_reward_time += userActions("LINK", driver, reward_time, linkTag)

    print("I will sleep for", {total_reward_time})

    time.sleep(total_reward_time)

    





#################################################
# Rewards via keyword or image or link based on action
# action: KEYOWRD, IMAGE, LINK
# driver: web driver
# req_list: list of either keyword or element tag
##################################################

def userActions(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        if(req_list):
            for keyword in req_list:
                print("looking for: ", keyword)
                num_words = findKeyword(driver, keyword)
                print("appeared", num_words, "times")
                reward_time_X = reward_time * num_words
                total_reward_time += reward_time_X
    elif action.upper() == "IMAGE":
        item = countElem(driver, req_list)
        num_images = item[0]
        reward_time_X = reward_time*num_images
        total_reward_time += reward_time_X
    elif action.upper() == "LINK":
        item = countElem(driver, req_list)
        num_links = item[0]
        
        clickLinks(driver, item[1])

        reward_time_X = reward_time*num_links
        total_reward_time += reward_time_X

    
    return total_reward_time


def findKeyword(driver, keyword):
    # Find all paragraph elements on the page
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')

    # Get the text from each paragraph
    visible_text = [p.text.lower() for p in paragraphs]

    # Create a regular expression pattern to match whole words
    pattern = r'\b{}\b'.format(keyword.lower())

    # Count the keyword in visible text
    num_occurrences = sum(len(re.findall(pattern, text)) for text in visible_text)

    return num_occurrences


#Used for both links and images...
def countElem(driver, tag_name):
    # Get all elements for the specified tag_name
    elements = driver.find_elements(By.TAG_NAME, tag_name)
    
    # Total number of elements
    total_length = len(elements)

    if total_length == 0:
        print("found nothing with tag", {tag_name})
    else:
        print("found tags, ", {tag_name}, {total_length}, " time(s)")

    return total_length, elements


#only for links...
def clickLinks(driver, links):
    #find link or links and click on them....
    for link in links:
        ActionChains(driver) \
            .key_down(Keys.SHIFT) \
            .click(link) \
            .key_up(Keys.SHIFT) \
            .perform()



def main():
    #initialize browser
    driver = webdriver.Chrome()

    #Navigate to your website
    driver.get("http://localhost:3000")

    userAction(driver)

if __name__ == "__main__":                          #this lets us test it stand-alone. when imported, this wont pose an issue.
    main()
