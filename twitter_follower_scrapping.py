from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# WebDriver'ı başlatırken options parametresini kullanın
driver = webdriver.Chrome(executable_path=r"C:/Users/erayc/OneDrive/Masaüstü/chromedriver.exe", options=options)

url = "https://twitter.com/login"
driver.get(url)
time.sleep(3)
username = "kendi kullanıcı adınız"
password = "kendi şifreniz"

driver.maximize_window()
time.sleep(2)

ka = driver.find_element_by_xpath("//input[@autocomplete='username']")
ka.send_keys(username)
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(3)

sif = driver.find_element_by_xpath("//input[@autocomplete='current-password']")
sif.send_keys(password)
time.sleep(3)
sif.send_keys(Keys.ENTER)
time.sleep(2)

url = "https://twitter.com/hedef hesabın kullanıcı adı"
driver.get(url)
time.sleep(2)

takipci = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a") # Buraya hedef hesabın takipçileri için kendi x pathinizi kopyalayın
takipci.click()
time.sleep(2)
fol = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-1dbjc4n.r-1e5uvyk.r-6026j > div:nth-child(2) > nav > div > div.css-1dbjc4n.r-1adg3ll.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1udh08x > div > div:nth-child(2) > a > div > div > span") # Buraya hedef hesabın takipçileri için kendi x pathinizi kopyalayın
fol.click()
time.sleep(5)
# Takipçi listesini al
takipciliste = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div").find_elements_by_css_selector("css-901oao.css-1hf3ou5.r-14j79pv.r-18u37iz.r-37j5jr.r-1wvb978.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0") # Buraya hedef hesabın takipçileri için kendi x pathinizi kopyalayın ve istenilen alanın css selectorunu kopyalayın
sayac = 1
for i in takipciliste:
    print(f"{sayac}-{i.text}")
    sayac += 1
    sayac = sayac
time.sleep(3)
driver.close()
