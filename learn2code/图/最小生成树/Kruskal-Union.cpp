struct Edge
{
    int u, v;
    int w;
};

bool cmp(const Edge &a, const Edge &b)
{
    return a.w < b.w;
}

int parent[N];

int find(int x)
{
    if (parent[x] != x)
        parent[x] = find(parent[x]);
    return parent[x];
}

void unite(int x, int y)
{
    x = find(x);
    y = find(y);
    if (x != y)
        parent[y] = x;
}

int Kruskal(int n, vector<Edge> &edges)
{
    sort(edges.begin(), edges.end(), cmp);
    for (int i = 0; i < n; i++)
        parent[i] = i;

    int cnt = 0, sum = 0;
    for (auto &e : edges)
    {
        if (find(e.u) != find(e.v))
        {
            unite(e.u, e.v);
            sum += e.w;
            cnt++;
            if (cnt == n - 1)
                break;
        }
    }
    return sum;
}