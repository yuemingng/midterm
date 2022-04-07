turn=10
while turn!=0:
    t = list(input("請輸入顔色").split())
    turn-=1
    a = ['red','blue','red','green']
    answer = [1,1,1,1]
    for i in range(4):
        if t[i] == a[i]:
            t[i] = 1
        elif t[i] not in ('red','blue','green'):
           t[i] = 3
        else:
           t[i]=2
    if t == answer:
        print("正確答案")
        break
    else:
        print(F'{t[0]}{t[1]}{t[2]}{t[3]}')
    if turn==0:
        print("挑戰失敗")