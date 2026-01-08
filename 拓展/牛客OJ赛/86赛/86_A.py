T=int(input())


n=[0]*T
k=[0]*T
a=[[]for i in range(T)]
for i in range(T):
    n[i],k[i]=map(int,input().split())

    a[i]=list(map(int,input().split()))

for i in range(T):
    summ=0
    for j in a[i]:
        if j>0:
            summ+=j
    print(summ)
