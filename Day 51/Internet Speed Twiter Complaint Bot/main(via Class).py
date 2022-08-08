import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
PROMISED_DOWN = 15
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Your Password"
TWITTER_USER_NAME = "Your User Name"


class InternetSpeedBot:
    def __int__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        starting_button = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        starting_button.click()
        sleep(60)

        up = self.driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        down = self.driver.find_element(By.XPATH,
                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(up, "is up and Down is ", down)
        if up < PROMISED_UP or down < PROMISED_DOWN:
            self.tweet_at_provider()
#
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(15)
        twitter_email_xpath = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        twitter_email_xpath.send_keys(TWITTER_EMAIL)
        sleep(10)
        next_button = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()
        sleep(10)

        phone_login = self.driver.find_element(By.CSS_SELECTOR,"div .css-1dbjc4n input")
        phone_login.send_keys(TWITTER_USER_NAME)
        phone_login.send_keys(Keys.ENTER)
        sleep(5)


        password_login = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_login.send_keys(TWITTER_PASSWORD)
        sleep(5)
        password_login.send_keys(Keys.ENTER)
        sleep(20)

        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(5)

        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedBot()
bot.get_internet_speed()

