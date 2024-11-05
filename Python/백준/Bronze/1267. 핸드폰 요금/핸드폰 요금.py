y=0
m=0
a=int(input())
l=list(map(int,input().split()))
for i in l:
    y+=(i//30+1)*10
    m+=(i//60+1)*15

if y<m:
    print("Y",y)
elif y>m:
    print("M",m)
else:
    print("Y M",y)
    