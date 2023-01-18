cevap="e"
while cevap== "e" or cevap== "E":
    
    isim=input("Öğrencinin adını girin:")
    not1=int(input("1. notu girin:"))
    not2=int(input("2. notu girin :"))
    ort=(not1+not2)/2
    if not1>100 or not2>100 or not1<0 or not2<0:
        print("Hatalı Not Girdiniz")
    else:
        if ort>=50:
            print("{}, {} ortalama ile geçti.".format(isim,ort))
        else:
            print("{}, {} ortalama ile kaldı.".format(isim,ort))
    cevap=input("Tekrar hesaplamak istermisiniz ?(e/h)")