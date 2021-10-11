import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class CoinInfo:

    def get_soup(self, coin_name):
        url = "https://coinmarketcap.com/currencies/" + coin_name + "/news/"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        time.sleep(3)
        for i in range(4):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            element = driver.find_element(By.XPATH, '//button[text()="Load More"]')
            driver.execute_script("arguments[0].click();", element)
            element.click()
            time.sleep(3)


        return BeautifulSoup(driver.page_source,"lxml")

    def get_paragraphs(self, coin_name):
        soup = self.get_soup(coin_name)
        news = soup.find_all("div", {"class": "svowul-5 czQlor"})
        ls = []
        for i in news:
            ls.append({"title": i.h3.text, "body": i.p.text, "link": i.a.get("href")})
        return ls

    def output_paragraphs(self, coin_name):
        soup = self.get_soup(coin_name)
        news = soup.find_all("div", {"class": "svowul-5 czQlor"})
        num = 1
        for i in news:
            if (i.p):
                print(str(num) + ")     Title : " + i.h3.text + ".\n    Link: "+ i.a.get("href"))
                print("Briefly: " + i.p.text)
                print("############################################################################################################")
                num+=1



        

