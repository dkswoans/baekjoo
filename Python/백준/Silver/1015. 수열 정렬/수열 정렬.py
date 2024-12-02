n=int(input()) #4
l=list(map(int,input().split()))
l1=l.copy() #2 1 3 1
l.sort() # 1 1 2 3
d={}
for i in range(n):
    if l[i] not in d:
        d[l[i]]=[]
    d[l[i]].append(i)
for i in l1:
    print(d[i].pop(0),end=' ')
    
