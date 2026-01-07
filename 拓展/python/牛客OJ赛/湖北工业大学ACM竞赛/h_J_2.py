n=int(input())

T=[[]for i in range(n)]

for i in range(n):
    inn=list(map(int,input().split()))
    T[i]=[sum(inn[:-1]),inn[-1]]

T=sorted(T,key=lambda x:x[1])


