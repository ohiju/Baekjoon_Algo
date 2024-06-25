#include <iostream>
using namespace std;

int main()
{   
    int n;    
    long long dp[101];

    cin >> n;

    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i-1] + 1;
        for (int j = 3; j < i; j++) {
            dp[i] = max(dp[i], dp[i-j] * (j-1));
        }
    }

    cout << dp[n] << endl;
    return 0;
}