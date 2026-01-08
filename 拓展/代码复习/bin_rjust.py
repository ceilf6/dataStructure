d=int(input())

b=bin(d)

s=b[2:].rjust(20,'0')

print(s)
