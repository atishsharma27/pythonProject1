#login with correct username and password
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Atish/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element_by_id("username").send_keys("student")
driver.find_element_by_id("password").send_keys("Password123")
driver.find_element_by_id("submit").click()
driver.maximize_window()
driver.find_element_by_link_text("Log out").click()
driver.current_url
print(driver.current_url)














