from collections import *

n,m,x,y=map(int,input().split())

start=(x-1,y-1)

maze=[[-1]*m for _ in range(n)]

di=[(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1)]

def bfs(maze,start):
    vis=set()
    vis.add(start) #每个end的visited不一样
    maze[start[0]][start[1]]=0 #x,y在之前已经减过了
    queue=deque([(start,0)])
    while queue:
        (x,y),steps=queue.popleft()

        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in vis:
                maze[nx][ny]=steps+1
                queue.append(((nx,ny),steps+1))
                vis.add((nx,ny))
bfs(maze,start)

for i in range(n):
    for j in range(m):
        print(f"{maze[i][j]:<3}",end='')
    print()

