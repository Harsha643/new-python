num=input("enter the number")
c=0
sum=0
for i in range(0,len(num)):
    for j in range(2,int(num[i])+1):
            # print(j,type(j))
            if(int(num[i])%j== 0):
                c+=1
    if(c==1):
        sum+=int(num[i])
        c=0
print(sum)