import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class UniqueUser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.keyword_list = ["technology", "innovation", "gadgets"]
        self.image_tags = ["img", "picture"]
        self.elements_to_check = ["header", "footer", "nav"]

    def find_keyword(self, keyword):
        if keyword.lower() in self.driver.page_source.lower():
            return True
        else:
            return False

    def count_images(self, tag_names):
        count = 0
        for tag_name in tag_names:
            count += len(self.driver.find_elements(By.TAG_NAME, tag_name))
        return count

    def find_element(self, element):
        try:
            self.driver.find_element(By.TAG_NAME, element)
            return True
        except:
            return False

    def user_action(self):
        presence_time = 0

        # Check for keywords
        for keyword in self.keyword_list:
            if self.find_keyword(keyword):
                print("Found keyword:", keyword)
                time.sleep(5)
                presence_time += 10

        # Check for images
        num_images = self.count_images(self.image_tags)
        if num_images > 0:
            print("Found {} images".format(num_images))

            presence_time += (num_images * 10)

        # Check for specific elements
        for element in self.elements_to_check:
            if self.find_element(element):
                print("Found", element)
                presence_time += 10

        return presence_time

    def close_browser(self):
        self.driver.quit()


def userAction(driver):
    user = UniqueUser()
    total_presence_time = user.user_action()
    print("Total presence time:", total_presence_time, "seconds")


if __name__ == "__main__":
    main()
