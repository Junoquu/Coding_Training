#include <iostream>
using namespace std;

int n, m;

int path[8];

void dfs(int lev)
{
	if (lev == m)
	{
		for (int i = 0; i < m; i++)
		{
			cout << path[i]<<' ';
		}
		cout << '\n';
		return;
	}

	for (int i = 1; i <= n; i++)
	{
		path[lev] = i;
		dfs(lev + 1);	
	}
}

int main()
{
	cin >> n >> m;

	dfs(0);
}