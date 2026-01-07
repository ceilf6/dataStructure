n=int(input())

l=list(map(int,input().split()))

ans=[[0]*n for i in range(n)]#for _ in range(n-1)]

#for z in range(n-1):
for i in range(n):
    for j in range(n):
        ans[i][j]=l[(i+j)%(n)]

for i in ans:
    #for j in i:
    print(''.join(map(str,i)))
