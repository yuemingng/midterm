n1=0
n = int(input("輸入小狗有可能跑到的n個地方"))
while n!=0:
    n-=1
    n1+=1
    k = int(input("小明猜想的點與家的距離,第%d點"%n1))
    if k%9==0 or k%11==0:
        print("第%d個點"%(n1),k)
    else:
        print()