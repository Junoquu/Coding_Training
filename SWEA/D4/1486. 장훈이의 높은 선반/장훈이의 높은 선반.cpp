#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int n, b;
vector<int> employee;
int res;

void init()
{
	employee.clear();
	res = 21e8;
}

void input()
{
	int cm; 
	cin >> n >> b;
	employee.resize(n);
	for (int i = 0; i < n; i++)
	{
		cin >> cm;
		employee[i] = cm;
	}
}

void solve(int idx, int cur_height)
{
	if (cur_height >= b)
	{
		res = min(res, cur_height - b);
		return;
	}

	if (idx >= n)
	{
		return;
	}

	solve(idx + 1, cur_height);
	solve(idx + 1, cur_height + employee[idx]);
}

int main()
{
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		init();
		input();
		solve(0, 0);

		cout << "#" << t << " " << res << endl;
	}
}