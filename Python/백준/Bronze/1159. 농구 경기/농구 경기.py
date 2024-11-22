n=int(input())
l=[]
for _ in range(n):
    l.append(list(input()))

lk=[0 for _ in range(26)]

for i in range(n):
    lk[ord(l[i][0])-ord('a')]+=1
# for i in range(26):
#     print(chr(i+65),":",lk[i])
flag=False
for i in range(26):
    if lk[i]>=5:
        print(chr(i+97),end='')
        flag=True
if flag==False:
        print("PREDAJA")
        
    
    
    
    