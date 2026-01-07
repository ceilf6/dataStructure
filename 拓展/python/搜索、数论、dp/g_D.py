n=int(input())


p=[[i for i in range(n)]]
p.append(list(map(int,input().split())))

#print(p)
v=list(map(int,input().split()))

Q=int(input())

last=0

p=sorted(p,key=lambda x:x[1])


def pack(L,R,P):
    dp=[0]*(P+1)
    for i in range(n):
        if p[1][i]>P:
            break
        else:
            if L-1<=p[0][i]<=R-1:
                for j in range(P,p[1][i]-1,-1):
                    dp[j]=max(dp[j],dp[j-p[1][i]]+v[i])

    '''
    for i in range(L-1,R):
        if p[i]>P:
            continue
        for j in range(P,p[i]-1,-1):
            dp[j]=max(dp[j],dp[j-p[i]]+v[i])
    '''
    return dp[-1]

for i in range(Q):
    Li,Ri,Pi=map(int,input().split())

    L=((Li+last)%n)+1
    R=((Ri+last)%n)+1
    P=((Pi+last)%10000)+1

    if L>R:
        L,R=R,L

    #print(L,R,P)

    last=pack(L,R,P)
    print(last)
