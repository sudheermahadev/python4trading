# INTREST RATE CALCULATION ** COMPOUND ** CHAKRA Baddi
print("P - Principle")
print("T - term in years")
print("N - No of times the intrest is compounded per year")
print("R - intrest rate in percentage")


import math

P = 1000 
T = 2 
N = 2 
R = 10
        

print("P = 1000, T = 2, N = 2, R = 10")
        
example1 = int(P * ( (1 + (R / 100) / N )**( N * T)))
print('IntrestCalex1')        
print(example1)


import math

P = 100
T = 1
N = 1
R =10
print("P = 100, T = 1, N = 1, R = 10")

example2 =  ( P * ( ( 1  + ( R / 100) / N )**(N * T)))
print("IntrestCalex2")  
print(example2)
print(int(example2))

print("######################################")
print("###########SWAPPING#################")

print('Example 1')
a=13
b=9
print(a,b)
print('After Swapping')
a,b=b,a
print(a,b)

print('Example 2')
c=15
d=8
print(c,d)
print('After Swapping')
c,d=d,c
print(c,d)