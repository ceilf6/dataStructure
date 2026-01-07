a,b=map(int,input().split())

mapp=[]
for _ in range(a):
    mapp.append(list(map(int,input().split())))

maxx=mapp[1][1]+mapp[0][1]+mapp[1][0]+mapp[2][1]+mapp[1][2]

#print(mapp)

for i in range(1,a-1):
    for j in range(1,b-1):
        now = mapp[i][j] + mapp[i-1][j]+mapp[i][j-1]+mapp[i+1][j]+mapp[i][j+1]
        if now>maxx:
            maxx = now

print(maxx)
