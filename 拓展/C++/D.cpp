#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool can_collect(const vector<int>& a, const vector<int>& b, int k) {
    int n = a.size();
    int m = b.size();
    int j = 0;
    for (int i = 0; i < n && j < m; ++i) {
        if (a[i] >= b[j]) {
            ++j;
        }
    }
    return j == m;
}

int solve() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> b(m);
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }

    if (can_collect(a, b, 0)) {
        return 0;
    }

    int min_k = -1;
    for (int k = 1; k <= 100; ++k) { 
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, k);
            if (can_collect(temp_a, b, k)) {
                if (min_k == -1 || k < min_k) {
                    min_k = k;
                }
            }
        }
    }
    
    if (min_k == -1) {
        int low = 1, high = 1e9;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            bool possible = false;
            for (int i = 0; i <= n; ++i) {
                vector<int> temp_a = a;
                temp_a.insert(temp_a.begin() + i, mid);
                if (can_collect(temp_a, b, mid)) {
                    possible = true;
                    break;
                }
            }
            if (possible) {
                min_k = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        if (min_k > 1e9) return -1;
        
        bool possible = false;
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, min_k);
            if (can_collect(temp_a, b, min_k)) {
                possible = true;
                break;
            }
        }
        if (!possible) return -1;
        
    } else {
        bool possible = false;
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, min_k);
            if (can_collect(temp_a, b, min_k)) {
                possible = true;
                break;
            }
        }
        if (!possible) return -1;
    }
    
    
    
    if (min_k == -1) {
        
        int max_b = 0;
        for(int val : b) max_b = max(max_b, val);
        
        bool possible = false;
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, max_b);
            if (can_collect(temp_a, b, max_b)) {
                possible = true;
                break;
            }
        }
        if(possible) return max_b;
        else return -1;
        
    }
    
    int real_min_k = -1;
    for (int k = 1; k <= 2000; ++k) { 
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, k);
            if (can_collect(temp_a, b, k)) {
                if (real_min_k == -1 || k < real_min_k) {
                    real_min_k = k;
                }
            }
        }
    }
    
    if(real_min_k == -1) {
        int max_b = 0;
        for(int val : b) max_b = max(max_b, val);
        
        bool possible = false;
        for (int i = 0; i <= n; ++i) {
            vector<int> temp_a = a;
            temp_a.insert(temp_a.begin() + i, max_b);
            if (can_collect(temp_a, b, max_b)) {
                possible = true;
                break;
            }
        }
        if(possible) return max_b;
        else return -1;
    }
    
    return real_min_k;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
    return 0;
}