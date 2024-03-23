from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse
from selenium.webdriver.chrome.options import Options

#parser = argparse.ArgumentParser()
#group = parser.add_mutually_exclusive_group(required=True)
#parser.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
#parser.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")

#args = parser.parse_args()
ua = UserAgent()
userAgent = ua.random
print(userAgent)

options = Options()
#options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options,
                          executable_path=r"/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver")

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(8)