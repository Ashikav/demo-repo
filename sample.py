#!/usr/bin/python3
from selenium import webdriver
import unittest
from time import sleep
class TestOrangeHRM(unittest.TestCase):
    
    def setUp(self):
       
        self.browser = webdriver.Firefox(executable_path='/home/ashika/selenium/geckodriver')
        self.browser.set_window_size(900,900)
        sleep(1)
        self.browser.set_window_position(0,0)
        self.browser.get("https://opensource-demo.orangehrmlive.com/")
    def tearDown(self):
        self.browser.close()

        
    
    def test_homePage(self):
        # self.setup()
        print("testing")
        # self.browser.get("https://opensource-demo.orangehrmlive.com/")
        assert self.browser.title =="OrangeHRM"
        sleep(2)
    
    
    def test_login(self):
        # self.setup()
        # self.browser.get("https://opensource-demo.orangehrmlive.com/")
        print("testing1")
        self.browser.find_element_by_id("txtUsername").send_keys("Admin")
        if 'txtUsername' in 'Admin':
            print("Passed")
        else:
            print("Failed")
        self.browser.find_element_by_id("txtPassword").send_keys("admin123")
        self.browser.find_element_by_id("btnLogin").click()
        assert self.browser.title =="OrangeHRM"
        sleep(15)

if __name__ == "__main__":
   unittest.main()