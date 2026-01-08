n=int(input())
l=list(map(int,input().split()))
q=int(input())
T=[]
lens=set()
for i in range(q):
    temp=list(map(int,input().split()))
    T.append((tuple(temp[1:]),i+1))
    lens.add(len(temp)-1)
d={}
for k in lens:
    for i in range(n-k+1):
        key=tuple(l[i:i+k])
        if key not in d:
            d[key]=i
res=[]
for t,i in T:
    pos=d[t]
    res.append((pos,i))
res.sort()
for i in range(q-1):
    print(res[i][1],end=' ')
print(res[-1][1])
