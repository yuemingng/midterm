w = 3
for i in range(0,4):
    a=''
    for j in range(0,w-i):
        a += " "
    for k in range(0,2*i+1):
        a+='*'
    print(a)
g = 4
for i in range(3,0,-1):
    a=''
    for j in range(0,g-i):
        a += " "
    for k in range(0,2*i-1):
        a+='*'
    print(a)