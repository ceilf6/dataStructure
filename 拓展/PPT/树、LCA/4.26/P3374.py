n,m=map(int,input().split())

l=list(map(int,input().split()))

def lowbit(x):
    return x & -x

def getsum(x):  # a[1]..a[x]的和
    ans = 0
    while x > 0:
        ans = ans + c[x]
        x = x - lowbit(x)
    return ans

def add(x, k):
    while x <= n:  # 不能越界
        c[x] = c[x] + k
        x = x + lowbit(x)

#初始化
c=[0]*(n+1) #注意add中可以观察得树状数组一般下标从1开始
for i in range(1,n+1):
    add(i,l[i-1])

for i in range(m):
    f,p,q=map(int,input().split())
    #不要用a，b，c。会和数组名重复
    if f==1:
        add(p,q)
    else:
        print(getsum(q)-getsum(p-1))#题目要求左闭右闭，那么就要b-1


        
