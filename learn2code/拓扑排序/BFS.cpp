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
    vector<vector<int>> graph = {
        {1, 2}, // 0
        {3},
        {3},
        {} // 3
    };

    vector<int> indeg(n, 0);
    for (int u = 0; u < n; u++)
    {
        for (int v : graph[u])
        {
            indeg[v]++;
        }
    }

    queue<int> q;
    for (int i = 0; i < n; i++)
    {
        if (indeg[i] == 0)
            q.push(i);
    }

    vector<int> topo;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        topo.push_back(u);

        for (int v : graph[u])
        {
            if (--indeg[v] == 0)
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