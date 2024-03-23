from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://instagram.com")
sleep(4)

# girisbilgileri

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input") \
    .send_keys("karavandayasamhayali")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input") \
    .send_keys("Delibedri78.")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]") \
    .click()
sleep(3)

# sifrekayitiptali

###driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
###.click()
###sleep(2)


# bildirimiptali

###driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
###.click()
###sleep(2)


# tümünügör

###driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")\
###.click()
###sleep(2)


###for i in range(3):
### for i in range(10):
###    driver.find_element_by_xpath("//button[text()='Takip Et']")\
###   .click()
###   sleep(2)

###2. kısım###

# hastag giriş
driver.get(f"https://www.instagram.com/explore/tags/vanlife/")
sleep(4)

# post seç

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[2]/div[1]/a") \
    .click()
sleep(2)

# beğen

driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button") \
    .click()
sleep(2)

# yorum yapma alanı
commentsub = driver.find_element_by_class_name('Ypffh')
commentsub.click()
commentsub = driver.find_element_by_class_name('Ypffh')
commentsub.send_keys("I love VanLife...")

driver.find_element_by_xpath("//button[@type='submit']") \
    .click()