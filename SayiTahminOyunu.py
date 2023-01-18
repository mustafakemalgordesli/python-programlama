import random # import ile random modülü kuruldu
import time  # import ile time modülü kuruldu
bss=random.randint(1,100) #Bilgisayar 1-100 arasından bir sayı seçer.
print("------------Sayı Tahmin Oyunu------------")

bts=int(input("Tuttuğum sayıyı tahmin et: ")) #Benden Bir sayı girmem istenir
print("-----------------------------------------")
while True: #while True sürekli tekrarla anlamındadır.
    if bss==bts:  #eğer benim tahmin ettiğim  sayı ile bilgisayarın seçtiği sayı aynı ise 
        print("Doğru Bildin. Tebrikler") #Doğru Bildin. Tebrikler yazar
        time.sleep(5) # kullanıcının görmesi için 5 sn bekleme verir
        break # döngüden çıkar
    elif bts>bss: # benim tahmin ettiğim sayı bilgisayarın tahmin ettiği sayıdan büyükse 
        bts=int(input("Daha küçük bir sayı dene: ")) # daha küçük bir sayı dene yazar.
        print("-----------------------------------------")
    else: # değilse
        bts=int(input("Daha büyük bir sayı dene: ")) # daha büyük bir sayı dene yazar.
        print("-----------------------------------------")
