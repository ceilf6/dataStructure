#from collections import deque

hezi=[]

ans=[]

n,m,k=map(int,input().split())
a=map(int,input().split())
'''
while
    now=[]
    
    if hezi:
        new=hezi.pop()
    else:
        new=a[j]
        
    now.append(new)

    while hezi[-1]>now[-1]:
        if len(hezi)==m:
            ans.append(now)
            now=[]
        new=a[j]
        if new<=now[-1]:
            now.append(new)
            break
        else:
            hezi.append(new)
'''
now=[]
j=0
def cz(a):
    global ans
    n=len(a)
    while j<=n-1:
        if not now:
            if not hezi:
                now.append(a[j])
            else:
                now.append(hezi.pop())
                
        while hezi:
            if hezi[-1]<=now[-1]:
                now.append(hezi.pop())
            else:
                break
        if a[j]<=now[-1]:
            now.append(a[j])
        else:
            hezi.append(a[j])
            if len(hezi)==m:
                ans.append(now)
                now=[]
    return hezi

while a:
    a=cz(a)

for i in ans:
    print(*i)







            
