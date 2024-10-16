#include <iostream>
using namespace std;

int n, m;
int path[9];
int visited[9];

void recur(int lev)
{
	if (lev==m)
	{
		for (int i = 0; i < m; i++)
		{
			cout << path[i] << ' ';
		}
		cout << '\n';
		return;
	}

	for (int i = 1; i <= n; i++)
	{
		if (visited[i])
		{
			continue;
		}

		path[lev] = i;
		visited[i] = 1;
		recur(lev + 1);
		path[lev] = 0;
		visited[i] = 0;
	}
}

int main()
{
	cin >> n >> m;

	recur(0);
}