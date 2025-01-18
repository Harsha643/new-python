num =int(input("enter a number "))
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True 
    return False 

if(isPrime(num)):
    print("it is prime ")
else:
    lp=num-1
    rp=num+1
    # print(lp,rp)
    left,right=True,True
    while left or right:
        if( isPrime(lp) and left):
            x=lp
            left =False
        lp-=1
        if( isPrime(rp) and right):
            y=rp
            right=False
        rp+=1
    print(x,y)