l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
S=0
T=0
for i in l1:
    S+=i
for i in l2:
    T+=i
if S>=T:
    print(S)
else:
    print(T)
