s = input()
t = input()

l1 = len(s)
l2 = len(t)

T = int(input())

pre = []

for i in range(l1):
    for j in range(l2):
        flag = 0
        if t[j]>s[i]:
            flag = 1
            break
    if(flag):
        pre.append(j)
    else:
        pre.append(-1)

'''
cache = []

#@cache
def xunwen(a,b):
    if(pre[a]==-1): return l2-b+1
    if(xunwen())
    for i in range(a):
        ans = max(ans,xunwen(a+1,b))
    return ans
'''

for _ in range(T):
    i,j = map(int,input().split())

    i-=1
    j-=1
    ans = l2-j
    for a in range(i,l1):
        
        if pre[a] and pre[a]>=j:
            ans = max(ans,l2-pre[a]+l1-a)
    print(ans)
