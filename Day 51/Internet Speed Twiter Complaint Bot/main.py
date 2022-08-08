import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

PRMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
# TWITTER_EMAIL = "spaow005@gmail.com"
# TWITTER_PASSWORD = "spaow005"
TWITTER_EMAIL = "wajeehul.hassan.311@gmail.com"
TWITTER_PASSWORD = "wajeeh.11"
#
# class InternetSpeedBot:
#
#     def __int__(self):
#         self.driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")
#         self.up = 10
#         self.down = 150
#
#     def get_internet_speed(self):
#         self.driver.get("https://www.speedtest.net/")
#
#         starting_button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
#         starting_button.click()
#         time.sleep(60)
#
#         self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
#         self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")
TWITTER_PHONE = "03085895267"
driver.get("https://twitter.com/i/flow/login")
time.sleep(15)
twitter_email_xpath = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
twitter_email_xpath.send_keys(TWITTER_EMAIL)
sleep(10)
next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_button.click()
time.sleep(10)
# recover = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
# recover.send_keys("@Syed_wajeeh05")
# time.sleep(10)
# next_button2 = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span')
# next_button2.click()
phone_login = driver.find_element(By.CSS_SELECTOR,"div .css-1dbjc4n input")
phone_login.send_keys(TWITTER_PHONE)
phone_login.send_keys(Keys.ENTER)
time.sleep(2)


password_login = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_login.send_keys(TWITTER_PASSWORD)
password_login.send_keys(Keys.ENTER)
time.sleep(1)




    # def tweet_at_provider(self):
    #     pass
#
#
# bot = InternetSpeedBot()
# bot.get_internet_speed()

