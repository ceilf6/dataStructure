// #include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> vis; // 三色标记：0=未访问, 1=访问中, 2=已完成
vector<int> topo;
bool hasCycle = false;

void dfs(int u)
{
    vis[u] = 1;
    for (int v : graph[u])
    {
        if (vis[v] == 0)
        {
            dfs(v);
            if (hasCycle) // 剪枝：如果中途打标记有环那么直接中断
                return;
        }
        else if (vis[v] == 1)
        {
            hasCycle = true;
            return;
        }
    }
    vis[u] = 2; // DFS结束后打标记完成
    topo.push_back(u);
}

int main()
{
    int n = 4;
    graph = {
        {1, 2},
        {3},
        {3},
        {}};

    vis.assign(n, 0); // 长度为n，初始值为0

    for (int i = 0; i < n; i++)
    {
        if (vis[i] == 0)
            dfs(i);
    }

    if (hasCycle)
    {
        cout << "有环，无法拓扑排序\n";
        return 0;
    }

    reverse(topo.begin(), topo.end()); // 逆序: 先进入的就是后进入的前驱

    cout << "DFS 拓扑序：";
    for (int x : topo)
        cout << x << " ";
    cout << "\n";
}