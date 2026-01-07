a,b,c=map(int,input().split())
d=[]
e=[]
for f in range(a):
    g=list(map(int,input().split()))
    d.append(g)
    for h in range(b):
        if g[h]<0:
            e.append((f,h))
i=[]
for f in range(a):
    for h in range(b):
        if d[f][h]!=0:
            continue
        j=0
        for k in range(h-1,-1,-1):
            if d[f][k]<0:
                j+=1
            elif d[f][k]>c:
                break
        for k in range(h+1,b):
            if d[f][k]<0:
                j+=1
            elif d[f][k]>c:
                break
        for k in range(f-1,-1,-1):
            if d[k][h]<0:
                j+=1
            elif d[k][h]>c:
                break
        for k in range(f+1,a):
            if d[k][h]<0:
                j+=1
            elif d[k][h]>c:
                break
        if j>=3:
            i.append((-j,f,h))
i.sort()
print(len(i))
if i:
    print(i[0][1],i[0][2])
