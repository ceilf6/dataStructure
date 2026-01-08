n=int(input())

degree=[0]*(n+1)

for i in range(n-1):
    u,v=map(int,input().split())
    degree[u]+=1
    degree[v]+=1

maxx=max(degree)


flagi=-1
for i in range(1,n+1):
    if degree[i]<maxx:
        flagi=i
        break

if n==2:
    print('1 1')
else:
    if flagi==-1:
        print(maxx,1)
    else:
        print(maxx-1,flagi)
    
