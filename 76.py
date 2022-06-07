ans=""
password = input("請輸入傳送密碼(6位數):")
if len(password)==6:
    finalpassword= list(password)
    for i in range(0,len(password)):
            for j in range(0,10):
                if j*4%7 == int(finalpassword[i]):
                    ans+=str(j)
                    break
print("解密後密碼為:"+ans)