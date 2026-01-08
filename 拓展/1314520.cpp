#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool check(const vector<int>& a, const vector<int>& b, int k) {
    int n = a.size(), m = b.size();
    for (int insert_pos = 0; insert_pos <= n; ++insert_pos) {
        vector<int> sorted_vals;
        sorted_vals.insert(sorted_vals.end(), a.begin(), a.begin() + insert_pos);
        sorted_vals.push_back(k);
        sorted_vals.insert(sorted_vals.end(), a.begin() + insert_pos, a.end());
        sort(sorted_vals.begin(), sorted_vals.end());
        int count = 0, j = sorted_vals.size() - 1;
        for (int i = m - 1; i >= 0; --i) {
            while (j >= 0 && sorted_vals[j] >= b[i]) {
                --j;
                ++count;
            }
            if (count >= m) return true;
        }
        if (count >= m) return true;
    }
    return false;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<int> a(n), b(m);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < m; ++i) cin >> b[i];
        sort(b.begin(), b.end());

        if (check(a, b, 0)) {
            cout << 0 << endl;
            continue;
        }

        int left = 1, right = max(*max_element(a.begin(), a.end()), *max_element(b.begin(), b.end()));
        int ans = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(a, b, mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        cout << ans << endl;
    }
    return 0;
}