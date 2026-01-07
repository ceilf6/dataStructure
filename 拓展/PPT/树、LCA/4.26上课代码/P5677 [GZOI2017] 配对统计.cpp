#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

struct Fenwick{

    static const int N = 3e5 + 5;

    int n, tree[N];

    void init(int _n){
        n = _n;
        for(int i = 1; i <= n; i++) tree[i] = 0;
        return;
    }

    int lowbit(int x){
        return x & (-x);
    }

    void update(int id, int k){
        while(id <= n){
            tree[id] += k;
            id += lowbit(id);
        }
        return;
    }

    int query(int id){
        int ans = 0;
        while(id >= 1){
            ans += tree[id];
            id -= lowbit(id);
        }
        return ans;
    }

}F;

bool cmp_pair(pair<int, int> a, pair<int, int> b){
    return a.second < b.second;
}

bool cmp_array(array<int, 3> a, array<int, 3> b){
    return a[1] < b[1];
}

void solve(){
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> a(n + 1);
    for(int i = 1; i <= n; i++){
        cin >> a[i].first;
        a[i].second = i;
    }
    sort(a.begin() + 1, a.end());
    
    vector<pair<int, int>> itv;
    if(n > 1){
        itv.push_back({min(a[1].second, a[2].second), max(a[1].second, a[2].second)});
        itv.push_back({min(a[n - 1].second, a[n].second), max(a[n - 1].second, a[n].second)});
    }
    for(int i = 2; i <= n - 1; i++){
        if(a[i].first - a[i - 1].first <= a[i + 1].first - a[i].first)
        itv.push_back({min(a[i - 1].second, a[i].second), max(a[i - 1].second, a[i].second)});
        if(a[i].first - a[i - 1].first >= a[i + 1].first - a[i].first)
        itv.push_back({min(a[i].second, a[i + 1].second), max(a[i].second, a[i + 1].second)});
    }
    sort(itv.begin(), itv.end(), cmp_pair);
    
    vector<array<int, 3>> q(m + 1);
    for(int i = 1; i <= m; i++){
        cin >> q[i][0] >> q[i][1];
        q[i][2] = i;
    }
    sort(q.begin() + 1, q.end(), cmp_array);
    
    F.init(n);
    int t = 0;
    LL ans = 0;
    for(int i = 1; i <= m; i++){
        auto [l, r, id] = q[i];
        while(t < itv.size() && itv[t].second <= r){
            F.update(itv[t].first, 1);
            t++;
        }
        ans += 1LL * id * (F.query(r) - F.query(l - 1));
    }
    
    cout << ans;
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