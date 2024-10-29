import sys
input = sys.stdin.readline
for _ in range(3):
    n = int(input())
    result = 0
    for i in range(n):
        tmp = int(input())
        result += tmp
    if result > 0:
        print("+")
    elif result == 0:
        print("0")
    else:
        print("-")
