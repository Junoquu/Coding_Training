#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, out = 1;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		out *= 2;
	}
	cout << out;
}