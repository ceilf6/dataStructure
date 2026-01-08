n,m,a,b=map(int,input().split())

mapp=[[] for i in range(n)]

for i in range(n):
    listt=list(map(int,input().split()))
    mapp[i]=listt

summ=0

'''
if a==b:
    for i in range(n-a+1):
        for j in range(m-b+1):
            maxx=mapp[i][j]
            minn=mapp[i][j]

            for dx in range(a):
                for dy in range(b):
                    if mapp[i+dx][j+dy]>maxx:
                        maxx=mapp[i+dx][j+dy]
                    if mapp[i+dx][j+dy]<minn:
                        minn=mapp[i+dx][j+dy]
            summ+=maxx*minn

else:
    for i in range(n-a+1):
        for j in range(m-b+1):
            print(i,j)
            maxx=mapp[i][j]
            minn=mapp[i][j]

            for dx in range(a):
                for dy in range(b):
                    if mapp[i+dx][j+dy]>maxx:
                        maxx=mapp[i+dx][j+dy]
                    if mapp[i+dx][j+dy]<minn:
                        minn=mapp[i+dx][j+dy]
            print(maxx,minn)
            summ+=maxx*minn
    for i in range(n-b+1):
        for j in range(m-a+1):
            print(i,j)
            maxx=mapp[i][j]
            minn=mapp[i][j]

            for dx in range(b):
                for dy in range(a):
                    if mapp[i+dx][j+dy]>maxx:
                        maxx=mapp[i+dx][j+dy]
                    if mapp[i+dx][j+dy]<minn:
                        minn=mapp[i+dx][j+dy]
            print(maxx,minn)
            summ+=maxx*minn
'''
for i in range(n-a+1):
    for j in range(m-b+1):
        maxx=mapp[i][j]
        minn=mapp[i][j]

        for dx in range(a):
            for dy in range(b):
                if mapp[i+dx][j+dy]>maxx:
                    maxx=mapp[i+dx][j+dy]
                if mapp[i+dx][j+dy]<minn:
                    minn=mapp[i+dx][j+dy]
        summ+=maxx*minn
print(summ%998244353)

            
