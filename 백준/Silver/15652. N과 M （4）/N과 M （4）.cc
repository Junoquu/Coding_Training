#include <iostream>
using namespace std;

int n, m;

int path[9];
int visited[9];

void dfs(int lev,int num)
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

	for (int i = num; i <= n; i++)
	{
		path[lev] = i;
		visited[i] = 1;
		dfs(lev + 1,i);	
		visited[i] = 0;
	}
}

int main()
{
	cin >> n >> m;

	dfs(0,1);
}