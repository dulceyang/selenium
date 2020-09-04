from selenium import webdriver
PATH = "/Users/daominyang/Documents/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.set_page_load_timeout(30)
#driver.get("https://techwithtim.net")
driver.get("http://www.facebook.com")
driver.maximize_window()
#driver.implicitly_wait(5)
driver.get_screenshot_as_file("Facebook.png")
print(driver.title)
driver.quit()
