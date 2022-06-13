from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flight import Flight
import time


def scrape_flights():

    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx")
    time.sleep(5)
    data = []

    wait = WebDriverWait(driver, 30)
    numOfResults = driver.find_element_by_id('numOfResults')
    TotalnumOfResults = driver.find_element_by_id('totalItems')
    while numOfResults.text != TotalnumOfResults.text:
        wait.until(EC.element_to_be_clickable((By.ID, "next")))
        bt = driver.find_element_by_id("next")
        bt.click()
    if numOfResults.text == TotalnumOfResults.text:
        flight = driver.find_elements_by_xpath('//table[@id="flight_board-arrivel_table"]/tbody//tr')
        for f in flight:
            company_name = f.find_element_by_xpath('.//div[@class="td-airline"]').get_attribute("innerText")
            flight_number = f.find_element_by_xpath('.//div[@class="td-flight"]').get_attribute("innerText")
            from_country = f.find_element_by_xpath('.//div[@class="td-city"]').get_attribute("innerText")
            terminal = f.find_element_by_xpath('.//div[@class="td-terminal"]').get_attribute("innerText")
            expected_time = f.find_element_by_xpath('.//div[@class="td-scheduledTime"]').get_attribute("innerText")
            updated_time = f.find_element_by_xpath('.//div[@class="td-updatedTime"]').get_attribute("innerText")
            status = f.find_element_by_xpath('.//div[@class="td-status"]').get_attribute("innerText")
            data.append(Flight(company_name, flight_number, from_country, terminal,
                               expected_time, updated_time, status))
        print(data)

        driver.close()
        return data




