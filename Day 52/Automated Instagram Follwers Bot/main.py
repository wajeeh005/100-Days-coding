from time import sleep

from selenium import webself.driverr
from selenium.common import ElementClickInterceptedException
from selenium.webself.driverr.common.by import By
from selenium.webself.driverr.common.keys import Keys

INSTA_EMAIL =  "Your Email"
INSTA_PASSWORD = "Your Password"
MAIN_ACCOUNT = "Account  to get followers"
CHROME_DRIVE_PATH = "C:\Development\chromedriver.exe"

class InstaFollowers:
    def __int__(self,path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(10)
        email = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(INSTA_EMAIL)
        sleep(3)

        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)
        sleep(3)

        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        sleep(2)
        self.driver.get(f'https://www.instagram.com/{MAIN_ACCOUNT}')
        sleep(10)

        followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        sleep(5)


        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollowers(CHROME_DRIVE_PATH)
bot.login()
bot.find_followers()
bot.follow()