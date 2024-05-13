import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findKeyword(driver, keyword)->bool:
	# print(driver.page_source.lower())
	return keyword.lower() in driver.page_source.lower()

def imageCount(driver, tag_name)->int:
	return len(driver.find_elements(By.TAG_NAME,tag_name))

def userActions(action, driver, rewardTime, reqList)->float:
	totalTime = 0
	keywords = reqList
	if action.upper() == "KEYWORD":
		for key in keywords:
			if findKeyword(driver, key):
				print("found", key)
				time.sleep(rewardTime)
				totalTime += rewardTime
			else:
				print("not found")
	elif action.upper() == "IMAGE":
		tags = reqList
		for elements in tags:
			imageNum = imageCount(driver, elements)
			print("found", imageNum, elements, "elements")
			time.sleep(rewardTime)
			totalTime += (rewardTime*imageNum)
			if (imageNum == 0):
				print("no image(s) found")

	return totalTime

def userAction(driver):

	rewardTime = 5
	totalTime = userActions("KEYWORD", driver, rewardTime, ["hobbies", "engineer", "experience"])
	tag_name = ["img"]
	rewardTime= 10
	totalTime += userActions("IMAGE", driver, rewardTime, tag_name)
	time.sleep(totalTime)

	print("Presence Time:", totalTime)
