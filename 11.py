M,D = map(int,input("請輸入日及月為：").split())
if M==1:
    if D<21:
        print("星座為：Capricorn")
    else:
        print("星座為：Aquarius")
elif M==2:
    if D<=18:
        print("星座為：Aquarius")
    else:
        print("星座為：Piesces")
elif M==3:
    if D<=20:
        print("星座為：Piesces")
    else:
        print("星座為：Aries")
elif M==4:
    if D<=20:
        print("星座為：Aries")
    else:
        print("星座為：Taurus")
elif M==5:
    if D<=21:
        print("星座為：Taurus")
    else:
        print("星座為：Gemini")
elif M==6:
    if D<=21:
        print("星座為：Gemini")
    else:
        print("星座為：Cancer")
elif M==7:
    if D<=22:
        print("星座為：Cancer")
    else:
        print("星座為：Leo")
elif M==8:
    if D<=23:
        print("星座為：Leo")
    else:
        print("星座為：Virgo")
elif M==9:
    if D<=23:
        print("星座為：Virgo")
    else:
        print("星座為：Libra")
elif M==10:
    if D<=23:
        print("星座為：Libra")
    else:
        print("星座為：Scorpio")
elif M==11:
    if D<=22:
        print("星座為：Scorpio")
    else:
        print("星座為：Sagittaurus")
elif M==12:
    if D<=23:
        print("星座為：Sagittaurus")
    else:
        print("星座為：Capricorn")