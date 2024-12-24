l=[]
for _ in range(3):
    l.append(int(input()))
l.remove(min(l))
l.remove(max(l))
print(l[0])

