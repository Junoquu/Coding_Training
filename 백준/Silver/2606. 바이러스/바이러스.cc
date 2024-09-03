#include <iostream>
#include <vector>
using namespace std;

int N, M;
int from, to;
int cnt = 0;
int visited[101];

vector<int> v[101];

void dfs(int st)
{
	cnt++;
	for (int i = 0; i < v[st].size(); i++)
	{
		int now = v[st][i];

		if (visited[now])
		{
			continue;
		}

		visited[now] = 1;
		dfs(now);
	}
}

int main()
{
	cin >> N;
	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> from >> to;
		v[from].push_back(to);
		v[to].push_back(from);
	}

	visited[1] = 1;
	dfs(1);

	cout << cnt - 1;
}