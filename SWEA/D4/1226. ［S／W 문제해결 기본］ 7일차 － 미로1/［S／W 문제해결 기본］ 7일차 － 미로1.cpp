#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
using namespace std;

struct Point
{
	int y;
	int x;
};

int T;
int map[17][17];
int visited[17][17];

Point st;
Point en;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void init()
{
	memset(visited, 0, sizeof(visited));
}

void input()
{
	for (int i = 0; i < 16; i++)
	{
		string line;
		cin >> line;

		for (int j = 0; j < 16; j++)
		{
			map[i][j] = line[j] - '0';

			if (map[i][j] == 2)
				st = { i,j };
			if (map[i][j] == 3)
				en = { i,j };
		}
	}
}

int BFS()
{
	queue<Point> q;
	q.push({ st.y,st.x });
	visited[st.y][st.x] = 1;

	while (!q.empty())
	{
		Point cp = q.front();
		q.pop();

		if (cp.y == en.y && cp.x == en.x)
		{
			return 1;
		}


		for (int i = 0; i < 4; i++)
		{
			int ny = cp.y + dy[i];
			int nx = cp.x + dx[i];

			if (ny < 0 || nx < 0 || ny >= 16 || nx >= 16 || map[ny][nx]==1)
			{
				continue;
			}

			if (visited[ny][nx]==1)
			{
				continue;
			}

			visited[ny][nx] = 1;
			q.push({ ny,nx });
		}
	}
	return 0;
}

int main()
{
	int num;
	T = 10;

	for (int tc = 1; tc <= T; tc++)
	{
		init();
		cin >> num;
		input();
		cout << "#" << tc << " " << BFS() << '\n';
	}
}