a = int(input("請輸入要判斷的第一個數字 : "))
b = int(input("請輸入要判斷的第二個數字 : "))
ans1=0
ans2=0

if a + 2 == b :
    for i in range(1,a):
        if a % i == 0 :
            ans1 = ans1 + 1
    for i in range(1,b):
        if b % i == 0 :
            ans2 = ans2 + 1  
            
if ans1 != 1 :
    print("N")
elif ans2 != 1:
    print("N")
elif ans1 == 1 :
    print("Y")
elif ans2 == 1 :
    print("Y")   