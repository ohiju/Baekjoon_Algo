#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;

int N, chk[10];
ll num[] = {9,8,7,6,5,4,3,2,1,0};
vector<ll> ans, comb;

void dfs(int depth, int idx, int piv) {
    if (depth == piv) {
        ll sum = 0;
        for (auto c:comb) {
            sum += c;
            sum *= 10;
        }
        sum /= 10;
        ans.push_back(sum);
        return;
    }
    
    for (int i=idx; i<10; i++) {
        if (chk[i] == 1) continue;
        chk[i] = 1;
        comb.push_back(num[i]);
        dfs(depth+1, i+1, piv);
        comb.pop_back();
        chk[i] = 0;
    }
}

int main() 
{
    cin >> N;
    
    if (N > 1023) {
        cout << -1;
        return 0;
    }
    
    for (int i=1; i<=10; i++) {
        dfs(0,0,i);
    }
    
    sort(ans.begin(), ans.end());
    cout << ans[N-1];
    return 0;
}
