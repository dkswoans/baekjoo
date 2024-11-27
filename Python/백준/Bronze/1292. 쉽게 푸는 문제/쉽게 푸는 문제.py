MAX=100
a,b=map(int,input().split())
l=[i for i in range(1,MAX) for _ in range(i)]
result=0
for i in range(a-1,b):
    result+=l[i]
print(result)