#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int n, b;
vector<int> height;
int res;

void init()
{
	height.clear();
	res = 21e8;
}

void input()
{
	cin >> n >> b;

	height.resize(n);

	for (int i = 0; i < n; i++)
	{
		cin >> height[i];
	}
}

void solve(int idx, int cur_height)
{
	if (cur_height >= b)
	{
		res = min(res, cur_height-b);
		return;
	}

	if (idx>=n)
	{
		return;
	}

	solve(idx + 1, cur_height);
	solve(idx + 1, cur_height + height[idx]);
}

int main()
{
	cin >> T;

	for (int tc = 1; tc <= T; tc++)
	{
		init();
		input();
		solve(0, 0);

		cout << "#" << tc << " " << res << "\n";
	}
}