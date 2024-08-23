from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# WebDriver'ı başlatırken options parametresini kullanın
driver = webdriver.Chrome(executable_path=r"C:/Users/erayc/OneDrive/Masaüstü/chromedriver.exe", options=options)

url = "https://www.instagram.com/accounts/login/"
driver.get(url)
time.sleep(3)

username = "kullanıcı adınızı buraya girin"
password = "Şifrenizi buraya girin"

ka = driver.find_element_by_xpath("kullanıcı adı xpathinizi buraya giriniz")
ka.send_keys(username)
sifre = driver.find_element_by_xpath("şifre xpathinizi buraya gidiniz")
sifre.send_keys(password)
sifre.send_keys(Keys.ENTER)
time.sleep(3)

# Takipçi sayfasına git
takipci_sayfasi = "https://www.instagram.com/bakmak istediğiniz hesabın kullanıcı adı/"
driver.get(takipci_sayfasi)
time.sleep(3)

# Takipçi sayısını çek
takipci_sayisi = driver.find_element_by_xpath("buraya takipçisini çekmek istediğiniz hesabın xpathini çekin")
print("Takipçi Sayısı:", takipci_sayisi.text)

driver.maximize_window()
