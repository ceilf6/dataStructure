n=int(input())

l=list(map(int,input().split()))

def f(t,l,m):
    for i in range(n-m+1):
        if l[i:i+m]==t:
            return i
    return -1

T=[]
q=int(input())
for i in range(q):
    temp=list(map(int,input().split()))
    T.append([temp[0],temp[1:],i+1])

T=sorted(T,key=lambda x:x[0],reverse=-1)#优先大数组？


d=[]
for i in range(q):
    x=f(T[i][1],l,T[i][0])
    d.append([T[i][2],x])

d=sorted(d,key=lambda x:x[1])

for i in range(q-1):
    print(d[i][0],end=' ')
print(d[-1][0])

