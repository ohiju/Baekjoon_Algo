#include <iostream>
#include <vector>
#include <math.h>
 
using namespace std;
 
vector<int> answer;
 
int main()
{
    int g;
    cin >> g;
 
    vector<int> vec;
    for (int i = 0; i < g + 1; i++) vec.push_back(i);
 
    int s = 1;
    int e = 1;
 
    while (e <= g)
    {
        long long _a = pow(s, 2);
 
        long long _b = pow(e, 2);
 
        if (_b - _a == g)
        {
            answer.push_back(e);
            s++;
        }
        else if (_b - _a < g) e++;
        else if (_b - _a > g) s++;
    }
 
 
    if (answer.size() == 0) cout << -1;
    else for (int ele : answer) cout << ele << '\n';
 
    return 0;
}