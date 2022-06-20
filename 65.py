f1 = input("請輸入A的好友 : ").split(" ")
f2 = input("請輸入B的好友 : ").split(" ")

s1 = set(f1)
s2 = set(f2)

t = s1 & s2
ans = len(t)
print(ans)