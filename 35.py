sA = input("輸入字串sA：")
sB = list(input("輸入字串sB：").split())
list_a = []
list_a.append(sA)
for i in range (len(list_a)):
    if list_a[i] in sB:
        print("YES")
    else:
        print("NO")