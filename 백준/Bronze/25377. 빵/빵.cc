#include <iostream>
using namespace std;

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, a, b, time = 999;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		if (a <= b) {
			time = min(time, b);
		}
	}
	if (time < 999)
		cout << time;
	else
		cout << -1;

}