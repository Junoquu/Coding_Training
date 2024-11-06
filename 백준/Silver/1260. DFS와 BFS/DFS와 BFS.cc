#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, m, v;
int to, from;

vector<int> graph[1001];

int visited[1001];

void DFS(int st)
{
	cout << st << ' ';
	for (int i = 0; i < graph[st].size(); i++)
	{
		int to = graph[st][i];
		if (visited[to])
		{
			continue;
		}

		visited[to] = 1;
		DFS(to);
		
	}
}

void BFS(int st)
{
	queue<int> q;
	q.push(st);
	visited[st] = 1;
	
	while (!q.empty())
	{
		int now = q.front();
		q.pop();
		cout << now << ' ';
		for (int i = 0; i < graph[now].size(); i++)
		{
			int np = graph[now][i];

			if (visited[np])
			{
				continue;
			}
			visited[np] = 1;
			q.push(np);
		}
	}
}

int main()
{
	cin >> n >> m >> v;

	for (int i = 0; i < m; i++)
	{
		cin >> to >> from;
		graph[to].push_back(from);
		graph[from].push_back(to);
	}

	for (int i = 0; i <= n; i++)
	{
		sort(graph[i].begin(), graph[i].end());
	}
	
	visited[v] = 1;
	DFS(v);

	for (int i = 0; i <= n; i++)
	{
		visited[i] = 0;
	}
	cout << '\n';

	BFS(v);
	
}