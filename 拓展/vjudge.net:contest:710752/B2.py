import re
n,k=map(int,input().split())

s=input()

lo=[m.start() for m in re.finditer(r'o',s)]
l2=[m.start() for m in re.finditer(r'\.',s)]

ans=['']*n
for i in lo:
    ans[i]='o'
    if i>0:
        ans[i-1]='.'
    if i<n-1:
        ans[i+1]='.'

for i in l2:
    ans[i]='.'

x=[]
for i in range(n):
    if not ans[i]:
        x.append(i)
        


if k-len(lo)==len(x):
    for j in x:
        ans[j]='o'
else:
    for j in x:
        ans[j]='?'

print(''.join(ans))
