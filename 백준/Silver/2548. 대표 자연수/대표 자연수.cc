#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, ans, diff = 987654321;
vector<int> nums;

int main() {
    cin >> N;
    nums.resize(N);
    
    for (int i=0; i<N; i++) {
        cin >> nums[i];
    }
    
    sort(nums.begin(), nums.end());
    
    for (int i=0; i<N; i++) {
        int sum = 0;
        for (int j=0; j<N; j++) {
            if (i == j) continue;
            sum += abs(nums[j] - nums[i]);
        }
        if (diff > sum) {
            diff = sum;
            ans = nums[i];
        }
    }
    
    cout << ans;
    return 0;
}