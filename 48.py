a=int(input("輸入筆數"))
while(a!=0):
   a-=1
   b=input("輸入欲查詢單字")
   lang1 = {"Dog":"狗","Cat":"貓","Bear":"熊","Snake":"蛇"}
   print("%s中文意思為%s" % (b,lang1[b]))
   while a==0:
       break