from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class LazadaBot:
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.bot = webdriver.Chrome("./chromedriver.exe", chrome_options=self.options)

    def search(self, search_keyword):
        bot = self.bot
        bot.get("https://www.lazada.sg/")
        time.sleep(1.5)
        search_bar = bot.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[1]/input[1]")
        search_bar.send_keys(search_keyword)
        search_bar.submit()
        time.sleep(1.5)

        listings = bot.find_elements_by_class_name("c2prKC")
        items = {}
        urls = {}
        # Loop through listings that fit class name
        for counter, listing in enumerate(bot.find_elements_by_class_name("c2prKC")):
            desc_box = listing.find_element_by_class_name("c16H9d").find_elements_by_xpath(".//*")[0]
            desc = desc_box.text
            product_url = desc_box.get_attribute("href")
            price = float(listing.find_element_by_class_name("c13VH6").text.replace("$", ""))
            if price < 100:
                continue
            try:
                review = listing.find_element_by_class_name("c3XbGJ").text
            except:
                review = "(No reviews)"
            items[desc] = {}
            items[desc]["price"] = price
            items[desc]["review"] = review
            urls[desc] = product_url
            # print(f"{counter+1}: {desc[:20]} {price} {review}")
            # print(f"{product_url}")
        return items, urls

    def get_product_details(self, product_url):
        bot = self.bot
        bot.get(product_url)
        time.sleep(1)
        main_block = bot.find_element_by_class_name("pdp-block.pdp-block__product-detail")
        try:
            flashsale_text = main_block.find_element_by_class_name("crazy-deal-details-notstart").find_element_by_class_name("content-wrapper").find_elements_by_xpath(".//*")[0].text
        except:
            flashsale_text = "No flash sale"
        try:
            right_block = main_block.find_element_by_class_name("pdp-block.pdp-block__delivery-seller")
            warranty_info = right_block.find_elements_by_xpath("delivery-option-item__title")
            warranty_details = [x.text for x in warranty_info]
        except:
            warranty_details = ["No Warranty details"]
        print(f"{product_url}: {warranty_details}")
        print(f"{flashsale_text}")
        pass

lazada = LazadaBot()
search_list = ["UE MegaBoom 3"]
for search_term in search_list:
    items, urls = lazada.search(search_term)
    for url in urls.values():
        lazada.get_product_details(url)

lazada.bot.quit()
