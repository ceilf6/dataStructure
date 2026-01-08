n,c=map(int,input().split())
name=['']*n

num=[[i,0] for i in range(n)]

for i in range(n):
    name[i],nn=input().split()
    num[i][1]=int(nn)

le=[[i,[],0]for i in range(n)]
'''
cnt=[[i,0]for i in range(n)]
'''
while any(x[1]>0 for x in num):
    num=sorted(num,key=lambda x:x[1],reverse=1)

    now=num[-1][1]
    if now>=c:
        for i in range(n):
            if le[i][0]==num[i][0]:
                le[i][2]+=1
                break
        num[-1][1]-=c
    else:
        num[-1][1]=0
        le=sorted(le,key=lambda x:x[2])
        flag=0
        for i in range(n):
            if flag:
                break
            for j in range(len(le[i][1])):
                if le[i][1][j]>=now:
                    le[i][1][j]-=now
                    le[i][1].sort()
                    flag=1
                    break
        if not flag:
            le[i][2]+=1
            le[i][1]=c-now
print(le)
