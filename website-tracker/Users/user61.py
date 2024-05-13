import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def measure_presence_time_with_scroll(driver, url, keyword):
    start_time = time.time()
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Check for keyword
    body_text = driver.find_element(By.TAG_NAME, 'body').text.lower()
    keyword_present = keyword.lower() in body_text
    print(f"Keyword '{keyword}' found: {keyword_present}")

    # Try scrolling in steps to ensure movement
    for _ in range(4):
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(0.5)

    scrolled_height = driver.execute_script("return window.scrollY;")
    print(f"Scrolled Height: {scrolled_height} pixels")

    # Calculate reward based on conditions
    if scrolled_height >= 400 and keyword_present:
        time.sleep(18)  # Reward time for conditions met
    else:
        time.sleep(5)  # Default time if conditions not met

    presence_time = time.time() - start_time
    print(f"Presence time on {url} with keyword '{keyword}' and scrolling: {presence_time:.2f} seconds")
    return presence_time

def userAction(driver):

    keyword = 'selenium'

    try:
        presence_with = measure_presence_time_with_scroll(driver, driver.current_url, keyword)

        print(f"Total presence time with preference: {presence_with:.2f} seconds")
        

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("done")

if __name__ == "__main__":
    main()
