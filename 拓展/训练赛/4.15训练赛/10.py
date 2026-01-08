n=int(input())
from collections import defaultdict

s=defaultdict(list)

for i in range(n):
    inn=input()
    inl=list(inn.split())
    shou=''
    for j in inl:
        shou+=j[0]

    s[shou].append(inn)

k=int(input())

f=[]
for i in range(k):
    f.append(input())

for i in f:
    l=list(i.split())
    shou=''
    for j in l:
        shou+=j[0]

    ll=len(s[shou])
    if ll:
        for j in range(ll-1):
            print(s[shou][j],end='|')
        print(s[shou][-1])
    else:
        print(i)





n=int(input())
from collections import defaultdict

d=defaultdict(list)

for _ in range(n):
    s=input()
    key=''.join([x[0]for x in s.split()])
    d[key].append(s)

m=int(input())
for _ in range(m):
    q=input()
    key=''.join([x[0]for x in q.split()])
    if key in d:
        print('|'.join(sorted(d[key])))
    else:
        print(q)
