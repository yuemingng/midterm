while True:
    n = int(input("輸入一正整數："))
    if n<=10 or n>=1001:
           break
    while(11<=n<=1000):
        if n%2==0 and n%11==0:
            print(n,"為新公倍數？：YES")
            break
        elif n%5!=0 and n%7!=0:
            print(n,"為新公倍數？：YES")
            break
        else:
            print(n,"為新公倍數？：NO")
            break
        