l=[]
a=input().strip()
n=int(input().strip())
for _ in range(n):
    l.append(input().strip())
max_=-1
result=""
l.sort()
for i in range(n):
    tmp=a+l[i]
    res = (
        (tmp.count('L') + tmp.count('O'))
        * (tmp.count('L') + tmp.count('V'))
        * (tmp.count('L') + tmp.count('E'))
        * (tmp.count('O') + tmp.count('V'))
        * (tmp.count('O') + tmp.count('E'))
        * (tmp.count('V') + tmp.count('E'))
    ) % 100

    if max_<res:
        max_=res
        result=l[i]
print(result)