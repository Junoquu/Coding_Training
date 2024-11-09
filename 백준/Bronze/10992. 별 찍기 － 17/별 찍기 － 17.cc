#include <iostream>
using namespace std;

int n;

int main()
{
	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		for (int j = n - i; j > 0; j--)
		{
			cout << ' ';
		}
		if (i==1 || i==n)
		{
			for (int j = 1; j < i*2; j++)
			{
				cout << "*";
			}
		}
		else
		{
			for (int j = 1; j < i*2; j++)
			{
				if (j==1||j==i*2-1)
				{
					cout << "*";
				}
				else
				{
					cout << " ";
				}
				
			}
		}
		
		cout << '\n';
	}
}