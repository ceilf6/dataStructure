n=int(input())

d=[[0]*3 for i in range(2)]
for i in range(n):
    a,b=map(int,input().split())
    d[a][b-1]+=1

for i in d:
    print(*i)

if d[0]>d[1]:
    print('The first win!')
else:
    print('The second win!')