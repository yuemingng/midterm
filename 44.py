a = int(input("班級數量 : "))
list1 = []

for i in range(a):
    if a > 1 and a <= 10:
        n = int(input("輸入人數 : "))
        list1.append(n)
    else:
        break
    list1.sort(reverse=True)
print(list1[0])    