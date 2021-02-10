#!/usr/bin/python3
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep 
# webdriver path set 
browser = webdriver.Firefox(executable_path='/home/ashika/selenium/geckodriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
browser.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
sleep(3) 
browser.find_element_by_xpath("//*[@id='identifierId']").send_keys("ashikavikraman@gmail.com")
sleep(1)
browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(Keys.RETURN)
sleep(1)
browser.find_element_by_name("password").send_keys("beurself")
sleep(1)
browser.find_element_by_name("password").send_keys(Keys.RETURN)
sleep(15)
browser.close()