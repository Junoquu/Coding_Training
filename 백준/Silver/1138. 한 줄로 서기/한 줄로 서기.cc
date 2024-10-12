#include <iostream>
using namespace std;

int N;
int tmp;
int res[11];

int main()
{
	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> tmp;

		for (int j = 0; j < N; j++)
		{
			if (tmp==0 && res[j]==0)
			{
				res[j] = i;
				break;
			}
			if (res[j]==0)
			{
				tmp--;
			}
		}
	}


	for (int i = 0; i < N; i++)
	{
		cout << res[i] << ' ';
	}
}