#include <iostream>
#include <string.h>
using namespace std;

int price[1000001];

void init()
{
	memset(price, 0, sizeof(price));
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		init();
		int tc;
		cin >> tc;
		for (int i = 0; i < tc; i++)
		{
			cin >> price[i];
		}

		long long max = price[tc - 1];
		long long sum = 0;

		for (int i = tc - 1; i >= 0; i--)
		{
			if (max < price[i])
			{
				max = price[i];
			}

			sum += (max - price[i]);
		}
		cout << "#" << test_case << " " << sum << '\n';
	}
	return 0;
}