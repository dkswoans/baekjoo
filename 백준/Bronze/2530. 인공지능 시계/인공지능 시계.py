a,b,c=map(int,input().split())
t=int(input())
for _ in range(t):
    c+=1
    if c==60:
        b+=1
        c=0
    if b==60:
        a+=1
        b=0
    if a==24:
        a=0
print(a,b,c)