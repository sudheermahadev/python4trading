# # try:
# #     number1=int(input('Enter first number '))
# #     number2=int(input('Enter second number '))
# #     print('division of number is: ',number1/number2)

# # except ValueError:
# #     print('please enter only numbers')

# # except ZeroDivisionError:
# #     print('please enter non zero number')

# # """     price=2345.4756

# #     stop=price-0.01*price
# #     print(stop)

# # except Exception as e:
# #     print('something went wrong')
# #     f=open('error.txt','a')
# #     f.write(str(e))
# #     f.close()

# # print('something important') """

# # import random

# # answer=random.randint(10,20)
# # print(answer)


# # import time
# # time.sleep(1)
# # print('hello')
# # time.sleep(2)
# # print ('world')

# # import time
# # import random
# # for i in range(1,10):
# #     a1=random.randint(1,100)
# #     a2=random.randint(101,200)
# #     a3=random.randint(201,300)
# #     time.sleep(1)
# #     print(a1,a2,a3)
# #     time.sleep(1)


# import time
# import random
# import sys
# b=random.randint(100,200)
# c= 150
# while b !=c:
#     print(b)
#     b=random.randint(100,200)
# print(b)
# sys.exit


import os
pwd = os.getcwd()
print(pwd)
os.chdir("/home/sudi/Documents/FinancialTrading/")
newpwd = os.getcwd()
# print(newpwd)
# os.chdir("/root/")
# root = os.getcwd()
# print(root)