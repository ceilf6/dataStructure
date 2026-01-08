from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

n=int(input())

words=[]
for i in range(n):
    words.append(input())

sta=input()#开头

def pipei(prew,nxtw):
    l=min(len(prew),len(nxtw))
    '''
    if prew[::-1]==nxtw:
        return l-1
    '''
    maxx=0
    for i in range(l):#注意自己和自己
        if prew[-i-1]!=nxtw[i]:
            maxx=i
            break
    else:           #不能包含
        maxx=l-1
    if maxx:
        return len(prew)+len(nxtw)-maxx
    else:           #maxx为0:不能接
        return 0

def dfs(i,ans,nums):
    global maxl
    for j in range(n):
        if pinum[i][j] and nums[words[j]]<2:
            nans=ans+pinum[i][j]
            nums[j]+=1
            dfs(j,nans,nums)
            nums[j]-=1#恢复
            maxl=max(nans,maxl)

pinum=[[0]*n for i in range(n)]
#预处理，不然每次都要算
for i in range(n):
    for j in range(n):
        pinum[i][j]=pipei(words[i],words[j])
print(pinum)    
maxl=0

for i in range(n):
    if words[i][0]==sta:   #开头
        nums=defaultdict(int)#记录使用次数
        nums[words[i]]+=1
        dfs(i,0,nums)

print(maxl)
