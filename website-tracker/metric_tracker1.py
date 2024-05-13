import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import strftime, localtime
import mysql.connector
from Users import user23 as user


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    # Connects to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pascal_16",
        database="4500final"
    )

    cursor = db.cursor()

    metrics = [
        ['Iteration', 'Variation', 'User', 'Presence_Time']
    ]

   
    # Iteration number
    iterationNum = 1
    # Control/Variant
    variantGroup = "Control"
    userNum = 23

    start_time = time.time()
    presence_time = start_time
    user.userAction(driver)
    current_time = time.time()

    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    # string query for mysql
    add_metric = ("INSERT INTO userdata (Iteration, Variant, User, Presence_Time) VALUES (%s, %s, %s, %s)")
    data_metric = (iterationNum, variantGroup, userNum, presence_time)
    cursor.execute(add_metric, data_metric)

        
    # saves/commits changes made to database
    db.commit()
    # closes cursor
    cursor.close()
    # closes database connection 
    db.close()

    print("End of script.")
    driver.quit()

if __name__ == "__main__":
    main()