#include <iostream>
#include <algorithm>
using namespace std;

int min(int a, int b) {
	return a < b ? a : b;
}
int Young(int tel) {
	int money = 0;
	if (tel / 30 >= 1) {
		if (tel % 30 < 30)
			money = tel / 30 + 1;
	}
	else
		money = 1;
	return money * 10;
}
int Min(int tel) {
	int money = 0;
	if (tel / 60 >= 1) {
		if(tel%60<60)
			money = tel / 60 + 1;
	}
	else
		money = 1;
	return money * 15;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, tel, Y = 0, M = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tel;
		Y += Young(tel);
		M += Min(tel);
	}

	if(Y==M)
		cout << "Y M " << min(Y, M) << endl;
	else if (min(Y, M) == Y)
		cout << "Y " << Y << endl;
	else if (min(Y, M) == M)
		cout << "M " << M << endl;
}