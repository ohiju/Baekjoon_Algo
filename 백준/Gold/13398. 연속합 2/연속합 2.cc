#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[100001][2], arr[100001];
int n;

int main() 
{
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    dp[0][0] = arr[0];
    dp[0][1] = arr[0];

    int MAX = arr[0];
    for (int i=1; i<n; i++) {
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i]);
        MAX = max(MAX, max(dp[i][0], dp[i][1]));
    }
    cout << MAX;

    return 0;
}
