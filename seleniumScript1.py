from selenium import webdriver
PATH = "/Users/daominyang/Documents/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.set_page_load_timeout(30)
#driver.get("https://techwithtim.net")
driver.get("http://www.facebook.com")
driver.maximize_window()
#driver.implicitly_wait(5)
driver.get_screenshot_as_file("Facebook1.png")
driver.find_elements_by_id("email").send_keys("Selenium Webdriver")
driver.find_elements_by_name("pass").send_keys("python")
driver.find_elements_by_id("loginbutton").click()
driver.get_screenshot_as_file("Facebook2.png")
print(driver.title)
driver.quit()