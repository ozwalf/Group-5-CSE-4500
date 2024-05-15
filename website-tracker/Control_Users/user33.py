from selenium import webdriver
import time

def count_instances(page_source, keyword):
    # Count occurrences of the keyword in the webpage content
    return page_source.lower().count(keyword.lower())

def count_images(page_source):
    # Count occurrences of the <img> tag in the webpage content
    return page_source.count("<img")

def count_urls(page_source):
    # Count occurrences of the <a> tag in the webpage content
    return page_source.count("<a href")

def userAction(driver):
    # Wait for the page to fully load
    time.sleep(2)

    # Get the HTML source of the webpage
    page_source = driver.page_source

    # Count instances of keyword, images, and URLs in the webpage content
    keyword_count = count_instances(page_source, "Jake")
    images_count = count_images(page_source)
    urls_count = count_urls(page_source)


    # Print individual counts
    print("Keyword Instances:", keyword_count)
    print("Image Instances:", images_count)
    print("URL Instances:", urls_count)

    # Sum up the total number of instances for all elements
    total_instances = keyword_count + images_count + urls_count

    time.sleep(total_instances)

if __name__ == "__main__":
    file_path = r"C:\Users\caleb\OneDrive\Documents\cse4500\assignment_1\aboutME.html"
    keyword = "Jake"  # Keyword to search for

    print("Running script against the local HTML file:")
    total_instances = main(file_path, keyword)
    print("Total Instances:", total_instances)
