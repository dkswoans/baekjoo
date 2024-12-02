a,ab=map(int,input().split())
l1=set(map(int,input().split()))
l2=set(map(int,input().split()))
res1=l1-l2
print(len(res1))
res1=list(res1)
res1.sort()
print(*res1)
