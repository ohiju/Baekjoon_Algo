#include <iostream>
using namespace std;

int N,M,K,x1,y1,x2,y2;
int map[1025][1025];
int dp[1025][1025];

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;
    for (int i=1;i<=N;i++) {
        for (int j=1;j<=M;j++) {
            cin >> map[i][j];
            dp[i][j] = map[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
        }
    }
    
    cin >> K;
    
    for (int i=0;i<K;i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        int result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1];
        cout << result << "\n";
    }
} 