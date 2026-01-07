def KMP(f,g):
    n=len(g)
    m=len(f)
    
    j=0
    p=[0]*m
    for i in range(1,m):#构建前缀数组
        while j>0 and f[i]!=f[j]:
            j=p[j-1]
        if f[i]==f[j]:
            j+=1
            p[i]=j

    j=0
    for i in range(n):
        while j>0 and g[i]!=f[j]:
            j=p[j-1]
        if g[i]==f[j]:
            j+=1
        if j==m:
            return i-m+1
    return -1

n=int(input())

l=list(map(int,input().split()))

q=int(input())
matchh=[]
for i in range(q):
    temp=list(map(int,input().split()))
    k=temp[0]
    now=temp[1:]
    pos=KMP(now,l)
    matchh.append((pos,i+1))
    
matchh.sort()
print(' '.join(str(x[1]) for x in matchh))
