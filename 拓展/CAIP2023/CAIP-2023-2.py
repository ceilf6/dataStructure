n,m=map(int,input().split())

d={}
for i in range(n):
    a,b=input().split()
    d[a]=b

#s=[]
from itertools import permutations
for i in range(m):
    s=input()
    l0=len(s)
    lans=0

    '''
    for j in d:
        if j in s:
    '''

    for j in d:
        while j in s:#防止多次len
            s=s.replace(j,d[j],1)
            lans+=len(j)


    '''
    for j in range(1,len(s2)+1):
       lis=[''.join(p) for p in permutations(s2,j)]
       lans=lans+lis    #不能用append
    '''
    if lans==l0:
        print(s)
    else:
        print('D')

