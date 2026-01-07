#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL MOD;

struct Segment_Tree{

    static const int N = 1e5 + 5;

    #define lson rt << 1, l, mid
    #define rson rt << 1 | 1, mid + 1, r

    LL tree[N << 2], mul[N << 2], add[N << 2];

    void pushup(int rt, int l, int r){
        tree[rt] = (tree[rt << 1] + tree[rt << 1 | 1]) % MOD;
        return;
    }

    void pushdown(int rt, int l, int r){
        if(mul[rt] != 1){
            tree[rt << 1] = tree[rt << 1] * mul[rt] % MOD;
            tree[rt << 1 | 1] = tree[rt << 1 | 1] * mul[rt] % MOD;
            mul[rt << 1] = mul[rt << 1] * mul[rt] % MOD;
            add[rt << 1] = add[rt << 1] * mul[rt] % MOD;
            mul[rt << 1 | 1] = mul[rt << 1 | 1] * mul[rt] % MOD;
            add[rt << 1 | 1] = add[rt << 1 | 1] * mul[rt] % MOD;
            mul[rt] = 1;
        }
        if(add[rt]){
            int mid = (l + r) >> 1;
            tree[rt << 1] = (tree[rt << 1] + (mid - l + 1) * add[rt] % MOD) % MOD;
            tree[rt << 1 | 1] = (tree[rt << 1 | 1] + (r - mid) * add[rt] % MOD) % MOD;
            add[rt << 1] = (add[rt << 1] + add[rt]) % MOD;
            add[rt << 1 | 1] = (add[rt << 1 | 1] + add[rt]) % MOD;
            add[rt] = 0;
        }
        return;
    }

    void build(int rt, int l, int r){
        mul[rt] = 1;
        add[rt] = 0;
        if(l == r){
            tree[rt] = 0;
            return;
        }
        int mid = (l + r) >> 1;
        build(lson);
        build(rson);
        pushup(rt, l, r);
        return;
    }

    void update(int rt, int l, int r, int L, int R, int c, LL k){
        if(L <= l && r <= R){
            if(c == 1){
                tree[rt] = tree[rt] * k % MOD;
                mul[rt] = mul[rt] * k % MOD;
                add[rt] = add[rt] * k % MOD;
            }else{
                tree[rt] = (tree[rt] + (r - l + 1) * k % MOD) % MOD;
                add[rt] = (add[rt] + k) % MOD;
            }
            return;
        }
        pushdown(rt, l, r);
        int mid = (l + r) >> 1;
        if(L <= mid) update(lson, L, R, c, k);
        if(R >  mid) update(rson, L, R, c, k);
        pushup(rt, l, r);
        return;
    }

    LL query(int rt, int l, int r, int L, int R){
        if(L <= l && r <= R) return tree[rt];
        pushdown(rt, l, r);

        int mid = (l + r) >> 1;
        LL ans = 0;
        if(L <= mid) ans = (ans + query(lson, L, R)) % MOD;
        if(R >  mid) ans = (ans + query(rson, L, R)) % MOD;
        return ans;
    }

}S;

void solve(){
    int n, q;
    cin >> n >> q >> MOD;
    
    S.build(1, 1, n);
    for(int i = 1; i <= n; i++){
        LL a;
        cin >> a;
        S.update(1, 1, n, i, i, 2, a % MOD);
    }

    while(q--){
        int opt, x, y; LL k;
        cin >> opt >> x >> y;
        if(opt == 1){
            cin >> k;
            S.update(1, 1, n, x, y, 1, k % MOD);
        }else if(opt == 2){
            cin >> k;
            S.update(1, 1, n, x, y, 2, k % MOD);
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