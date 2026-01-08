# 1. 邻接矩阵存储（适用于稠密图）
def adjacency_matrix_example():
    n = 4  # 顶点数
    # 初始化n*n的矩阵，所有元素为0
    graph = [[0] * n for _ in range(n)]
    
    # 添加边：例如添加边 0->1 权重为2
    graph[0][1] = 2
    # 如果是无向图，需要同时添加反向边
    graph[1][0] = 2

# 2. 邻接表存储（适用于稀疏图）
def adjacency_list_example():
    n = 4  # 顶点数
    # 使用列表的列表，每个顶点对应一个列表存储其邻接点
    graph = [[] for _ in range(n)]
    
    # 添加边：例如添加边 0->1 权重为2
    graph[0].append((1, 2))  # (目标顶点，权重)
    # 如果是无向图，需要同时添加反向边
    graph[1].append((0, 2))

# 3. 边集数组存储
def edge_array_example():
    # 存储所有边的信息
    edges = []
    
    # 添加边：(起点，终点，权重)
    edges.append((0, 1, 2))
    edges.append((1, 2, 3))
    edges.append((2, 3, 4))

# 4. 链式前向星存储（静态邻接表）
class Edge:
    def __init__(self, to, weight, next):
        self.to = to        # 终点
        self.weight = weight  # 权重
        self.next = next     # 下一条边的编号

def forward_star_example():
    n = 4  # 顶点数
    m = 5  # 边数
    idx = 0  # 当前边的编号
    
    head = [-1] * n  # 每个顶点的第一条边的编号
    edges = []       # 存储所有边的信息
    
    def add_edge(u, v, w):
        nonlocal idx
        # 添加一条从u到v，权重为w的边
        edges.append(Edge(v, w, head[u]))
        head[u] = idx
        idx += 1
    
    # 使用示例
    add_edge(0, 1, 2)  # 添加边 0->1，权重为2
    add_edge(1, 2, 3)  # 添加边 1->2，权重为3

# 测试代码
if __name__ == "__main__":
    # 测试邻接矩阵
    print("邻接矩阵示例：")
    adjacency_matrix_example()
    
    # 测试邻接表
    print("\n邻接表示例：")
    adjacency_list_example()
    
    # 测试边集数组
    print("\n边集数组示例：")
    edge_array_example()
    
    # 测试链式前向星
    print("\n链式前向星示例：")
    forward_star_example()