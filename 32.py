t=0
drink=0
list_of_drink = []
while True:
    m = int(input("小明身上有幾元："))
    if m==0:
        break
    while 0<=m<=100:
        n = int(input("販賣機有幾種飲料："))
        while n!=0 and 1<=n<=30:
            n-=1
            t+=1
            list_of_drink.append(int(input("第%d飲料的價格：" % t))) 
        for i in range (len(list_of_drink)):
            if m==list_of_drink[i] or m>list_of_drink[i]:
                drink+=1
            else:
                drink+=0
        print(drink)
        if n==0:
            break