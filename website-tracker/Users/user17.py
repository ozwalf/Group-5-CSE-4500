import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findKeyword(driver, keyword)->bool:
	# print(driver.page_source.lower())
	return keyword.lower() in driver.page_source.lower()

def imageCount(driver, tag_name)->int:
	return len(driver.find_elements(By.TAG_NAME,tag_name))

def userAction(driver)->float:
	rewardTime = 10
	tags = ["img", "p"]
	totalTime = 0
		
	for elements in tags:
		imageNum = imageCount(driver, elements)
		print("found", imageNum, elements, "elements")
		time.sleep(rewardTime)
		totalTime += (rewardTime*imageNum)
		if (imageNum == 0):
			print("no image(s) found")

	return totalTime

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

totalTime = userAction(driver)
driver.quit()

print("Presence Time:", totalTime)
