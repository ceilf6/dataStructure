#1.邻接矩阵
n=int(input()) #点数

INF=float('inf')
ma=[[INF]*n for i in range(n)] #初始化为inf表示没边、无法到达

for i in range(n):
    ma[i][i]=0
#预处理自己到自己为0
'''
然后开始存储输入信息
注意如果是有向图那么一次只能 ma[i][j]= 表示从i到j
    如果是无向的那么 ma[i][j]=ma[j][i]=
'''
#如
for i in range(n):
    a,b,k=map(int,input().split())
    ma[a-1][b-1]=min(ma[a-1][b-1],k)#有向单向图
                #存在重边：取min



#2.边集数组
edge=[]

#每个元素就是（起点，终点，边权）
edge.append((a,b,k))
#如果不存在权值那么直接append((a,b))


#3.邻接表
from collections import defaultdict
d=defaultdict(list)
for a,b,k in inn:#inn是输入内容
    d[a].append((b,k))

for i in d:
    print(d[i])

#4.关联矩阵
# 输入顶点数和边数
n, m = map(int, input("请输入顶点数n和边数m：").split())

# 初始化关联矩阵(行是顶点，列是边)
matrix = [[0] * m for _ in range(n)]
edges = []  # 存储边的信息

print(f"请输入{m}条边的信息（每行输入：起点 终点）：")
# 读入边并构建关联矩阵
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    # 对于有向图：起点标1，终点标-1
    matrix[u][i] = 1   # 出边标记为1
    matrix[v][i] = -1  # 入边标记为-1
    # 如果是无向图，把上面两行改成：
    # matrix[u][i] = matrix[v][i] = 1

# 打印关联矩阵
print("\n关联矩阵：")
for row in matrix:
    print(*row)

"""
示例输入：
4 5
0 1
0 2
1 2
1 3
2 3

输出示例（有向图）：
关联矩阵：
1 1 0 0 0
-1 0 1 1 0
0 -1 -1 0 1
0 0 0 -1 -1
"""