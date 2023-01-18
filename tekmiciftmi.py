while True:
    try:
        x = int(input("Sayı Giriniz :"))
        kalan = x%2
        if kalan==0:
            print("Girdiğiniz Sayı Çift")
        else:
            print("Girdiğiniz Sayı Tek")
    except ValueError:
        print("Tip uyuşmazlığı : Lütfen sayı giriniz")
    