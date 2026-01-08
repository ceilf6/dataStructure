n,m,ll=map(int,input().split())

s=[[]]
for _ in range(n):
    s.append(list(input()))

kua=[]
l=list(map(int,input().split()))

for x in l:
    if x==-1:
        break
    if x==0:
        if kua:
            print(kua.pop(), end='')
    else:
        if s[x]:
            if len(kua)==ll:
                print(kua.pop(), end='')
            kua.append(s[x].pop(0))
