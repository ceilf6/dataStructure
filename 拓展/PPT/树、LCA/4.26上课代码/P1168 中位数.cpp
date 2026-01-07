#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

void solve(){
    int n;
    cin >> n;

    priority_queue<int, vector<int>, less<int> > q1;
    priority_queue<int, vector<int>, greater<int> > q2;

    vector<int> a(n + 1);
    for(int i = 1; i <= n; i++) cin >> a[i];

    q1.push(a[1]);
    cout << a[1] << "\n";
    for(int i = 2; i <= n; i++){
        if(a[i] > q1.top()) q2.push(a[i]);
        else q1.push(a[i]);
        if(i % 2 == 1){
            while(q2.size() > q1.size()){
                int u = q2.top();
                q2.pop();
                q1.push(u);
            }
            while(q1.size() > q2.size() + 1){
                int u = q1.top();
                q1.pop();
                q2.push(u);
            }
            cout << q1.top() << "\n";
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