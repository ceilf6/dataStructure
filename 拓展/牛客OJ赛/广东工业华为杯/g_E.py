T=int(input())

a=['G','D','U','T']


def dfs(step,chose,vis,nums):
    global flag

    if flag:
        return
    
    if step==len(vis):
        summ=0
        for i in nums:
            for j in range(len(vis)):
                i=i.replace(vis[j],str(chose[vis[j]]))
            
            summ+=int(i)
        if summ==int(musum):
            print('YES')
            for m in nums:
                for n in m:
                    print(chose[n],end=' ')
            print()
            flag=1
        return
    
    for i in range(0,10):
        nchose=chose.copy()
        nchose[vis[step]]=i
        dfs(step+1,nchose,vis,nums)
            



for i in range(T):
    s,musum=input().split()

    nums=[]
    l=0
    vis=[]

    for j in range(len(s)):
        if s[j]=='+':
            nums.append(s[l:j])
            l=j+1
        else:
            if s[j] not in vis:
                vis.append(s[j])
                
    nums.append(s[l:])

    flag=0
    dfs(0,{},vis,nums)

    if flag==0:
        print('NO')
            
