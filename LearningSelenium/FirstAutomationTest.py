from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Atish/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()
