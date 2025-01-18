# num =int(input("enter a number :"))
# count=int(input("enter count no:"))
# def isPrime(n):
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if n%i==0:
#                 return False
#         return True 
#     return False 

# if(isPrime(num)):
#     print("it is prime ")
# else:
#     lp=num-1
#     rp=num+1
#     rc,lc=0,0
#     # print(lp,rp)
#     # left,right=True,True
#     while rc!=count or lc!=count:
#         if( isPrime(lp) and lc!=count):
#             x=lp
#             lc+=1
            # left =False
#         if lc!=count:
#             lp-=1
#         if( isPrime(rp) and rc!=count):
#             y=rp
#             rc+=1
#             right=False
#         if rc!=count:
#             rp+=1
#     if x<2:
#         print(x,y)
#     else:
#         print("your entered invalid number")

# num = int(input("Enter a number: "))
# count = int(input("Enter count number: "))

# def isPrime(n):
#     """Check if a number is prime."""
#     if n > 1:
#         for i in range(2, (n // 2) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     return False

# if isPrime(num):
#     print("It is prime.")
# else:
#     lp = num - 1
#     rp = num + 1
#     rc, lc = 0, 0
#     # left_primes = []
#     # right_primes = []

#     while (rc < count or lc < count) and lp >= 2:
#         # Check for left primes
#         if lc < count and isPrime(lp):
#             # left_primes.append(lp)
#             x=lp
#             lc += 1
#         lp -= 1

#         # Check for right primes
#         if rc < count and isPrime(rp):
#             # right_primes.append(rp)
#             y=rp
#             rc += 1
#         rp += 1

#     # Handle invalid cases where left side becomes less than 2
#     if lp < 2 and lc < count:
#         print("Invalid number.")
#     else:
#         # print(f"Left primes: {left_primes}")
#         # print(f"Right primes: {right_primes}")
#         print(x,y)



num = int(input("Enter a number: "))
count = int(input("Enter count number: "))

def isPrime(n):
    """Check if a number is prime."""
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True
    return False

if isPrime(num):
    print("It is prime.")
else:
    lp = num - 1
    rp = num + 1
    rc, lc = 0, 0
   

    while (rc!=count or lc!=count) and lp >= 2:
       
        if lc!=count and isPrime(lp):
         
            x=lp
            lc += 1
            
        if lc!=count:
            lp-=1

        if rc != count and isPrime(rp):
        
            y=rp
            rc += 1
        if rc!=count:
            rp+=1

    if lp < 2 and lc!=count:
        print("Invalid number.")
    else:
       
        print(x,y)
