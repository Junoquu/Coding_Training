#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

struct Stone
{
	int y;
	int x;
};

int T, N, M;
int y, x, s;
int BCnt, WCnt;

int map[9][9];

int dy[] = { -1,-1,-1, 0,0, 1,1,1 };
int dx[] = { -1, 0, 1,-1,1,-1,0,1 };

void init()
{
	memset(map, 0, sizeof(map));
	BCnt = 0;
	WCnt = 0;
}

void print();
void flipStones(int startY, int startX, int color);
void input();
void calcStone();

void input()
{
	cin >> N >> M;

	map[N / 2][N / 2] = 2;
	map[N / 2][N / 2 + 1] = 1;
	map[N / 2 + 1][N / 2] = 1;
	map[N / 2 + 1][N / 2 + 1] = 2;

	for (int i = 0; i < M; i++)
	{
		//print();
		cin >> y >> x >> s;
		map[y][x] = s;
		flipStones(y, x, s);
	}
}

void print()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cout << map[i][j] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}

void flipStones(int startY, int startX, int color)
{
	for (int dir = 0; dir < 8; ++dir) {
		int ny = startY + dy[dir];
		int nx = startX + dx[dir];
		vector<Stone> toFlip;

		// 상대방 돌 찾기
		while (ny >= 1 && nx >= 1 && ny <= N && nx <= N && map[ny][nx] != 0 && map[ny][nx] != color) {
			toFlip.push_back({ ny, nx });
			ny += dy[dir];
			nx += dx[dir];
		}

		// 자신의 돌을 찾으면 돌 뒤집기
		if (ny >= 1 && nx >= 1 && ny <= N && nx <= N && map[ny][nx] == color) {
			for (int i = 0; i < toFlip.size();i++) {
				map[toFlip[i].y][toFlip[i].x] = color;
			}
		}
	}
}

void calcStone()
{
	BCnt = 0;
	WCnt = 0;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (map[i][j] == 1) BCnt++;
			else if (map[i][j] == 2) WCnt++;
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
		//print();
		calcStone();

		cout << "#" << tc << " " << BCnt << " " << WCnt << '\n';
	}
}
