a=int(input())
b=int(input())
c=int(input())
res=str(a*b*c)
l=[0]*10
for i in range(len(res)):
    l[int(res[i])]+=1
for i in l:
    print(i)
