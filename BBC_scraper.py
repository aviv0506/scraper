from selenium import webdriver
import time

def scrape_BBC_articles():
    driver = webdriver.Chrome('./chromedriver')
    data = []

    driver.get("https://www.bbc.com/")
    time.sleep(2)

    #Get links from main page
    links = [elem.get_attribute("href") for elem in driver.find_elements_by_class_name('media__link')]
    i = 0

    for x in links:

        driver.get(x)  # Go to each link
        time.sleep(2)
        x = driver.current_url

        time.sleep(5)
        elements = driver.find_element_by_tag_name('article')  # Copy the data of the article

        time.sleep(4)
        data.append([x, elements.text])
        time.sleep(2)

    driver.close()
    return data





