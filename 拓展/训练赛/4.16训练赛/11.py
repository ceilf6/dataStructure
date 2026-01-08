
k=int(input())

los=[]
for i in range(k):
    los.append(list(map(int,input().split())))
w=int(input())

from collections import deque

tot=2**(k+1)-1
t=[0]*tot
los=[deque(l) for l in los]

def dfs(x,lev):
    if lev==k:
        return 1
    if not los[lev]:
        return 0
    w=t[x]
    lo=los[lev].popleft()
    l=x*2+1
    r=x*2+2
    for wl in[1,0]:
        if wl:
            t[l]=w
            t[r]=lo
        else:
            t[l]=lo
            t[r]=w
        if t[l]<t[r]:
            continue
        if dfs(l,lev+1) and dfs(r,lev+1):
            return 1
    los[lev].appendleft(lo)
    return 0
t[0]=w
if dfs(0,0):
    leaves=t[(2**k)-1:]
    print(' '.join(map(str,leaves)))
else:
    print('No Solution')
