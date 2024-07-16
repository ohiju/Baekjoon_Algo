#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N,S,D;
int ans = 0;
vector<int> vec[100001];
int depth[100001];

int dfs(int node, int before){
    for(auto next: vec[node]){
        if(next != before){
            depth[node] = max(depth[node], dfs(next, node)+1);
        }
    }
    if(depth[node]>=D && node != S) ans++;
    return depth[node];
}

int main()
{
    // 인풋 받기
    cin >> N >> S >> D;
    for (int i=1; i<N; i++) {
        int x,y;
        cin >> x >> y;
        vec[x].push_back(y);
        vec[y].push_back(x);
    }
    
    
    dfs(S, -1);
    cout<<ans*2;
    
    return 0;
}