import os

def Factorial(num):
    _Cnum = num
    for i in range(1, num):
        num *= (_Cnum - i)
    return num

print(Factorial(5))