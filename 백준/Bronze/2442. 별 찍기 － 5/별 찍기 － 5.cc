#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j=n-2; j >= i; j--) {
			cout << " ";
		}
		for (int m = 1; m <= 2*i+1; m++) {
			cout << "*";
		}
		cout << endl;
	}
}