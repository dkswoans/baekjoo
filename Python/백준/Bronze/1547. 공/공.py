n=int(input())
res=1
for _ in range(n):
    a,b=map(int,input().split())
    if a==res:
        res=b
    elif b==res:
        res=a
print(res)
        