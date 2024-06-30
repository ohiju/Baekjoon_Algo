#include <iostream>
using namespace std;

int main()
{
    int L, A, B, C, D;
    cin >> L >> A >> B >> C >> D;
    
    int days_for_A = (A + C - 1) / C;
    int days_for_B = (B + D - 1) / D;

    int max_days = max(days_for_A, days_for_B);
    int remaining_days = L - max_days;

    cout << remaining_days << endl;
    return 0;
}