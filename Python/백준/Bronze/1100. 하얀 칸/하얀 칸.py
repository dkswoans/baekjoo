l=[]
result=0
for i in range(8):
    l.append(list(input()))
for i in range(8):
    for j in range(8):
        if i==j or (i+j)%2==0:
            if l[i][j]=='F':
                result+=1
print(result)