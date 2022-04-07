b=4
a=int(input("請輸入處理方式(1)字典(2)串列"))
while b!=0:
    if a==1:
        awards=input("請輸入獎牌")
        values=int(input("請輸入各獎牌數"))
        b-=1
        dict1={awards:values}
        items1=list(dict1.items())
        for name,score in items1:
            print("%s牌得到%d面"%(name,score)) 
    else:
        awards=input("請輸入獎牌")
        values=int(input("請輸入各獎牌數"))
        b-=1
        list=[awards]
        print("%s牌得到%d面"%(list[0],values))