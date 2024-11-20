a=list(input())
for i in range(len(a)):
    if 'A'<=a[i]<='Z':
        print(chr(ord(a[i])+32),end='')
    if 'a'<=a[i]<='z':
        print(chr(ord(a[i])-32),end='')