n=int(input())

a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())


I=[[] for i in range(10)]

for i in range(n):
    I[a[i]].append(b[i])

#print(I)
summ=0
for i in range(10):
    if len(I[i])>n//10:
        I[i].sort()
        summ+=sum(I[i][:len(I[i])-n//10])

print(summ)
