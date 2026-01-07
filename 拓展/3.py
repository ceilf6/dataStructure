#动态:当组成这个字符串所索引的 $ 对象变的时候也会随着变

T=int(input())
d={}

import re

for _ in range(T):
    temp=list(input().split())
    if temp[0]=='1':
        st=''
        for i in range(2,len(temp)):
            if temp[i][0]!='$':
                st+=temp[i]
            else:
                if temp[i][1:] in d:
                    st+=d[temp[i][1:]]
        #st=''.join(s for s in temp[2:])
        d[temp[1]]=st

    elif temp[0]=='2':
        st=''
        for i in range(2,len(temp)):
            if temp[i][0]=='$':
                st+=temp[i]+'^'
            else:
                st+=temp[i]
        d[temp[1]]=st

    else:
        #print(d)
        if temp[1] in d:
            l=d[temp[1]]
            '''
            for key in d:
                l=l.replace('$'+key+'^',d[key])#太久没用，都忘记replace要赋值了
            #print(l)
            '''
            
            pattern=r"\$.*?\^"
            matches=re.findall(pattern,l)
            for key in matches:
                l=l.replace(key,d[key[1:len(key)-1]])
            
            print(len(l))
        
        else:
            print(0)
'''
l='$a^'
l.replace('$'+'a'+'^',d['a'])
print(l)
print('$'+'a'+'^')
'''
