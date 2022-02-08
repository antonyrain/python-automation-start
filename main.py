from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time


class SetWebDriver:

    def __init__(self, service, options):
        self.driver = webdriver.Chrome(service=service, options=options)

    def launch_browser(self, url):
        driver = self.driver
        driver.get(url)
        print(driver.page_source)

    def close_browser(self):
        self.driver.close()
        self.driver.quit()


def main():
    service = Service(executable_path="/path/to/chromedriver")
    lang = "en-US"
    window_size = "1200,800"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/98.0.4758.80 Safari/537.36 "

    options = Options()
    options.headless = False  # Headless Mode. Driving Headless Browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Disable " Chrome is being controlled
    # by automated test software " notification
    options.add_argument(f"--lang={lang}")
    options.add_argument(f"user-agent={user_agent}")
    # options.add_argument("--proxy-server=198.50.163.192:3129")  # set proxy
    options.add_argument(f"--window-size={window_size}")

    """
    _______________________________________________________________________
    ____________________Creating an instance of a class____________________
    _______________________________________________________________________
    """
    bot = SetWebDriver(service, options)
    bot.launch_browser("https://antonyrain.com/")
    time.sleep(random.randrange(10, 15))
    bot.close_browser()


if __name__ == "__main__":
    main()
