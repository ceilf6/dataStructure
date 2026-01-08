import sys
sys.setrecursionlimit(5000)

N,D=map(int,input().split())

A=list(map(int,input().split()))

gn=max(A)
'''
vis=[-1]*gn
ans=0
def dfs(step,chosen,num):
    global ans
    
    if chosen==num:
        #print(vis)
        ans+=1
        return

    if step==N:
        return

    if vis[A[step]-1]!=-2:#
        if vis[A[step]-1]!=-1:#已有一个
            if (step-vis[A[step]-1])>D:#超过D
                dfs(step+1,chosen,num)
            else:#已有一个且能选择选还是不选
                a0=vis[A[step]-1]
                
                dfs(step+1,chosen,num)
                vis[A[step]-1]=-2
                dfs(step+1,chosen+1,num)

                vis[A[step]-1]=a0#记得复原，下面还可能会用
        else:#没有一个
            vis[A[step]-1]=step
            dfs(step+1,chosen+1,num)
            vis[A[step]-1]=-1
            dfs(step+1,chosen,num)
        
    else:#已有两个
        dfs(step+1,chosen,num)
'''
vis={}
ans=0
def dfs(step,chosen,num):
    global ans
    
    if chosen==num:
        #print(vis)
        ans=(ans+1)%(10**9+7)
        return

    if step==N:
        return

    if A[step] in vis:#一个或两个
        if vis[A[step]]==-2:#两个
            dfs(step+1,chosen,num)
        else:
            if (step-vis[A[step]])>D:#超过D
                dfs(step+1,chosen,num)
            else:#已有一个且能选择选还是不选
                a0=vis[A[step]]
                
                dfs(step+1,chosen,num)
                vis[A[step]]=-2
                dfs(step+1,chosen+1,num)

                vis[A[step]]=a0
    else:#0个
        vis[A[step]]=step
        dfs(step+1,chosen+1,num)
        del vis[A[step]]
        dfs(step+1,chosen,num)
        
for i in range(2,N+1):
    dfs(0,0,i)

'''
viss={1:2}
del viss[1]
print(1 in viss)
'''
print((ans+N)%(10**9+7))
