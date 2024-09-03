#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

vector<int> v[1001];

int N, M, V;
int from, to;
int visited[1001];

void dfs(int st)
{
	cout << st << ' ';
	
	for (int i = 0; i < v[st].size(); i++)
	{
		int to = v[st][i];
		if (visited[to])
			continue;

		visited[to] = 1;
		dfs(to);
	}
}

void bfs(int st)
{
	queue<int>q;
	visited[st] = 1;
	q.push(st);

	while (!q.empty())
	{
		int now = q.front();
		q.pop();
		cout << now << ' ';

		for (int i = 0; i < v[now].size(); i++)
		{
			int next = v[now][i];
			if (visited[next])
				continue;

			visited[next] = 1;
			q.push(next);
		}
	}
}

int main()
{
	cin >> N >> M >> V;

	for (int i = 0; i < M; i++)
	{
		cin >> from >> to;
		v[from].push_back(to);
		v[to].push_back(from);
	}

	for (int i = 1; i <= N; i++) {
		sort(v[i].begin(), v[i].end());
	}

	visited[V] = 1;
	dfs(V);
	memset(visited, 0, sizeof(visited));
	cout << '\n';
	bfs(V);
}