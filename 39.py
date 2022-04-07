for i in range(5):
    for j in range(4-i):
        print(" ",end='')
    for j in range(2*i+1):
        if j%2==0:
            print("*",end='')
        if j%2==1:
            print(" ",end='')
    print()
for i in range(4,0,-1):
    for j in range(5-i):
        print(" ",end='')
    for j in range(2*i-1):
        if j%2==0:
            print("*",end='')
        if j%2==1:
            print(" ",end='')
    print()