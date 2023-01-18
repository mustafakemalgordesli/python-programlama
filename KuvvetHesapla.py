

import time
while(True):
    t=int(input("Tabanı Giriniz : " ))
    k=int(input("Kuvveti Giriniz : " ))
    a = 1
    s = 1
    while(a<=k):
        s=s*t
        a=a+1
    print(s)
    time.sleep(2)





