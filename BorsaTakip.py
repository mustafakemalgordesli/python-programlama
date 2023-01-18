import requests
import json
import time

adres="https://finans.truncgil.com/today.json"
durum=requests.get(adres)
veriler=durum.json()
güncellemeTarihi=veriler["Güncelleme Tarihi"]

gramAltın=veriler["Gram Altın"]
gramAltınAlış=gramAltın["Alış"]
gramAltınSatış=gramAltın["Satış"]
gramAltınyazı=("{} tarihinde \nGram Altın Alışı: {}.\nGram Altın Satışı: {}".format(güncellemeTarihi,gramAltınAlış,gramAltınSatış))

abdDoları=veriler["ABD DOLARI"]
abdDolarıAlış=abdDoları["Alış"]
abdDolarıSatış=abdDoları["Satış"]
abdDolarıYazı=("{} tarihinde \nUSD Alışı: {}.\nUSD Satışı: {}".format(güncellemeTarihi,abdDolarıAlış,abdDolarıSatış))

euro=veriler["EURO"]
euroalış=euro["Alış"]
eurosatış=euro["Satış"]
euroyazı=("{} tarihinde \nEURO Alışı: {}.\nEURO Satışı: {}".format(güncellemeTarihi,euroalış,eurosatış))

Sterlin=veriler["İNGİLİZ STERLİNİ"]
SterlinAlış=Sterlin["Alış"]
SterlinSatış=Sterlin["Satış"]
SterlinYazı=('{} tarihinde \İngiliz sterlini Alışı: {}.\nİngiliz sterlini Satışı: {}'.format(güncellemeTarihi,SterlinAlış,SterlinSatış))

while True:
    soru=input("Hangi Borsa Kurunu Merak Ediyorsun ?") 
    if soru=="USD" or soru=="usd":
        print(abdDolarıYazı)
        time.sleep(3)
    elif soru=="EURO" or soru=="euro" :
        print(euroyazı)
        time.sleep(3)
    elif soru=="sterlin" or soru=="STERLİN":
        print(SterlinYazı)
        time.sleep(3)
    elif soru=="ALTIN" or soru=="altın":
        print(gramAltınyazı)
        time.sleep(3)
    elif soru=="borsa çık" or soru=="BORSA ÇIK":
        print("Borsa Uygulamasından Çıkılıyor.")
        time.sleep(5)
        break
    else :
        print("Henüz Bunu Yapamıyorum.")
        print("Geri Bildirim için: m.alkan35@hotmail.com")
        time.sleep(5)
        break