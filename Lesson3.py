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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    output= text.split(":")[1]
    return output

def write_file(text):
    filename = f'{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt'
    with open(filename , 'w') as file:
        file.write(text)

def main():
    driver=get_driver()
    time.sleep(2)
    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id",value="id_password").send_keys("*******" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    i =0
    while True:
        i += 1
        time.sleep(2)
        temp = driver.find_element(by="id",value="displaytimer").text
        write_file(clean_text(temp))
        if i >= 9:
            False
            break




print(main())