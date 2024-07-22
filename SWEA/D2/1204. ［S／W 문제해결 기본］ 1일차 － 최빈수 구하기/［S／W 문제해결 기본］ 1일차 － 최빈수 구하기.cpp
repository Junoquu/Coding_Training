#include <iostream>
#include <string.h>
using namespace std;

int DAT[101] = { 0 };

void init()
{
	memset(DAT, 0, sizeof(DAT));
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
		int scores[1001];
		cin >> tc;
		for (int i = 0; i < 1000; i++)
		{
			cin >> scores[i];
			DAT[scores[i]]++;
		}

		int max = 0, maxIdx = 0;

		for (int i = 0; i < 101; i++)
		{
			if (max<=DAT[i])
			{
				max = DAT[i];
				maxIdx = i;
			}
		}

		cout << "#" << tc << " " << maxIdx << '\n';

	}
	return 0;
}