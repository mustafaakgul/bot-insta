import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import bot_test_1.accountInfoGenerator as account
import bot_test_1.getVerifCode as verifiCode
from selenium import webdriver
import time
import argparse
from selenium.webdriver.chrome.options import Options

def getFakeMail():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find_all("span", {"id": "email_ch_text"})
    print(mail)
    print(mail[0])
    print(mail[0].contents)
    return mail[0].contents


driver_path = "/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito");
chrome = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
#chrome.get("http://whatismyipaddress.com")
#chrome.get("https://google.com")
#chrome.get("https://www.instagram.com/accounts/emailsignup/")
fake_email = getFakeMail()
print(fake_email)

fMail = fake_email[0].split("@")
mailName = fMail[0]
domain = fMail[1]

instCode = verifiCode.getInstVeriCode(mailName, domain, chrome)
print(instCode)

