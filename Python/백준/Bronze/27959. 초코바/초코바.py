print("Yes" if (lambda x, y: x*100 >= y)(*map(int, input().split())) else "No")
