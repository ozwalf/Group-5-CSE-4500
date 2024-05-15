import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def find_keywords(driver, keywords):
    page_content = driver.page_source.lower()
    for keyword in keywords:
        if keyword.lower() in page_content:
            return True
    return False

def click_link(driver, link_text):
    try:
        link_element = driver.find_element(By.LINK_TEXT, link_text)
        link_element.click()
        return True
    except NoSuchElementException:
        return False

def userAction(driver):

    # Define user preferences
    keywords = ["panama", "soccer", "trilingual"]
    preferred_links = ["GitHub"]
    preferred_image = "Beautiful Landscape"

    # Reward time for engaging elements
    reward_time = 10
    total_reward_time = 0

    # Check for keywords
    if find_keywords(driver, keywords):
        print("Keywords found. Extending presence time by", reward_time, "seconds.")
        total_reward_time += reward_time

    # Click preferred links
    for link_text in preferred_links:
        if click_link(driver, link_text):
            print("Clicked on link:", link_text)
            total_reward_time += reward_time

    # Look for preferred image
    try:
        driver.find_element(By.XPATH, f"//img[@alt='{preferred_image}']")
        print("Preferred image found. Extending presence time by", reward_time, "seconds.")
        total_reward_time += reward_time
    except NoSuchElementException:
        pass

    # Simulate staying on the site for the reward time
    time.sleep(total_reward_time)

    

    print("Total Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()
