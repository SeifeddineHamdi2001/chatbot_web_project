from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class CrawledArticle():
    def __init__(self, title, price, Memory, GraphicsCard, Cpu, Storage):
        self.title = title
        self.price = price
        self.Memory = Memory
        self.GraphicsCard = GraphicsCard
        self.Cpu = Cpu
        self.Storage = Storage


class Bot:
    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 20
        maxRetrieves = 368
        a = []

        url = "https://spacenet.tn/categorie/74-pc-portable?page=" + str(page)
        s = Service("C:\Program Files (x86)\chromedriver.exe")
        options = Options()
        options.headless = True
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=s)
        browser.maximize_window()
        url = "https://spacenet.tn/categorie/74-pc-portable?page=" + str(page)
        browser.get(url)
        browser.set_page_load_timeout(10)

        while True:
            try:
                if pageIncrement * page > maxRetrieves:
                    break
                if count > pageIncrement:
                    count = 1
                    page += 1

                # Get Title
                xPathTitle = '//*[@id="box-product-grid"]/div/div[' + str(count) + ']/div/div/div[2]/div[2]/a'
                title = browser.find_element(By.XPATH, xPathTitle)
                titleText = title.get_attribute("innerHTML")
                title.click()
                xPathPrice = '//*[@id="main"]/div[1]/div[3]/div/div[1]/div[1]/div/span'
                price = browser.find_element(By.XPATH, xPathPrice)
                priceText = price.get_attribute("innerHTML")
                xPathMemory = '//*[@id="product-details"]/section[1]/dl/dd[2]'
                Memory = browser.find_element(By.XPATH, xPathMemory)
                MemoryText = Memory.get_attribute("innerHTML")
                xPathGraphicsCard = '//*[@id="product-details"]/section[1]/dl/dd[3]'
                GraphicsCard = browser.find_element(By.XPATH, xPathGraphicsCard)
                GraphicsCardText = GraphicsCard.get_attribute("innerHTML")
                xPathCpu = '//*[@id="product-details"]/section[1]/dl/dd[15]'
                Cpu = browser.find_element(By.XPATH, xPathCpu)
                CpuText = Cpu.get_attribute("innerHTML")
                xPathStorage = '//*[@id="product-details"]/section[1]/dl/dd[10]'
                Storage = browser.find_element(By.XPATH, xPathStorage)
                StorageText = Storage.get_attribute("innerHTML")

                url = "https://spacenet.tn/categorie/74-pc-portable?page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)
                info = CrawledArticle(titleText, priceText, MemoryText, GraphicsCardText, CpuText, StorageText)
                a.append(info)
                count += 1



            except Exception as e:
                print("Exception", e)
                count += 1
                if pageIncrement * page > maxRetrieves:
                    break
                if count > pageIncrement:
                    count = 1
                    page += 1
                url = "https://spacenet.tn/categorie/74-pc-portable?page="+ str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)

        browser.close()
        return a


fetcher = Bot()

with open("results.csv", "w", newline="", encoding="utf-8") as csvfile:
    articleWriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for article in fetcher.article('pc portable'):
        articleWriter.writerow({article.title, article.price,article.GraphicsCard,article.Cpu,article.Storage,article.Memory })
