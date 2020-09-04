from selenium import webdriver

PATH = "/Users/daominyang/Documents/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get("https://client.schwab.com")
print(driver.title)

def display_cookies():
    cookies = driver.get_cookies()
    for c in cookies:
        print(c)
    print(len(cookies))
mycook = {'domain': '.schwab.com', 'name': 'Mycookie', 'value': '1234567'}
driver.add_cookie(mycook)
display_cookies()
driver.quit()
