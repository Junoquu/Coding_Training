#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j=1; j <= i; j++) {
			cout << " ";
		}
		for (int m = 1; m <=n-i; m++) {
			cout << "*";
		}
		cout << endl;
	}
}