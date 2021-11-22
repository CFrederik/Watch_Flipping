#testing web-scraping 
import requests
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

path = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(path)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
google_cookies= driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
google_cookies.click()
time.sleep(2)
search_ricardo = driver.find_element_by_xpath('//input[@class = "gLFyf gsfi"]')
search_ricardo.click()
search_ricardo.send_keys("www.Ricardo.ch",Keys.ENTER)
select_url = driver.find_element_by_xpath('//div[@class="yuRUbf"]')
time.sleep(5)
select_url.click()
time.sleep(10)
ric_privacy_check = driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]')
ric_privacy_check.click()
time.sleep(2)
website_header = driver.find_element_by_xpath('//div[@class ="MuiInputBase-root MuiInput-root jss117 MuiInputBase-fullWidth MuiInput-fullWidth"]/input')
action = ActionChains(driver)
action.move_to_element(website_header).click().perform
website_header.send_keys("Garmin MARQ",Keys.ENTER)
time.sleep(30)
search_details = driver.find_element_by_xpath('//span[@class ="MuiButton-label"]')
time.sleep(5)
search_details.click()
time.sleep(5)


#response = requests.get('https://www.ricardo.ch/de/s/garmin%20marq/').content
#sel = Selector(text=response)

#website_header = sel.xpath('//div[@id="ricardo-spa"]').extract()
#print(website_header)

#[contains(@class, "MuiGrid-root link--2OHFZ MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 MuiGrid-grid-md-3")]


