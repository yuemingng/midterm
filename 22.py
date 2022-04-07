g=int(input("請輸入數組"))
while (g!=0):
    while True:
        acc,pw=map(int,input("請輸入賬號與密碼").split())
        g-=1
        if acc==123 and pw==456:
            print("9000")
        elif acc==456 and pw==789:
            print("5000")
        elif acc==789 and pw==888:
            print("6000")
        elif acc==336 and pw==558:
            print("10000")
        elif acc==775 and pw==666:
            print("12000")
        elif acc==566 and pw==221:
            print("7000")
        else:
            print("error")
        if g==0:
            break