#include <iostream>
using namespace std;

int find(int arr[]) {
	for (int i = 0; i < 4; i++) {
		if (arr[i] == 1) {
			return i;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int arr[] = { 0,1,2,3 };

	int n, x, y, temp;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> x >> y;

		temp = arr[x];
		arr[x] = arr[y];
		arr[y] = temp;
	}
	if (find(arr) > 0)
		cout << find(arr);
	else
		cout << -1;
}