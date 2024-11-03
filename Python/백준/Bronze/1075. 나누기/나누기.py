n=int(input())
f=int(input())
n = (n // 100) * 100
while True:
    if n%f==0:
        print(f"{n % 100:02d}")
        break
    n+=1
