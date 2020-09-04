from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "/Users/daominyang/Documents/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get("https://client.schwab.com")
print(driver.title)
login_form = driver.swit
#log_ele = driver.find_elements_by_xpath("//*[@id='loginContainer']/div/section[1]/div[2]")
# print(f'the input_box Password is displayed {log_ele.is_displayed()}')
# print(f'the input_box Password is enabled as {log_ele.is_enabled()}')
print(log_ele.is_displayed())



driver.get("http://facebook.com/")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.quit()