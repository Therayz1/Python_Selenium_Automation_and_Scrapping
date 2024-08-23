import requests
import json


while True:
    sehir = input("Lütfen Hava Durumu Bilgilerini öğrenmek İstediğin Şehrin Adını Yaz:")
    apikey = "649838368c254830e61ef9a8f32d43e7"
    adres = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apikey)
    baglan = requests.get(adres)
    sorgu = baglan.json()
    ulke = sorgu["sys"]["country"]
    sehir = sorgu["name"]
    havadurumu = sorgu["weather"][0]["description"]
    havasicaklikderecesi = sorgu["main"]["temp"]
    hissedilensicaklik = sorgu["main"]["feels_like"]
    minsicaklik = sorgu["main"]["temp_min"]
    maxsicaklik = sorgu["main"]["temp_max"]
    basinc = sorgu["main"]["pressure"]
    nem = sorgu["main"]["humidity"]
    print(" \n ","Ülke:",ulke," \n ","Şehriniz:",sehir," \n ","Hava Durumu:",havadurumu," \n ","Hava Sıcaklık Derecesi:", havasicaklikderecesi," \n ","Hissedilen Sıcaklık:",hissedilensicaklik," \n ", "Minimum Sıcaklık:",minsicaklik," \n ","Maksimum Sıcaklık:",maxsicaklik," \n ", "Basınç:",basinc, " \n ","Nem:", nem)
    
