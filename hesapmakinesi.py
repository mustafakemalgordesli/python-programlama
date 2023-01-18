while True:
    print("Merhaba Hesap Makinesine Hoşgeldin!")
    print("1-Toplama 2-Çıkarma 3-Bölme 4-Çarpma 0-ÇIKIŞ")
    print("-" * 30)
    islem = int(input("işlem seçin="))
    if islem == 0:
        break
    if islem == 1:
        sayi1 = int(input("1.sayıyı girin="))
        sayi2 = int(input("2.sayıyı girin="))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    if islem == 2:
        sayi1 = int(input("1.sayıyı girin="))
        sayi2 = int(input("2.sayıyı girin="))
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
    if islem == 3:
        sayi1 = int(input("1.sayıyı girin="))
        sayi2 = int(input("2.sayıyı girin="))
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
    if islem == 4:
        sayi1 = int(input("1.sayıyı girin="))
        sayi2 = int(input("2.sayıyı girin="))
        print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
print("Çıkış Yapıldı")
