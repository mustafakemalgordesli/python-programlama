import time
sayi1=0
sayi2=1
fibonacciSayisi=0
while fibonacciSayisi<150:
    print(fibonacciSayisi)
    fibonacciSayisi+=sayi2
    sayi2=sayi1
    sayi1=fibonacciSayisi
time.sleep(10)