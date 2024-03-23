
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://instagram.com")
sleep(4)

#giriş bilgileri
driver.find_element_by_xpath("//input[@name='username']")\
    .send_keys("karavandayasamhayalim")
driver.find_element_by_xpath("//input[@name='password']")\
    .send_keys("852147Yen.")
driver.find_element_by_xpath("//button[@type='submit']")\
    .click()
sleep(3)

#sifrekayitiptali
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
    .click()
sleep(2)

#sifrekayitiptali
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
    .click()
sleep(2)

#bildirimiptali
driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")\
    .click()
sleep(2)

#takip et
for i in range(3):
    for i in range(10):
        driver.find_element_by_xpath("//button[text()='Takip Et']")\
            .click()
        sleep(2)
    driver.refresh()  #sayfayı yenile
    continue