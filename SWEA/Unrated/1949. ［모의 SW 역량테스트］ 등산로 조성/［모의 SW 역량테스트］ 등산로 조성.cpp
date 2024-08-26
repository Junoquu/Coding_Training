#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring> 
#include <vector>
#include <algorithm>
using namespace std;

struct Point
{
	int y;
	int x;
};

int T;
int N, K;
int maxDir;
int map[9][9];
int visited[9][9];
int peak = 0;
vector<Point> peaks;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void init()
{
	memset(map, 0, sizeof(map));
	memset(visited, 0, sizeof(visited));
	peaks.clear();
	maxDir = 0;
	peak = 0;
}

void input()
{
	cin >> N >> K;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
			if (peak<map[i][j])
			{
				peak = map[i][j];
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j]==peak)
			{
				visited[i][j] = 1;
				peaks.push_back({ i,j });
			}
		}
	}
}

void print(Point cp)
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (cp.y == i && cp.x == j)
				cout << '@' << ' ';
			else
				cout << map[i][j] << ' ';
		}
		cout << '\n';
	}
	cout << '\n';
}

void dfs(Point cp, int dir)
{
	if (dir>maxDir)
	{
		maxDir = dir;
	}
	// 더이상 낮은게 없을 경우 && 지형 깎는 공사를 했을 경우
	//print(cp);
	for (int i = 0; i < 4; i++)
	{
		int ny = cp.y + dy[i];
		int nx = cp.x + dx[i];

		if (ny<0 || nx<0 || ny>=N || nx >= N)
		{
			continue;
		}

		if (visited[ny][nx])
		{
			continue;
		}


		if (map[ny][nx]<map[cp.y][cp.x])
		{
			dfs({ ny,nx },dir+1);
		}
	}
}

void make_road()
{
	int y, x;
	for (int i = 0; i < peaks.size(); i++)
	{
		if (map[peaks[i].y][peaks[i].x]==peak)
		{
			visited[peaks[i].y][peaks[i].x] = 1;
			dfs({ peaks[i].y,peaks[i].x }, 1);
			visited[peaks[i].y][peaks[i].x] = 0;
		}
	}
}

void solve()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			for (int k = 1; k <= K; k++)
			{
				map[i][j] -= k;
				make_road();
				map[i][j] += k;
			}
		}
	}
}

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	cin >> T;

	for (int tc = 1; tc <= T; tc++)
	{
		init();
		input();
		solve();

		cout << "#" << tc << " " << maxDir << '\n';
	}
}