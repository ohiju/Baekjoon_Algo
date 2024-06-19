#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    double x,y,c;
    cin >> x >> y >> c;

    double start = 0;
    double end = min(x,y);

    double ans = 0;

    while (end - start > 0.000001) {
        double mid = (start + end) / 2;

        double a = pow((pow(x,2) - pow(mid,2)), 0.5);
        double b = pow((pow(y,2) - pow(mid,2)), 0.5);

        double tmp_ans = a*b / (a+b);

        if (tmp_ans >= c) {
            ans = mid;
            start = mid;
        }
        else {
            end = mid;
        }
    }

    cout << ans;
    return 0;
}