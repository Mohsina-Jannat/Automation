import unittest
from selenium import webdriver
import time

class PlayVideoContent(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/home/mim/Downloads/chromedriver_linux64/chromedriver')

    def test_get_and_play_content(self):
        driver = self.driver
        driver.get('https://www.youtube.com/watch?v=CevxZvSJLk8')
        time.sleep(5)
        driver.refresh()
        time.sleep(180)


if __name__ == "__main__":
    unittest.main()


