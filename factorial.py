import math
import sys
import string
import time

Factorialnum = int(input())
t = Factorialnum

for i in range(Factorialnum):
    Factorialnum = Factorialnum * Factorialnum - 1
    print(Factorialnum)
