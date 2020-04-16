from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/")
        time.sleep(5)
        email_input = bot.find_element_by_name("username")
        password_input = bot.find_element_by_name("password")
        email_input.clear()
        password_input.clear()
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        password_input.submit()
        time.sleep(3)

    def like_photos(self):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/")
        time.sleep(3)
        for i in range(1,2):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
        body = bot.find_element_by_class_name("K6yM_")
        pictures = body.find_elements_by_xpath('//a')
        print(pictures)
        links = []
        for picture in pictures:
            link = picture.get_attribute("href")
            if link.split("/")[-3] == "p":
                links.append(link)
        for link in links:
            bot.get(link)
            time.sleep(1)
            like_button = bot.find_element_by_class_name("wpO6b")
            like_button.click()
            time.sleep(1)




hidey = InstagramBot('kanazawahideyuki@gmail.com', 'Physicsmath!7')
hidey.login()
hidey.like_photos()