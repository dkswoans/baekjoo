from math import *
n=int(input())
for _ in range(n):
    n,m=map(int,input().split())
    result=factorial(m)//(factorial(n)*factorial(m-n))
    print(result)
