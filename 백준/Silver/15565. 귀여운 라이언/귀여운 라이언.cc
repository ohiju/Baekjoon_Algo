#include <iostream>
#include <vector>
using namespace std;

int N,K;
int inf=10000000;
vector<int> vec;


int main()
{
    cin >> N >> K;
    for (int i=0;i<N;i++) {
        int x;
        cin >> x;
        if (x == 1) {
            vec.push_back(i);
        }
    }
    
    if (vec.size() < K) {
        cout << -1;
        return 0;
    }
    
    int l=0,r=K-1,rec=inf;
    for (int i=0;i<vec.size()-K+1;i++) {
        rec = min(rec, vec[r] - vec[l] + 1);
        l++;
        r++;
    }
    
    cout << rec;
}