#问题：有多少个子序列：用一个个数组存储

n=int(input())

h=list(map(int,input().split()))

l=[]

for i in h:
    flag=0
    for j in range(len(l)):
        if l[j][0]-1==i:
            l[j]=[i]+l[j]
            flag=1
            break
    if not flag:
        l.append([i])

#print(l)
print(len(l))
