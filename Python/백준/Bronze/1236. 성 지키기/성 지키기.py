a,b=map(int,input().split())
flag=[False]*a
l=[]
result1=0
result2=0
for _ in range(a):
    tmp=list(input())
    l.append(tmp)
for i in range(a):
    if 'X' not in l[i]:
        result1+=1
for i in range(b):
    c=False
    for j in range(a):
        if l[j][i]=='X':
            c=True
            break
    if not c:
        result2+=1
        
print(max(result1,result2))
            
# a,b=map(int,input().split())
# l=[]
# result=0
# for _ in range(a):
#     tmp=list(input())
#     l.append(tmp)
# for i in l:
#     if 'X' not in i:
#         result+=1
# print(result)    