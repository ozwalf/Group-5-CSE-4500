from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# Function to simulate unique user behavior
def simulate_unique_user_behavior(driver):
    try:
        # Search for specific keywords
        keywords = ["technology", "artificial intelligence", "machine learning"]
        keyword_found = False
        for keyword in keywords:
            if keyword.lower() in driver.page_source.lower():
                keyword_found = True
                break

        if keyword_found:
            # If keywords found, simulate scrolling through images and clicking on links
            scroll_images(driver)
            click_links(driver)

        # Measure total time spent on the website
        total_time_spent = random.randint(60, 90)  # Simulate 60-90 seconds of engagement
        return total_time_spent

    except Exception as e:
        print("Error occurred during user behavior simulation:", e)
        return 0

# Function to simulate scrolling through images
def scroll_images(driver):
    # Simulate scrolling action by scrolling down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Simulate time spent scrolling

# Function to simulate clicking on links
def click_links(driver):
    # Find all anchor elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    if links:
        # Filter out non-interactable links
        clickable_links = [link for link in links if EC.element_to_be_clickable((By.TAG_NAME, "a")).__call__(link)]
        if clickable_links:
            # Click on a random clickable link
            random_link = random.choice(clickable_links)
            try:
                random_link.click()
                time.sleep(3)  # Simulate time spent loading the new page
            except Exception as e:
                print("Error occurred while clicking on a link:", e)
        else:
            print("No clickable links found.")
    else:
        print("No links found.")

# Main function
def main(url):
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome()  # You can change this to your preferred WebDriver

        # Navigate to the URL
        driver.get(url)

        # Wait for the content to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Simulate unique user behavior
        total_time_spent = simulate_unique_user_behavior(driver)

        # Output total time spent on the website
        print("Total time spent on the website:", total_time_spent, "seconds")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver
        if driver:
            driver.quit()

def userAction(driver):
    time.sleep(simulate_unique_user_behavior(driver))
