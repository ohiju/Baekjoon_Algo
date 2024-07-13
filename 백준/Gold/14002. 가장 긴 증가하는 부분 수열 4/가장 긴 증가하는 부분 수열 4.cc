#include<iostream>
#include<vector>
using namespace std;
#define max(a,b) (a > b) ? a: b

int N;
int A[1001];
int dp[1001];
vector<int> increase; 
 
int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> A[i];

    for (int i = N - 1; i >= 0; i--)
    {
        dp[i] = 1;
        for (int j = N - 1; j > i; j--)
        {
            if (A[j] > A[i]) dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    int ans = dp[0];
    for (int i = 1; i < N; i++)
        if (ans < dp[i]) ans = dp[i];

    cout << ans << endl;

    for (int i = 0; i < N; i++) {
        if (dp[i] == ans) {
            increase.push_back(A[i]);
            ans--;
        }
    }

    for (int i = 0; i < increase.size(); i++) {
        cout << increase[i] << " ";
    }

    return 0;
}