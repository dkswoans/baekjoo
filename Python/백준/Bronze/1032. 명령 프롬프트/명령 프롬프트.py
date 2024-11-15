n=int(input())
l=[]
for i in range(n):
    tmp=input()
    l.append(tmp)
li=list(l[0])

for i in range(1,n):
    for j in range(len(li)):
        if li[j]!=l[i][j]:
            li[j]='?'
        


print(''.join(li))


