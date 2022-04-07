str1 = input("請輸入第一字串")
str2 = input("請輸入第二字串")
list_a = []
list_a.append(str1)
for i in range (len(list_a)):
    if list_a[i] in str2 :
        print("YES")
    else:
        print("NO")