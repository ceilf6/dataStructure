n=int(input())

s=[]
for i in range(n):
    s.append(list(input().split()))

for i in range(n):
    for j in s[i]:
        print(j[0],end='')
    print()
