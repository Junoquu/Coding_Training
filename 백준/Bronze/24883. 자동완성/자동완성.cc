#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	char n;
	cin >> n;
	if (n == 'N' || n == 'n')
		cout << "Naver D2";
	else
		cout << "Naver Whale";
}