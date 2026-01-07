n=int(input())

t=[[0]*6 for i in range(n)]

for i in range(n):
    t[i]=list(map(int,input().split()))

for i in range(n):
    a=t[i][0]*t[i][3]
    b=t[i][1]*t[i][4]
    c=t[i][2]*t[i][5]
    T=max(a,b,c)
    print(T)
