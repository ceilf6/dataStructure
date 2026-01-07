n,x=map(int,input().split())

s=input()

ss=[]
for i in s:
    ss.append(i)

ss.sort()


ans=[]
ans.append(ss[0])
del ss[0]
mu=x-1
while mu>0 and ss:
    if ss[0]==ans[-1]:
        mu-=1
        del ss[0]
    else:
        ans.append(ss[0])
        del ss[0]
        
while mu>0:
    del ans[-1]
    mu-=1

while ss:
    ans.append(ss[0])
    del ss[0]

ans=''.join(ans)
print(ans)
