#include <iostream>
using namespace std;

int n, m;
int day_stress;
int stress=0;
int cnt = 0;

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		cin >> day_stress;
		stress += day_stress;
		if (stress<0)
		{
			stress = 0;
		}
		if (stress>=m)
		{
			cnt++;
		}
	}
	cout << cnt;
}