from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time
from sys import argv
from math import ceil

DEBUG: bool = False

def userAction(driver: WebDriver) -> None:
    start_time: float = time.time()
    presence_time: float = 0

    page_content: str = driver.page_source
    images: list[WebElement] = driver.find_elements(By.TAG_NAME, 'img')
    links: list[WebElement] = driver.find_elements(By.TAG_NAME, 'a')
    iframe: list[WebElement] = driver.find_elements(By.TAG_NAME, 'iframe')

    preference: str = "keyword"
    keyword: str = 'Assignment'

    print(f"User Preference: {preference}")

    sleep_time: float = 5 
    if images:
        print(f"User sees {len(images)} image(s)")
        if preference == "image": 
            sleep_time = sleep_time * 2
        sleep_time = len(images) * sleep_time
        print(f"Browsing for {sleep_time}s")
        if not DEBUG:
            time.sleep(sleep_time)
        sleep_time = 5
    if links:
        print(f"User sees {len(links)} link(s)")
        if preference == "links": 
            sleep_time = sleep_time * 2
        sleep_time = ceil(len(links) / 3 * sleep_time) # links can be posted like nothing
        print(f"Browsing for {sleep_time}s")
        if not DEBUG:
            time.sleep(sleep_time)
        sleep_time = 5
    if keyword.lower() in page_content.lower():
        print(f"Keyword found!")
        if preference == "keyword": 
            sleep_time = sleep_time * 20 # 100s because keyword would make content interesting
            print(f"Browsing for {sleep_time}s")
        if not DEBUG:
            time.sleep(sleep_time)
        sleep_time = 5
    if iframe:
        print(f"User spotted {len(links)} iframe(s)")
        if preference == "iframe": 
            sleep_time = (sleep_time * 20 )
            print(f"Browsing for {sleep_time}s")
        sleep_time = (len(iframe) * sleep_time) % 200 # user hits max iframe stare at 200s
        if not DEBUG:
            time.sleep(sleep_time)
        sleep_time = 5
    
    current_time: float = round(time.time(), 2)
    presence_time = abs(round(current_time - start_time, 2))
    print(f"Presence time on: {presence_time}s")




def main() -> None:
    driver = Edge()
    URL: str = 'https://google.com'
    driver.get(URL)

    userAction(driver)
    driver.quit()



if __name__ == '__main__':
    main()