qes='1234'
a=0
b=0
while True:
    ans=input("請輸入一連串的4位數字")
    for i in range(len(qes)):
        if ans[i] in qes and ans[i]==qes[i]:
            a+=1
        elif ans[i] in qes and ans[i]!=qes[i]:
            b+=1
    print(str(a)+"A"+str(b)+"B")
    if ans=='0000':
        break
    