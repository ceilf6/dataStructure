import math

m, n = input().split()
m = int(m)

def an():
    if n == '+':
        print(m - 1, 1)
        return
    elif n == '-':
        print(m + 1, 1)
        return
    elif n == '*':
        print(m,1)
        return

an()
