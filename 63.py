a = int(input("請輸入正整數n : "))
ans = 0

for i in range(1,a):
    if a % i == 0 :
        ans = ans + i 

if ans == a :
    print("perfect")
elif ans > a :
    print("abundant")
elif ans < a :
    print("deficient")   