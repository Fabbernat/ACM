#include <iostream>
#include <vector>
#include <numeric>
using namespace std;


bool john_wins(const vector<int>& eminems) {
    int xor_sum = 0;
    for (int count : eminems) {
        xor_sum ^= count;
    }
    return xor_sum != 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> eminems(N);
        for (int i = 0; i < N; ++i) {
            cin >> eminems[i];
        }

        cout << (john_wins(eminems) ? "John" : "Brother") << '\n';
    }

    return 0;
}
