num = []
diff=0
t = int(input("輸入測試資料："))
while t!=0:
    t-=1
    for i in range(1,5):
        w = (int(input("依序輸入已知的前4項：第%d項"% i)))
        num.append(w)
    for i in range(len(num)):
        if num[1]-num[0]==num[2]-num[1]:
                diff=num[1]-num[0]
                fifth = num[3]+diff
                print(num[0],num[1],num[2],num[3],fifth)
                print("此等為等差數列")
                del num[0:9]
                break
                
        else:
                diff=num[2]-num[1]
                fifth = num[3]*diff
                print(num[0],num[1],num[2],num[3],fifth)
                print("此為等比數列")
                del num[0:9]
                break
    