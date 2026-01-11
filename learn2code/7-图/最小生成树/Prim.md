普里姆算法核心思想：
从一个顶点出发，每一步都选择一条“ 连接已选顶点集合和未选顶点集合 ”的最小权边

因为是不断引入新顶点，所以不会形成环

3. 选择 lowweight 最小的顶点

4. 松弛：读取邻接矩阵中当前(V-U)未加入点和新加入U的点的距离进行比较
    g.GetWeight(v, u) < closearc[u].lowweight
    如果 true 的话那么就更新 closearc[u].lowweight 同时更新邻接点 closearc[u].nearvertext = v


Prim 有双重循环，复杂度 O(n**2)