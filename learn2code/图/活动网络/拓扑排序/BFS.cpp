// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int n = 4;
    // 邻接表
    // vector<vector<int>> graph = {
    //     {1, 2}, // 0
    //     {3},
    //     {3},
    //     {} // 3
    // };
    vector<vector<int>> graph = {
        {1},
        {2},
        {3},
        {0}};

    vector<int> indeg(n, 0);
    for (int u = 0; u < n; u++)
    {
        for (int v : graph[u])
        {
            indeg[v]++; // 入度统计
        }
    }

    queue<int> q;
    for (int i = 0; i < n; i++)
    {
        if (indeg[i] == 0)
            q.push(i); // BFS队列初始化：入度为 0 的点
    }

    vector<int> topo;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        topo.push_back(u);
        // 出队进入拓扑序列

        for (int v : graph[u])
        {
            if (--indeg[v] == 0) // 对应的相邻点入度-1
            {
                q.push(v);
            }
        }
    }

    if ((int)topo.size() < n)
    {
        cout << "有环，无法拓扑排序\n";
    }
    else
    {
        cout << "BFS 拓扑序：";
        for (int x : topo)
            cout << x << " ";
        cout << "\n";
    }
}