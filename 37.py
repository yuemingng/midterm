numc=int(input("insert number :"))
def threen(numc):
    if numc ==1:
        return 1
    elif numc%2 == 0:
        numc = numc/2
        print(round(numc),end=" ")
    else:
        numc = 3*numc+1
        print(round(numc),end=" ")
    return threen(numc)+1
threen(numc)+1
print()
