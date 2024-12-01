a1,b1=map(int,input().split())
a=min(a1,b1)-1
b=max(a1,b1)-1
print(b//4-a//4+abs(b%4-a%4))

