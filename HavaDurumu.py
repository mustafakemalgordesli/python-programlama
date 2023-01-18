import feedparser
import time


print("Lütfen il isminizi Türkçe Karekter KUllanmadan\nBüyük Harfle Giriniz.")
time.sleep(3)
il=input("*İLi Giriniz: ")
pk=input("*Posta Kodunu Giriniz: ")


def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|{}|{}|".format(pk,il))
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print ("Hava", parse[4], parse[5])
    time.sleep(3)
    return (hava)

hava()