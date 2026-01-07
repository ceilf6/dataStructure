#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool compare(const string &a, const string &b) {
    return a + b < b + a;
}

int main() {
    int n;
    cin >> n;  
    vector<string> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
  
    sort(nums.begin(), nums.end(), compare);
   
    string result = "";
    for (const auto &num : nums) {
        result += num;
    }
    
    
    cout << result << endl;  

    
    return 0;
}
