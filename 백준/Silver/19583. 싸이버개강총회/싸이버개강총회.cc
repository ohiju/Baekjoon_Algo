#include <iostream>
#include <unordered_map>

using namespace std;
string S,E,Q,T, name;
unordered_map<string, int> nicknames;
int answer = 0;

int main()
{
    cin >> S >> E >> Q;
    
    while(cin >> T >> name) {
        if (T <= S)
        {
            nicknames[name] = 1;
        }
        else if (T >= E && T <= Q) 
        {
            if (nicknames[name] == 1)
            {
                nicknames[name] = 2;
                answer++;
            }
        }
    }
    
    cout << answer;
    return 0;
}