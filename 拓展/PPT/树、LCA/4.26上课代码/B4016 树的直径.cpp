#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N = 1e5 + 5;

vector<int> edge[N];

int d1, d2, maxid;
int d[N];
vector<int> ds;
vector<int> s;
void dfs(int u, int fa){
    s.push_back(u);

    d[u] = d[fa] + 1;
    if(d[u] > d[maxid]) maxid = u;
    if(s.size() > ds.size()) ds = s;

    for(auto v : edge[u]){
        if(v == fa) continue;
        dfs(v, u);
    }

    s.pop_back();
    return;
}

void solve(){
    int n;
    cin >> n;

    for(int i = 1; i <= n - 1; i++){
        int u, v;
        cin >> u >> v;
        edge[u].push_back(v);
        edge[v].push_back(u);
    }
    dfs(1, 0);
    d1 = maxid;
    for(int i = 1; i <= n; i++) d[i] = 0;
    dfs(d1, 0);
    d2 = maxid;

    cout << d[d2] - 1;
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    while(T--){
        solve();
    }
    return 0;
}