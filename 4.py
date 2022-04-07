X = int(input("請輸入X座標"))
Y = int(input("請輸入Y座標"))
D = X*X + Y*Y
if X>0 and Y>0:
    print("該點位於第一象限，離原點距離爲根號",D)
elif(X==0 and Y==0):
    print("該點位於原點")
elif(X==0 and Y>0):
    print("該點位於上半平面Y軸上，離原點的距離為根號",D)
elif(X<0 and Y==0):
    print("該點位於上半平面X軸上，離原點距離爲根號",D)