n=int(input())
l=list(map(int,input().split()))
q=int(input())
T=[]
for i in range(q):
    temp=list(map(int,input().split()))
    T.append((tuple(temp[1:]),i+1))
res=[]
for t,i in T:
    k=len(t)
    #flag=0
    for j in range(n-k+1):
        if tuple(l[j:j+k])==t:
            res.append((j,i))
            #flag=1
            break
res.sort()
for i in range(q-1):
    print(res[i][1],end=' ')
print(res[-1][1])
