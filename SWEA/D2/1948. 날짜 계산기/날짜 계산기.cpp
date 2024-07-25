#include <iostream>
using namespace std;

int months[13] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };
int T;
int strMon, strDay, endMon, endDay;
int dayCnt = 0;

void init()
{
	dayCnt = 0;
}

void solve(int strMon, int strDay, int endMon, int endDay)
{
	if (strMon==endMon)
	{
		dayCnt = endDay - strDay + 1;
	}
	else
	{
		for (int i = strMon; i < endMon; i++)
		{
			dayCnt += months[i];
		}
		dayCnt = dayCnt - strDay +endDay + 1;
	}
	
	cout << dayCnt << '\n';
}

int main()
{
	cin >> T;
	
	for (int tc = 1; tc <= T; tc++)
	{
		init();
		cin >> strMon >> strDay >> endMon >> endDay;
		
		cout << "#" << tc << " ";

		solve(strMon,strDay,endMon,endDay);
	}
}