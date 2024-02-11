from selenium import webdriver
import time
from datetime import datetime as dt
from selenium.webdriver.common.keys import Keys
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-Atuomation"])
    options.add_argument("disable-blink-features=AtuomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://finance.yahoo.com")
    return driver

def download_historical_data():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by="id", value="yfin-usr-qry").send_keys("TI.NS" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="//*[@id=\"quote-nav\"]/ul/li[5]/a/span").click()
    time.sleep(2)
    driver.find_element(by="xpath",value="//*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section/div[1]/div[2]/span[2]/a/span").click()
    time.sleep(5)


def main():
    download_historical_data()