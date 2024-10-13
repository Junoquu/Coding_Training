#include <iostream>
using namespace std;

int n;
int arr[51];

int main()
{
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	int cnt = 0;

	for (int i = 0; i < n; i++)
	{
		if (arr[i]%2!=0)
		{
			cnt++;
		}
	}

	cout << cnt;
}