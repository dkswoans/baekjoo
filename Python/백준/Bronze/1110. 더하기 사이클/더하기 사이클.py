n=int(input())
nn=n
result=0
while True:
    n11=n//10 #2
    n1=n%10 #6
    n2=n1+n11 #8
    n3=n1*10+n2%10 #14
    if n3==nn:
        break
    n=n3
    result+=1
print(result+1)