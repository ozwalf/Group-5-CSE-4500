from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class UniqueUser:
    def __init__(self, preference):
        self.preference = preference
        self.presence_time = 0

    def extend_presence_time(self, driver, keyword, extend_time):
        start_time = time.time()
        page_source = driver.page_source
        if keyword.lower() in page_source.lower():
            print(f"Keyword '{keyword}' found. Extending presence time by {extend_time} seconds.")
            time.sleep(extend_time)
        else:
            print(f"Keyword '{keyword}' not found.")
        end_time = time.time()
        presence_time = end_time - start_time
        self.presence_time += presence_time
        print(f"Presence time: {self.presence_time:.2f} seconds")

    # Function to check for presence of links in HTML content
    def check_for_links_in_html(self, html_content):
        return '<a' in html_content.lower()

    # Function to extend presence time if links are present
    def extend_presence_time_for_links(self, driver, extend_time):
        html_content = driver.page_source
        if self.check_for_links_in_html(html_content):
            print(f"Links found. Extending presence time by {extend_time} seconds.")
            time.sleep(extend_time)
            self.presence_time += 15
        else:
            print("No links found.")

    def read_article(self, url_or_html):
        # Create a new driver instance
        driver = webdriver.Chrome()
        driver.maximize_window()

        try:
            self.presence_time = 0
            if url_or_html.startswith("http"):
                # Input is a URL, load the URL
                driver.get(url_or_html)
            else:
                # Input is HTML content, load it as a string
                driver.get("data:text/html;charset=utf-8," + url_or_html)

            # Simulate reading the article for 10 seconds
            time.sleep(10)
            self.presence_time += 10

            # Extend presence time if links are present
            extend_time_for_links = 15
            self.extend_presence_time_for_links(driver, extend_time_for_links)

            # Simulate searching for the "technology" keyword
            extend_time_for_keywords = 5
            self.extend_presence_time(driver, user_preference, extend_time_for_keywords)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            # Quit the driver after usage
            driver.quit()
            print(f"Presence time: {self.presence_time} seconds")


def userAction(driver):
    # Define user's preference
    user_preference = "technology"

    # Initialize unique user with preference
    user = UniqueUser(user_preference)

    # Test with a website that has elements related to the user's preference
    print(f"Opening Wired:")
    user.read_article(driver.current_url)

    # Read the content of the local HTML file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_directory, "without_images.html"), "r", encoding="utf-8") as file:
        html_content = file.read()

    # Test with the HTML content
    print(f"Opening basic html page: ")
    user.read_article(html_content)
