#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

struct Fenwick{

    static const int N = 5e5 + 5;

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

void solve(){
    int n;
    cin >> n;

    vector<int> a(n + 1);
    for(int i = 1; i <= n; i++) cin >> a[i];

    auto p = a;
    sort(p.begin() + 1, p.end());
    int m = unique(p.begin() + 1, p.end()) - p.begin() - 1;
    
    F.init(m);
    LL ans = 0;
    for(int i = 1; i <= n; i++){
        int x = lower_bound(p.begin() + 1, p.begin() + 1 + m, a[i]) - p.begin();
        ans += F.query(m) - F.query(x);
        F.update(x, 1);
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