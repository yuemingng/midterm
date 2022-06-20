first = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

ans1 = ((-b)+((b**2-4*first*c)**0.5))/(2*first)
ans2 = ((-b)-((b**2-4*first*c)**0.5))/(2*first)

if (b**2)-(4*first*c) > 0:
    print("%d" %ans1,"%d" %ans2)
elif (b**2)-(4*first*c) < 0:
    print("0")
elif (b**2)-(4*first*c) == 0:
    print("%d" %ans1,) 