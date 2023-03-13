#login with correct username and incorrect password
from selenium import webdriver
driver = webdriver

driver.get("https://practiceautomation.com/practice-test-login/")
driver.find_element_by_id("username").send_keys("student")
driver.find_element_by_id("password").send_keys("Password124")
driver.find_element_by_id("submit").click()