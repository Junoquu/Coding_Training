#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	string s;

	while (1) {
		cin >> s;
		int width = s.length() + 1;
		if (s == "0")
			break;
		else {
			for (int i = 0; i < s.length(); i++) {
				if (s[i] == '1')
					width += 2;
				else if (s[i] == '0')
					width += 4;
				else
					width += 3;
			}
		}		
		cout << width << endl;
	}
}