s=input()

'''
l=0
i=0
flag=0
ans=''
while i<=len(s)-2:
    if flag and s[i]!=s[i+1]:
        
        
    if not flag and s[i]==s[i+1]:
        flag=1
        l=2
        i+=1
    i+=1
'''
from collections import Counter

d=Counter(s)

ans=''
for i in d:
    ans=ans+i+str(d[i])

if len(ans)<len(s):
    print(ans)
else:
    print('NO')
