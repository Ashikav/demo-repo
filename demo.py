#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Firefox(executable_path='/home/ashika/selenium/geckodriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)
browser.get("https://en.wikipedia.org/wiki/Home_page")
# assert 'Wikipedia' in browser.title
sleep(1)
browser.find_element_by_id("searchInput").send_keys("Selenium")
sleep(2)
browser.find_element_by_id("searchInput").send_keys(Keys.RETURN)

sleep(5)
browser.close()
