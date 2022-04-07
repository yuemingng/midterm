j=total=0
r=int(input("請輸入組數")) 
while (r!=0):
    j+=1
    f,h = map(int,input("第%d組"%(j)).split())
    total=f*250+h*175
    print("第%d組應收費用:%d" %(j,total))
    if j==r:
        break