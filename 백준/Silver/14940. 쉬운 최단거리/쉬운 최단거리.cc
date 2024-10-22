#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Point
{
	int y;
	int x;
};

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

int n, m;

vector<vector<int>> map;
vector<vector<int>> visited;

void Flood_Fill(Point st)
{
	queue<Point> q;
	//visited[st.y][st.x] = 1;
	q.push(st);

	while (!q.empty())
	{
		Point now = q.front();
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			Point np = { now.y + dy[i], now.x + dx[i] };
			if (np.y < 0 || np.x < 0 || np.y >= n || np.x >= m)
			{
				continue;
			}
			if (visited[np.y][np.x] || map[np.y][np.x] != 1)
			{
				continue;
			}
			visited[np.y][np.x] = visited[now.y][now.x]+1;
			q.push(np);
		}
	}
}

Point st;

int main()
{
	cin >> n >> m;

	map.resize(n, vector<int>(m));
	visited.resize(n, vector<int>(m));

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
			if (map[i][j]==2)
			{
				st = { i,j };
			}
		}
	}

	Flood_Fill(st);
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 1 && visited[i][j] == 0)
			{
				visited[i][j] = -1;
			}
			
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << visited[i][j]<<' ';
		}
		cout << '\n';
	}
}