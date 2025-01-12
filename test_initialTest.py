# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInitialTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_initialTest(self):
    # Test name: Initial Test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://kick.com/")
    # 2 | setWindowSize | 1470x860 | 
    self.driver.set_window_size(1470, 860)
    # 3 | click | linkText=Browse | 
    self.driver.find_element(By.LINK_TEXT, "Browse").click()
    # 4 | click | css=.category-tile:nth-child(1) > .z-\[3\] | 
    self.driver.find_element(By.CSS_SELECTOR, ".category-tile:nth-child(1) > .z-\\[3\\]").click()
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | click | css=.see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
    # 7 | click | css=.grid-item:nth-child(3) > .category-banner > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(3) > .category-banner > .relative > .w-full").click()
    # 8 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 9 | click | linkText=falkonn | 
    self.driver.find_element(By.LINK_TEXT, "falkonn").click()
    # 10 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 11 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 12 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 13 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 14 | click | css=.border-b:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)").click()
    # 15 | click | css=.see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
    # 16 | click | css=.grid-item:nth-child(2) .absolute > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(2) .absolute > .relative > .w-full").click()
    # 17 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 18 | mouseOver | css=.size-sm:nth-child(2) .inner-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 19 | click | css=.base-dialog | 
    self.driver.find_element(By.CSS_SELECTOR, ".base-dialog").click()
    # 20 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 21 | mouseOver | css=.size-sm:nth-child(2) .inner-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 22 | click | css=.border-b:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)").click()
    # 23 | click | css=.see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
    # 24 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 25 | click | css=.grid-item:nth-child(5) .group .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(5) .group .relative > .w-full").click()
    # 26 | mouseOver | css=.size-sm:nth-child(2) > .button-content | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) > .button-content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 27 | mouseOut | css=.size-sm:nth-child(2) > .button-content | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 28 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 29 | mouseOver | css=.size-sm:nth-child(2) .inner-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 30 | click | css=.vjs-big-play-button > .vjs-icon-placeholder | 
    self.driver.find_element(By.CSS_SELECTOR, ".vjs-big-play-button > .vjs-icon-placeholder").click()
    # 31 | click | css=.grid-item:nth-child(4) > .card-thumbnail-holder > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(4) > .card-thumbnail-holder > .relative > .w-full").click()
    # 32 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 33 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 34 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 35 | click | css=.border-b:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)").click()
    # 36 | click | css=.md\3Aoverflow-hidden:nth-child(2) .see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".md\\3Aoverflow-hidden:nth-child(2) .see-more-btn").click()
    # 37 | mouseOver | css=.grid-item:nth-child(5) .absolute > .relative > .w-full | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(5) .absolute > .relative > .w-full")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 38 | mouseOut | css=.grid-item:nth-child(5) .absolute > .relative > .w-full | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 39 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 40 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 41 | click | css=.grid-item:nth-child(4) > .category-banner > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(4) > .category-banner > .relative > .w-full").click()
    # 42 | click | css=.grid-item:nth-child(2) > .card-thumbnail-holder > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(2) > .card-thumbnail-holder > .relative > .w-full").click()
    # 43 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 44 | click | css=.size-sm:nth-child(2) > .button-content | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) > .button-content").click()
    # 45 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 46 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 47 | click | css=.border-b:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)").click()
    # 48 | click | css=.md\3Aoverflow-hidden:nth-child(2) .see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".md\\3Aoverflow-hidden:nth-child(2) .see-more-btn").click()
    # 49 | click | css=.grid-item:nth-child(2) .absolute > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(2) .absolute > .relative > .w-full").click()
    # 50 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 51 | mouseOver | css=.size-sm:nth-child(2) .inner-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 52 | click | css=.mt-5:nth-child(1) .see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-5:nth-child(1) .see-more-btn").click()
    # 53 | click | css=.grid-item:nth-child(3) .absolute > .relative > .w-full | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(3) .absolute > .relative > .w-full").click()
    # 54 | mouseOver | css=.size-sm:nth-child(2) .inner-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 55 | click | css=.size-sm:nth-child(2) .inner-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
    # 56 | click | css=.vjs-big-play-button > .vjs-icon-placeholder | 
    self.driver.find_element(By.CSS_SELECTOR, ".vjs-big-play-button > .vjs-icon-placeholder").click()
    # 57 | click | css=.mt-5:nth-child(1) .see-more-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-5:nth-child(1) .see-more-btn").click()
    # 58 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 59 | close |  | 
    self.driver.close()
  
