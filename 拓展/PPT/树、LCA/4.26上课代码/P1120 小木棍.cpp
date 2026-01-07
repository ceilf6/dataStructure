#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N = 70;

int n;
int cnt[N];

int maxn, minn = 100;
bool ok = false;
void dfs(int rest, int num, int sum, int cur){
    if(num == 0){
        cout << sum;
        exit(0);
    }

    if(rest == 0){
        dfs(sum, num - 1, sum, maxn);
        return;
    }

    for(int i = min(rest, cur); i >= minn; i--){
        if(cnt[i] == 0) continue;
        cnt[i]--;
        dfs(rest - i, num, sum, i);
        cnt[i]++;
        if(rest == sum || rest == i) break;
    }
    return;
}

void solve(){
    cin >> n;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        int a;
        cin >> a;
        if(a > 50) continue;
        
        cnt[a]++;
        maxn = max(maxn, a);
        minn = min(minn, a);
        sum += a;
    }

    for(int i = maxn; i <= sum / 2; i++){
        if(sum % i != 0) continue;
        dfs(i, sum / i, i, maxn);
    }

    cout << sum;
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