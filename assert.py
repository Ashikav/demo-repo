#!/usr/bin/python3
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep 
# webdriver path set 
browser = webdriver.Firefox(executable_path='/home/ashika/selenium/geckodriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
browser.get("https://www.google.com/")
sleep(1)
try:
    assert "Google Site" in browser.title, "Verification Failed"
except AssertionError as exception:
    print("Verification Failed")

# assert 
sleep(2)
browser.close()