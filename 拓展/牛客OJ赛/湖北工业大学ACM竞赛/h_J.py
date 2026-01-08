summ=0

n=int(input())

T=[[]for i in range(n)]

for i in range(n):
    T[i]=list(map(int,input().split()))

T=sorted(T,key=lambda x:x[3])

k=0
for i in range(n):
    if sum(T[i][:3])>(T[i][-1]-summ):
        continue
    else:
        summ+=sum(T[i][:3])
        k+=1

print(k)
