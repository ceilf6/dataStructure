t=int(input())

import re

for i in range(t):
    p=input()
    s=input()

    lis_p=re.findall(r'L+|R+',p)
    lis_s=re.findall(r'L+|R+',s)
    #print(lis_p,lis_s)
    flag=1
    
    if len(lis_p)!=len(lis_s):
        flag=0
    else:
        for i in range(len(lis_p)):
            lp=len(lis_p[i])
            ls=len(lis_s[i])
            #print(lp,ls)
            if lis_p[i][0]!=lis_s[i][0]\
               or ls<lp or ls>2*lp:
                flag=0
                break
    if not flag:
        print('NO')
    else:
        print('YES')
