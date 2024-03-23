from selenium import webdriver

PROXY = "185.204.187.111:8369" # IP:PORT or HOST:PORT185.204.187.111:8300:8400:Kmw27k:Kmw27k
driver_path = "/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito");
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
#chrome.get("http://whatismyipaddress.com")
#chrome.get("https://google.com")
chrome.get("https://www.instagram.com/accounts/emailsignup/")
#chrome.get("https://email-fake.com/")