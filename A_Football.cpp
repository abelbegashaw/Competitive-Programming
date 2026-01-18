#include <iostream>
using namespace std;

int main() {
    string players;
    cin >> players;
    int start = 0;
    bool flag = false;
    for(int end = 1; end < players.size(); end++) {
        if (players[end] != players[start]) {
            start = end;
        } else if (start - end + 1 == 7) {
            flag = true;
            break;
        }
    } 
    if (flag) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}