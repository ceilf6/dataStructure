T=int(input())

n=[0]*T
m=[0]*T
k=[0]*T
q=[0]*T



for i in range(T):
    n[i],m[i],k[i],q[i]=map(int,input().split())

for i in range(T):
    up=m[i]*(k[i]-1)
    su=n[i]%k[i]
    
    flag=0
    
    if q[i]%k[i]==su and q[i]<=up:
        print('YES')

    else:
        print('NO')
