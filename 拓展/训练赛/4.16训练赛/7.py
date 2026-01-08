nv,nan,n=map(int,input().split())


nnv=2

ans=[]

while nnv<=n-2:
    nnan=n-nnv
    if nan%nnan==0 and nv%nnv==0 and nan//nnan>1 and nv//nnv>1:
        ans.append((nnv,nnan))
    nnv+=1


if not ans:
    print("No Solution")

else:
    minn=float('inf')
    for i in range(len(ans)):
        if abs(nv/ans[i][0]-nan/ans[i][1])<minn:
            idx=i
            minn=abs(nv/ans[i][0]-nan/ans[i][1])
            
    print(ans[idx][0],ans[idx][1])
