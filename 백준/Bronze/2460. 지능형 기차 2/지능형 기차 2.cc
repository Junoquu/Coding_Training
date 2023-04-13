#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int out, in, person = 0, max = 0;

	for (int i = 0; i < 10; i++) {
		cin >> out >> in;

		person += (in - out);

		if (max < person)
			max = person;
	}
	cout << max;
}