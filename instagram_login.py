from selenium import webdriver
import time
driver_path = "/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver"
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.instagram.com")

time.sleep(5) #sayfa yklensin ve ayrica bot gibi gzkmesn
#sayfa yklenmesse hata alırız


"""
login bilgilerde id var ve syfa heryuklennce degisiyor xpath id ile calısır o yzden
xpath ypmaaycaggz
x path yerine name den gidilcek
"""


"""
sag tıkla login butona inspect de copy to xpath de koda yapstr
"""

#//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a

#giris sayfasnda login gozukuyor ise yni acilis signup olarak glyrsa
#login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/div/p/a")
#login.click()

time.sleep(5)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("nyil0376@gmail.com")
password.send_keys("nehir123456")

login_button = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
login_button.click()

time.sleep(30)
browser.close()