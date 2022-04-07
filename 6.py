f,t = map(int,input("請輸入月租費及通話時間").split(","))
if f==186:
    if (t*0.09)<f:
        print("通話費為",f)
    elif f<(t*0.09)<f*2:
        print("通話費為",round(t*0.09*0.9))
    elif (t*0.09)>f*2:
        print("通話費為",round(t*0.09*0.8))
elif f==386:
    if t*0.08<f:
        print("通話費為",f)
    elif (t*0.08)>f*2:
        print("通話費為",round(t*0.08*0.7))
    elif f<t*0.08<f*2:
        ("通話費為",round(t*0.08*0.8))
elif f==586:
    if t*0.07<f:
        print("通話費為",f)
    elif f<(t*0.07)<f*2:
        print("通話費為",round(t*0.07*0.7))
    elif (t*0.07)>f*2:
        ("通話費為",round(t*0.07*0.6))
elif f==986:
    if t*0.06<f:
        print("通話費為",f)
    elif f<(t*0.06)<f*2:
        print("通話費為",round(t*0.06*0.6))
    elif (t*0.06)>f*2:
        ("通話費為",round(t*0.06*0.5))

