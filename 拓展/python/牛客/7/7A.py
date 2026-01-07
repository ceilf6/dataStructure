n,x,y,z,T=map(int,input().split())

N=[]
for i in range(n):
    N.append(list(map(int,input().split())))


Tmax=T+z
maxx=x+y
for i in range(n):
    if N[i][2]<=Tmax:
        maxx=max(maxx,N[i][0]+N[i][1])

print(maxx)
'''
for i in range(1,n+1):
    for j in range(T+1):
        if
        '''
