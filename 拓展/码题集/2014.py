n=int(input())

h=list(map(int,input().split()))

#目标：清除在某点之后值为该点-1的点
#即清除非连续子序列








#模拟会超时
vis=[1]*n

vis[0]=0
ans=1
i=1
j=h[0]-1
last=-1
lasti=-1
#模拟一支支箭
while sum(vis)!=0:
    if i==n:
        j=last-1
        i=lasti+1
        last=-1
        lasti=-1
    '''
    if i==n:
        ans+=1
        for k in range(n):
            if vis[k]!=0:
                vis[k]=0
                j=h[k]-1
                i=k+1
                break
        #print(i,j)
        continue
    '''
    
    if h[i]==j:
        j-=1
        #i+=1
        vis[i]=0
    else:
        if lasti==-1:
            last=vis[i]
            lasti=i
    i+=1 #先使用再变
    #print(vis)

print(ans)

'''
for i in range(n):
    h[i]+=i

print(max())
'''
'''
#递减
ans=1

for i in range(1,n):
    if h[i]!=h[i-1]-1:
        ans+=1

print(ans)
'''
