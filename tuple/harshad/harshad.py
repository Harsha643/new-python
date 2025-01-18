num=input("enter")#123
res=0
for i in range(0,len(num)):
   res=res + int(num[i])
print("sum of num :",res)
if int(num)%res==0:
   print(" Yes it is a Harshad number")
else:
   print("No")