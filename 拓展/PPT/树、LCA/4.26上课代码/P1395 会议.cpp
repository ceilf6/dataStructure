#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N = 5e4 + 5;

vector<int> edge[N];

int n;
int s[N], w[N], cen[2];
void get_centroid(int u, int fa){
    s[u] = 1;
    w[u] = 0;
    for(auto v : edge[u]){
        if(v == fa) continue;
        get_centroid(v, u);
        s[u] += s[v];
        w[u] = max(w[u], s[v]);
    }
    w[u] = max(w[u], n - s[u]);
    if(w[u] <= n / 2) cen[cen[0] != 0] = u;
    return;
}

int ans;
void dfs(int u, int fa, int d){
    ans += d;
    for(auto v : edge[u]){
        if(v == fa) continue;
        dfs(v, u, d + 1);
    }
    return;
}

void solve(){
    cin >> n;

    for(int i = 1; i <= n - 1; i++){
        int u, v;
        cin >> u >> v;
        edge[u].push_back(v);
        edge[v].push_back(u);
    }
    get_centroid(1, 0);
    dfs(cen[0], 0, 0);

    int x = cen[0];
    if(x > cen[1] && cen[1] != 0) x = cen[1];
    cout << x << " " << ans;
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