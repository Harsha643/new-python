# t1=(3,2,4,5,6,"true",2,2)
# print(t1)
# t2=(tuple([1,2,3,4,5]))
# print(t2)
# t3=6,
# print(t3)
# t4=()
# print(t4)
# print(t1.count(2))
# print(t1.index(2))
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
s1=input()
s2=input()
c=0
# for i in range(0,len(num1)):
#     if num1[i] == num2[0]:
#         if(num2 == num1[i:i+len(num2)]):
#             count+=1
# print(c) 
for i in range(0,len(s1)):
    if s1[i]==s2[0]:
        if s2==s1[i:i+len(s2)] :
            c+=1
        print(c)