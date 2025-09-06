#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> vec(5);

int main() {

	int sum = 0;

	for (int i = 0; i < 5; i++) {
		cin >> vec[i];
		sum += vec[i];
	}

	sort(vec.begin(), vec.end());

	cout << sum / 5 << "\n" << vec[2];
    
    return 0;
}