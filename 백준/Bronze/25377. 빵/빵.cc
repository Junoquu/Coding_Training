#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, a, b, time = 999;

	cin >> n;
	while(n--){
		cin >> a >> b;
		if (a <= b) {
			time = min(time, b);
		}
	}
	if (time == 999)
		cout << -1;
	else
		cout << time;
}