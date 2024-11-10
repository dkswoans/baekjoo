n=int(input())
l=[]
for i in range(n):
    l.append(input())
for i in range(n):
    print("%d. %s"%(i+1,l[i]))
