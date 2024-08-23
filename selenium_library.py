from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:/Users/erayc/OneDrive/Masaüstü/chromedriver.exe")
driver.implicitly_wait(5)

url = "https://www.reuters.com/"
driver.get(url)
#print(driver.page_source)
time.sleep(3)
driver.refresh()
time.sleep(3)
time.sleep(5)
driver.maximize_window() # Penceryi tam ekran yapar
time.sleep(5)
url = "https://www.bloomberg.com/middleeast"
driver.get(url)
driver.save_screenshot("Ekrangoruntusu.png") # Ekran görüntüsü almamızı sağlar
driver.minimize_window() # Pencereyi sekme durumuna küçültür
time.sleep(5)
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.close()
