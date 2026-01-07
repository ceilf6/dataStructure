T=int(input())

MOD=10**9+7

def exgcd(b,m=MOD):
    if m==0:
        return b,1,0
    gcd,x,y=exgcd(m,b%m)
    return gcd,y,x-(b//m)*y

def mov_inv(b,m=MOD):
    gcd,x,y=exgcd(b,m)
    return x%m

for _ in range(T):
    n,m=map(int,input().split())

    pre=[0]
    for i in range(m):

        l,r=map(int,input().split())
        if r==n:
            #pre.append((pre[-1]+(r-l-1/2))%MOD)
            b_1=mov_inv(2,MOD)
            ans=pre[-1]+((r-l)*2-1)*b_1%MOD
            pre.append(ans)
        else:
            pre.append((pre[-1]+(r-l))%MOD)

        print(pre[-1])

'''
#模拟但是T了
for _ in range(T):
    n,m= map(int, input().split())
    skill=[]
    for _ in range(m):
        l,r=map(int, input().split())
        skill.append((l, r))

    #pre=[0]
    diff=[0]*(n+2)
    tar=[0]*n
    #cur=0
    #pos=0
    res=[]

    for i in range(m):
        l,r= skill[i]
        diff[l] += 1
        diff[r] -= 1

        #tar=[0]*n
        #tar[0]=diff[0]
        for j in range(1, n):
            tar[j]+=1

        cur=0
        pos=0
        for t in range(n):
            if cur< tar[t]:
                cur+= 1
            elif cur> tar[t]:
                cur-= 1
            pos = (pos + cur) % MOD

        res.append(pos)
        #print((pre[-1]-pre[0]+MOD)%MOD)
    for i in res:
        print((i-res[0]+MOD)%MOD)
'''
