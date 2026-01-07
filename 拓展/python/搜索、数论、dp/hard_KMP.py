t=int(input())

from collections import Counter

for i in range(t):
    s=input()
    f=input()

    cs=Counter(s)
    cf=Counter(f)

    #print(cf,cs)

    minn=float('inf')

    flag=1
    for i in cf:
        if i not in cs:
            print(0)
            flag=0
            break
        minn=min(minn,cs[i]//cf[i])

    if flag:
        print(minn)
    
