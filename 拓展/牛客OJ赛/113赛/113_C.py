q=int(input())

K=[]
'''
maxx=-1
minn=float('inf')
'''
Flag=[-1]*q#可能会输入空，进行判断
for i in range(q):
    inn=list(map(int,input().split()))

    K.append(inn)
    if inn:
        del K[-1][0]
        Flag[i]=1
    #print(K[-1])

flag=1
'''
if maxx!=-1 and minn!=(float('inf')):
    vis=[-1]*(maxx-minn+1)

for i in range(q):

    if flag==0:
        break

    if Flag[i]!=-1:
        if sorted(K[i])!=K[i]:
            flag=0
        #print(sorted(K[i]))
            break

        for j in range(len(K[i])):
            if vis[K[i][j]-minn]!=-1:
                flag=0
                break
            else:
                vis[K[i][j]-minn]=K[i][j]
#print(vis)
if flag:
    if -1 in vis:
        flag=0
'''
vis=[]
for i in range(q):
    if flag==0:
        break

    if Flag[i]!=-1:
        if sorted(K[i])!=K[i]:
            flag=0
        #print(sorted(K[i]))
            break

        for j in range(len(K[i])):
            if K[i][j] in vis:
                flag=0
                break
            else:
                vis.append(K[i][j])

if flag:
    vis.sort()
    for j in range(len(vis)-1):
        if vis[j]!=vis[j+1]-1:
            flag=0
            break

if flag:
    print('YES')
else:
    print('NO')
            
