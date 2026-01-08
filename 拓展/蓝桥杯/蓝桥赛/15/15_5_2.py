n,m=map(int,input().split())

a=[]
for i in range(n):
    a.append(input())

def lian(a1,a2):
    A1=a1+a1
    A2=a2+a2

    i=0
    j=0

    Lenn=[0]
    for i in range(len(a1)):
        for j in range(len(a2)):
            if A1[i]==A2[j]:
                l1=i
                l2=j
                summ=1
                
                while l1+summ<len(A1) and l2+summ<len(A2):
                    if A1[l1+summ]==A2[l2+summ]:
                        summ+=1
                    else:
                        break
                r1=i+summ-1
                r2=j+summ-1
                

                if r1>len(a1)-1:
                    len1=len(a1)-l1
                else:
                    len1=r1-l1+1
                if r2>len(a2)-1:
                    len2=len(a2)-l2
                else:
                    len2=r2-l2+1

                Lenn.append(max(len1,len2))#Lenn存可能公共字符串长度

    Len.append(max(Lenn))#Len存公共字符串长度

#全排序：暴力枚举
    
k=list(range(n))
c=[]
vis=[0]*n
b=[0]*n
def dfs(step):
    if step==n:
        B=[]
        for i in range(n):
            B.append(b[i])
        c.append(B)
        
        return
    
    for i in range(n):
        if vis[i]!=1:
            b[step]=k[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0

dfs(0)

MaxLen=0
for ci in c:
    Len=[]
    for i in range(n-1):
        lian(a[ci[i]],a[ci[i+1]])
    lian(a[ci[0]],a[ci[-1]])

    Len.sort(reverse=1)
    summ=0
    #print(Len)
    
    for i in range(n-1):
        summ+=Len[i]
    MaxLen=max(MaxLen,summ)

print(MaxLen)

            
        



