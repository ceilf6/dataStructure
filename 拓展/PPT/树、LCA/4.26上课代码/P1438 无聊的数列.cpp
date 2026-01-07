#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

struct Segment_Tree{

    static const int N = 1e5 + 5;

    #define lson rt << 1, l, mid
    #define rson rt << 1 | 1, mid + 1, r

    LL tree[N << 2], tagf[N << 2], tagd[N << 2];

    void pushdown(int rt, int l, int r){
        if(tagf[rt] != 0 || tagd[rt] != 0){
            tree[rt << 1] += tagf[rt];
            tagf[rt << 1] += tagf[rt];
            tagd[rt << 1] += tagd[rt];

            int mid = (l + r) >> 1;
            tree[rt << 1 | 1] += tagf[rt] + tagd[rt] * (mid - l + 1);
            tagf[rt << 1 | 1] += tagf[rt] + tagd[rt] * (mid - l + 1);
            tagd[rt << 1 | 1] += tagd[rt];

            tagf[rt] = 0;
            tagd[rt] = 0;
        }
        return;
    }

    void build(int rt, int l, int r){
        if(l == r){
            tree[rt] = 0;
            tagf[rt] = 0;
            tagd[rt] = 0;
            return;
        }
        int mid = (l + r) >> 1;
        build(lson);
        build(rson);
        return;
    }

    void update(int rt, int l, int r, int L, int R, LL K, LL k, LL d){
        if(L <= l && r <= R){
            tree[rt] += k;
            tagf[rt] += k;
            tagd[rt] += d;
            return;
        }
        pushdown(rt, l, r);

        int mid = (l + r) >> 1;
        if(L <= mid) update(lson, L, R, K, K + max(l - L, 0) * d, d);
        if(R >  mid) update(rson, L, R, K, K + max(mid + 1 - L, 0) * d, d);
        return;
    }

    LL query(int rt, int l, int r, int id){
        if(l == r) return tree[rt];
        pushdown(rt, l, r);

        int mid = (l + r) >> 1;
        LL ans = 0;
        if(id <= mid) ans = query(lson, id);
        else ans = query(rson, id);
        return ans;
    }

}S;

void solve(){
    int n, m;
    cin >> n >> m;
    
    S.build(1, 1, n);
    for(int i = 1; i <= n; i++){
        LL a;
        cin >> a;
        S.update(1, 1, n, i, i, a, a, 0);
    }

    while(m--){
        int opt, l, r; LL k, d;
        cin >> opt;
        if(opt == 1){
            cin >> l >> r >> k >> d;
            S.update(1, 1, n, l, r, k, k, d);
        }else{
            cin >> l;
            cout << S.query(1, 1, n, l) << "\n";
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