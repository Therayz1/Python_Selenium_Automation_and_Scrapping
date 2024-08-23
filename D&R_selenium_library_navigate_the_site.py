from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options=Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:/Users/erayc/OneDrive/Masaüstü/chromedriver.exe",options = options)
driver.implicitly_wait(5)

url = "https://www.dr.com.tr/"
driver.get(url)
time.sleep(2)
driver.maximize_window()

time.sleep(2)
kitap = driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/div[2]/ul/li[1]/a")
kitap.click()

kitapara = driver.find_element_by_css_selector("body > div.site-container > header > div.site-header-center.bg-c255.py-10 > div > div > div.search.col-12.col-lg-7.mt-10.mt-lg-0.dr-flex > div.search-wrapper.col-12.col-lg-10.p-0 > input")
kitapara.send_keys("Şiir")
kitapara.send_keys(Keys.ENTER)


for i in range(1, 10):
    bilgi = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/main/div[2]/div[1]/div[{}]/div/div[3]/div[1]/div[2]/h3[1]/a".format(i))
    yazarlar = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/main/div[2]/div[1]/div[{}]/div/div[3]/div[1]/div[2]/h3[2]/a".format(i))
    
    # Şair ve yazarı birleştirerek çıktı oluşturun
    kitap_bilgisi = "{} - Yazar: {}".format(bilgi.text, yazarlar.text)
    print(kitap_bilgisi)

driver.close()
