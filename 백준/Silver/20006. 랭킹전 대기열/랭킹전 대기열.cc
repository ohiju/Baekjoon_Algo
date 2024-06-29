#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int,string> a, pair<int,string> b) {
    return a.second < b.second;
}

int main() 
{
    int p,m;
    int l; string n;
    vector<vector<pair<int,string>>> vec;
    
    cin >> p >> m;
    
    for (int i=0; i<p; i++) {
        cin >> l >> n;
        
        if (vec.empty()) {
            vec.push_back({ {l,n} });
            continue;
        }
        
        for (int j=0; j<=vec.size(); j++) {
            if (vec[j].size() < m) {
                if (vec[j][0].first + 10 >= l && vec[j][0].first - 10 <= l )
                {
                    vec[j].push_back({l,n});
                    break;
                }
                else {
                    if (j == vec.size() - 1)
                    {
                        vec.push_back({ {l,n} });
                        break;
                    }
                    else {
                        continue;
                    }
                }
            }
            else {
                    if (j == vec.size() - 1)
                    {
                        vec.push_back({ {l,n} });
                        break;
                    }
                    else {
                        continue;
                    }
                }
        }
    }
    
    for (int i=0; i<vec.size(); i++) {
        sort(vec[i].begin(), vec[i].end(), compare);

        if (vec[i].size() == m) {
            cout << "Started!" << "\n";
        } else {
            cout << "Waiting!" << "\n";
        }

        for (int j=0; j<vec[i].size(); j++) {
            cout << vec[i][j].first << " " << vec[i][j].second << "\n";
        }
    }

    return 0;
}