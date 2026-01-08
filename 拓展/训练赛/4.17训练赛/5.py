l=list(map(int,input().split()))

n=int(input())
s=[set([x]) for x in l]

for i in range(n):
    for j in range(6):
        for z in range(6,0,-1):
            if z not in s[j]:
                l[j]=z
                s[j].add(z)
                break
    

print(*l)
