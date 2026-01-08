n,m=map(int,input().split())

s=[]
for i in range(n):
    s.append(list(map(int,input().split()))[1:])
'''
for i in range(n):
    s[i].sort()
    s[i]=''.join(map(str,s[i]))
print(s)
'''
q=int(input())

for i in range(q):
    a,b=map(int,input().split())
    '''
    if a>b:
        k=b+a
    else:
        k=a+b
    '''
    cnt=0
    for j in range(n):
        if a in s[j] and b in s[j]:
            cnt+=1
    print(cnt)
