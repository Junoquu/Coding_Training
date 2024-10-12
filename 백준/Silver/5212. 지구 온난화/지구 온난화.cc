#include <iostream>
#include <vector>
using namespace std;

struct Point
{
	int y;
	int x;
};

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

vector<vector<char>> map;
vector<Point> gnd;

int R, C;

void init()
{
	map.assign(R + 2, vector<char>(C + 2, '.'));
}

void print_map(int y, int x)
{
	for (int i = 1; i <= y; i++)
	{
		for (int j = 1; j <= x; j++)
		{
			cout << map[i][j];
		}
		cout << '\n';
	}
}

int countSea(int y, int x)
{
	int sea_cnt = 0;
	for (int j = 0; j < 4; j++)
	{
		int ny = y + dy[j];
		int nx = x + dx[j];
		if (ny >= 0 && ny <= R + 1 && nx >= 0 && nx <= C + 1 && map[ny][nx] == '.')
		{
			sea_cnt++;
		}
	}
	return sea_cnt;
}

int main()
{
	cin >> R >> C;
	init();

	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 'X')
			{
				gnd.push_back({ i, j });
			}
		}
	}

	vector<Point> seaed;
	for (const auto &p : gnd)
	{
		if (countSea(p.y, p.x) >= 3)
		{
			seaed.push_back(p);
		}
	}

	for (const auto &p : seaed)
	{
		map[p.y][p.x] = '.';
	}

	int imin = R, imax = 1, jmin = C, jmax = 1;
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			if (map[i][j] == 'X')
			{
				if (i < imin) imin = i;
				if (i > imax) imax = i;
				if (j < jmin) jmin = j;
				if (j > jmax) jmax = j;
			}
		}
	}

	for (int i = imin; i <= imax; i++)
	{
		for (int j = jmin; j <= jmax; j++)
		{
			cout << map[i][j];
		}
		cout << '\n';
	}

	return 0;
}