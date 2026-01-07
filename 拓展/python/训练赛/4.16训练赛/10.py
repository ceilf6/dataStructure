n,c=map(int,input().split())

name=['']*n
num=[0]*n
for i in range(n):
    name[i],num[i]=input().split()
    num[i]=int(num[i])
'''
inlc=[[i for i in range(n)]]+num+[[0]*n for i in range(2)]
'''
inlc=[[i,num[i],0,0]for i in range(n)]

while any(x[1]> 0 for x in inlc):
    inlc=sorted(inlc,key=lambda x:x[1])
    now=inlc[0][1]
    if now>=c:
        inlc[0][3]+=1
        inlc[0][1]-=c
    else:
        flag=0
        inlc=sorted(inlc,key=lambda x:x[3])
        for i in range(n):
            if inlc[i][2]>now:
                inlc[i][3]+=1
                inlc[i][2]-=now
                inlc[i][1]=0
                flag=1
                break
        if not flag:
            inlc[i][3]+=1
            inlc[i][2]=c-now
            inlc[i][1]=0
        
print(inlc)

'''
for i in range(n):
    iln[i]=sh[i][1]//c
    leftnow=sh[i][1]%c
    flag=0
    for j in range(len(left)):
        if left[j]>=leftnow:
            cnt[j]+=1
            flag=1
            left[j]-=leftnow
    if not flag:
        cnt[i]+=1
        left[i]=c-leftnow
    #left.sort()
    print(left)
print(cnt)
'''
        
