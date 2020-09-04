import unittest
from selenium import webdriver

class test(unittest.TestCase):
    def setUp(self) -> None:
        PATH = "/Users/daominyang/Documents/chromedriver 2"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.facebook.com")

    def tearDown(self) -> None:
        self.driver.close()

    def test1(self):
        title = self.driver.title
        print(title)
        self.assertNotEqual("Facebook", title, "The title of the page is not expected!")

if __name__ == "__main__":
    unittest.main()



