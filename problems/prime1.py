# num=int(input("enter"))
# c=0
# for i in range(2,num+1):
#     if(num%i==0):
#         c=c+1
#     if(c==1):
#      print(num)  
#      c=0
# c = 0
# n=int(input("enter a number"))
# for i in range(2, n + 1):
#     if n % i == 0:
#         c += 1
# if c == 1:
#     print("its prime")
# else:
#     print("it is not prime")
#     for j in range(n,26):
#         print(j)

from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
h = 0.2
pensize(3)
for i in range(200):
    color(hsv_to_rgb(h,1,1,))
    h +=0.005
    left(100)
    up()
    forward(i)
    down()
    circle(i,-90)
    right(200)
    up()
    forward(i)
    left(120)
    forward(i)
    down()
done()