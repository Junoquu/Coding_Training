#include <iostream>
#include <string>
#include <queue>
using namespace std;

struct Point
{
	int y;
	int x;
};

int n, m, cnt = 0;
int minCnt = 21e8;
int map[101][101];
int visited[101][101];
int dy[4] = { -1,0,1,0 };
int dx[4] = { 0,1,0,-1 };

void bfs(int y, int x)
{
	queue<Point> q;
	visited[y][x] = 1;
	q.push({ y,x });

	while (!q.empty())
	{
		int cy = q.front().y;
		int cx = q.front().x;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int ny = cy + dy[i];
			int nx = cx + dx[i];

			if (ny<0||nx<0||ny>=n||nx>=m || map[ny][nx]==0)
			{
				continue;
			}

			if (visited[ny][nx])
			{
				continue;
			}
			visited[ny][nx] = visited[cy][cx] + 1;
			q.push({ ny,nx });
		}
	}
}
int main()
{
	string line;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> line;
		for (int j = 0; j < m; j++)
		{
			map[i][j] = line[j]-'0';
		}
	}

	bfs(0, 0);

	cout << visited[n - 1][m - 1];
}