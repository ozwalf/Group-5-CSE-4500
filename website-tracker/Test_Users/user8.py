from selenium.webdriver.common.by import By
import time

total_reward_time = 0

def count_elem(id, driver):
    try:
        elements = len(driver.find_elements(By.ID, id))
        return elements
    except Exception as error:
        return 0
        print(error)

def find_link(href, driver):
    try:
        link = driver.find_element(By.CSS_SELECTOR, f'a[href="{href}"]')
        link.click()
        return True
    except:
        return False

def userAction(driver):
    global total_reward_time
    reward_time = 10
    wait_time = 0
    num_images = 0
    keywords = ["I'm", 'Annese', 'me', 'my']
    ids = ['HyruleWarriors', 'Persona']
    hrefs = ['https://github.com/Annese3908/Platform-Computing']

    page_source = driver.page_source
    keyword_counts = {keyword: 0 for keyword in keywords}
    for keyword in keywords:
        keyword_counts[keyword] = page_source.count(keyword)
        print(f"Found {keyword}: {keyword_counts[keyword]} times")
        wait_time = reward_time * keyword_counts[keyword]
        total_reward_time += wait_time
        time.sleep(wait_time)

    # image interaction
    for id in ids:
        num_images += count_elem(id, driver)
        wait_time = reward_time * num_images
        total_reward_time += wait_time
        time.sleep(wait_time)
    print(f"{num_images} images found.")

    # link interaction
    for href in hrefs:
        while find_link(href, driver):
            print(f"{href} found.")
            total_reward_time += reward_time
            time.sleep(reward_time)
    return total_reward_time

def main():
    driver = None
    try:
        # initialize driver
        from selenium import webdriver
        driver = webdriver.Firefox()
        # navigate to website
        driver.get('http://localhost:3000/')
        user_action(driver)
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.quit()
    print(f"Total reward time: {total_reward_time} milliseconds")
if __name__ == '__main__':
     main()

