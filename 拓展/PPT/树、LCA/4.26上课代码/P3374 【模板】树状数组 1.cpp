#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N = 5e5 + 5;

struct Fenwick{

    LL tree[N]; int n;

    void init(int _n){
        n = _n;
        return;
    }

    int lowbit(int x){
        return x & (-x);
    }

    void update(int id, LL k){
        while(id <= n){
            tree[id] += k;
            id += lowbit(id);
        }
        return;
    }

    LL query(int id){
        LL ans = 0;
        while(id >= 1){
            ans += tree[id];
            id -= lowbit(id);
        }
        return ans;
    }

}F;

void solve(){
    int n, m;
    cin >> n >> m;

    F.init(n);
    vector<LL> a(n + 1);
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        F.update(i, a[i]);
    }

    while(m--){
        int opt, x, y;
        cin >> opt >> x >> y;
        if(opt == 1){
            F.update(x, y);
        }else{
            cout << F.query(y) - F.query(x - 1) << "\n";
        }
    }
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