from selenium import webdriver
import time
driver_path = "/Users/mustafaakgul/Documents/Apps/BotInstaScripts/include/chromedriver"
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.youtube.com")

#browser.get("Site başlığı : ", browser.title)   website title
#driver.back()  previous index
#driver.close()  only this section close

#driver.maximize_window()
#driver.set_window_size(800,600)
#driver.save_screenshot("/home/sinan/test.png")

#driver.page_source getting page source
"""
Açtığınız sayfanın kaynak koduna ulaşmak için ise page_source methodunu kullanmalısınız. Sayfa kaynağını aldıktan 
sonra bunu beautifulsoup gibi bir modüle aktarıp sonrasında istediğiniz yerleri keserek kendinize bir bot yazabilirsiniz.
"""

browser.refresh()
browser.get("https://www.google.com")

time.sleep(5)

browser.quit()