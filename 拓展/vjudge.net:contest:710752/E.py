n=int(input())
m=int(input())

s=[[0]*n for i in range(m)]
for i in range(m):
    temp=list(input().split())
    l=int(temp[0])
    r=int(temp[1])
    s[i][l-1:r]=[0]*(r-l+1) if temp[2]=='odd' else [1]*(r-l+1) 


flag=int(''.join(map(str,s[0])),2)
for i in range(2,m):
    now=int(''.join(map(str,s[0])),2)
    flag^=now
    if flag!=0:
        print(i)
        break
