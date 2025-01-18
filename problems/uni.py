# 2)  Problem Statement: Given N integers separated with space, print the count of unique numbers in the given N integers
# Input:
#  1 11 2 20 2 3 3 
# Output:
# 3


c=0
num=input().split()
for i in num:
    for j in num:
        # print(i,j)
        if(i==j):
            c+=1
print(c)
                