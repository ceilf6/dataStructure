#include <bits/stdc++.h>
using namespace std;

#define F(a, b) fixed << setprecision(b) << a
typedef long long LL;
const int N = 1e5 + 50;

LL a[N];

struct Segment_Tree{

    #define lson rt << 1, l, mid
    #define rson rt << 1 | 1, mid + 1, r

    struct node_tree{
        LL val, tag;
    }tree[N << 2];

    void pushup(int rt, int l, int r){
        tree[rt].val = tree[rt << 1].val + tree[rt << 1 | 1].val;
        return;
    }

    void pushdown(int rt, int l, int r){
        if(tree[rt].tag){
            int tag = tree[rt].tag;
            int mid = (l + r) >> 1;
            tree[rt << 1].val += tag * (mid - l + 1); tree[rt << 1].tag += tag;
            tree[rt << 1 | 1].val += tag * (r - mid); tree[rt << 1 | 1].tag += tag;
            tree[rt].tag = 0;
        }
        return;
    }

    void build(int rt, int l, int r){
        if(l == r){
            tree[rt].val = a[l];
            tree[rt].tag = 0;
            return;
        }
        int mid = (l + r) >> 1;
        build(lson);
        build(rson);
        pushup(rt, l, r);
        return;
    }

    void update(int rt, int l, int r, int L, int R, LL k){
        if(L <= l && r <= R){
            tree[rt].val += k * (r - l  + 1);
            tree[rt].tag += k;
            return;
        }
        pushdown(rt, l, r);
        int mid = (l + r) >> 1;
        if(L <= mid) update(lson, L, R, k);
        if(R >  mid) update(rson, L, R, k);
        pushup(rt, l, r);
        return;
    }

    LL query(int rt, int l, int r, int L, int R){
        if(L <= l && r <= R) return tree[rt].val;
        pushdown(rt, l, r);
        int mid = (l + r) >> 1;
        LL ans = 0;
        if(L <= mid) ans += query(lson, L, R);
        if(R >  mid) ans += query(rson, L, R);
        return ans;
    }

}S;

void solve(){
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) cin >> a[i];    
    S.build(1, 1, n);
    while(m--){
        int opt, x, y; LL z;
        cin >> opt >> x >> y;
        if(opt == 1){
            cin >> z;
            S.update(1, 1, n, x, y, z);
        }else{
            cout << S.query(1, 1, n, x, y) << "\n";
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