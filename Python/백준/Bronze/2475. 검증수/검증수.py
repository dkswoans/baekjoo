l=list(map(int,input().split()))
result=0
for i in l:
    result+=i*i
print(result%10)