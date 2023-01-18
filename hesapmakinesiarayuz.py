def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2


import time
while True:
    print("Operasyon:")
    print("1 : Topla")
    print("2 : Çıkar")
    print("3 : Çarp")
    print("4 : Böl")
    
    print("0 : Çıkış")
    
    secenek = input("Operasyon seçiminiz:")
    
    
    try:
        if secenek == '1':
            sayi1 = int(input("Birinci sayı?"))
            sayi2 = int(input("İkinci sayı?"))
            print(str(sayi1)+" + "+str(sayi2)+" = " +str(topla(sayi1,sayi2)))
            time.sleep(1)
        elif secenek == '2':
            sayi1 = int(input("Birinci sayı?"))
            sayi2 = int(input("İkinci sayı?"))
            print(str(sayi1)+" - "+str(sayi2)+" = "  +str(cikar(sayi1,sayi2)))
            time.sleep(1)
        elif secenek == '3':
            sayi1 = int(input("Birinci sayı?"))
            sayi2 = int(input("İkinci sayı?"))
            print(str(sayi1)+" * "+str(sayi2)+" = " +str(carp(sayi1,sayi2)))
            time.sleep(1)
        elif secenek == '4':
            sayi1 = int(input("Birinci sayı?"))
            sayi2 = int(input("İkinci sayı?"))
            print(str(sayi1)+" / "+str(sayi2)+" = "  +str(bol(sayi1,sayi2)))
            time.sleep(1)
        elif secenek== '0':
            print("Çıkış Yapıldı")
            time.sleep(1)
            break
        else:
            print("Geçersiz seçenek")
            time.sleep(1)
    except ValueError:
        print("Tip uyuşmazlığı : Lütfen sayı giriniz")
        time.sleep(1)
    except ZeroDivisionError:
        print("Payda sıfır olamaz")
        time.sleep(1)
    except:
        print("Bir hata oluştu")
        time.sleep(1)
    

