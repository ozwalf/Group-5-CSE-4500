import os
import time
import csv
import importlib.util
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import strftime, localtime
import mysql.connector

def import_user_module(user_module_name):
    module_path = f'./Control_Users/{user_module_name}.py'
    spec = importlib.util.spec_from_file_location(user_module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

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
    metrics = [['Iteration', 'Variation', 'User', 'Presence_Time']]
   
    # List all user modules in the directory
    user_files = os.listdir('./Control_Users')
    for user_file in user_files:
        if user_file.endswith('.py') and user_file.startswith('user'):
            user_module_name = user_file[:-3]  # Strip the '.py' to get the module name
            user_num = user_file[4:-3] # Strip both 'user' and '.py' to get the user number
            user_module = import_user_module(user_module_name)

            print(f"┌--Testing {user_module_name}-------┐")
            # Execution part
            start_time = time.time()
            user_module.userAction(driver)  # Execute user action
            presence_time = time.time() - start_time
            print(f"Presence time: {presence_time} seconds")
            print(f"└--Done testing {user_module_name}--┘")
            # Database insertion
            add_metric = ("INSERT INTO userdata (Iteration, Variant, User, Presence_Time) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE Presence_Time=%s")
            data_metric = (2, "Control", user_num, presence_time, presence_time)
            cursor.execute(add_metric, data_metric)
    
            # Commit changes to database
            db.commit()

    # Clean up
    cursor.close()
    db.close()
    driver.quit()
    print("End of script.")

if __name__ == "__main__":
    main()
