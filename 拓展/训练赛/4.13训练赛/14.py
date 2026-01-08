
n=int(input())
a=list(map(int,input().split()))

def cnt(b):
    cntt=0
    for i in range(n):
        for j in range(i+1,n):
            if b[i]>b[j]:
                cntt+=1
    return cntt

ans=[]
for p in range(n):
    for q in range(p,n):

        b=a[:p]+list(reversed(a[p:q+1]))+a[q+1:]
        ans.append(cnt(b))

res=' '.join(map(str,ans))

print(res)
