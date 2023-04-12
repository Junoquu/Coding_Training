#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, ch, sum = 0;
	cin >> n;

	for (int i = 0; i < 3; i++) {
		cin >> ch;
		if (ch <= n)
			sum += ch;
		else if (ch > n)
			sum += n;
	}
	cout << sum;
}