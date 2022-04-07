chinese = int(input("請輸入國文成績："))
eng = int(input("請輸入英文成績"))
math = int(input("請輸入微積分成績"))
pe = int(input("請輸入體育成績"))
pro = int(input("請輸入程式設計成績"))
list1 = [chinese,eng,math,pe,pro]
list = []
total=0
for i in list1:
    list.append(i)
    total += i
    average= total/len(list)
    max_value = max(list)
    min_value = min(list)
print("平均分數%5.2f" % average)
print("最高分科目：",max_value,"分")
print("最低分科目:",min_value,"分")