#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Point
{
	int y;
	int x;
};

int T;

int N;
vector<vector<char>> map;

int Q;
int len;
vector<string> commands;

int dy[4] = { -1, 0, 1,  0 };
int dx[4] = {  0, 1, 0, -1 };


Point sp;
Point tp;

vector<int> check_target;

void input()
{
	cin >> N;

	map.resize(N, vector<char>(N));

	char map_input;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map_input;
			map[i][j] = map_input;
			if (map_input == 'X')
				sp = { i,j };
			else if (map_input == 'Y')
				tp = { i,j };
		}
	}

	cin >> Q;
	commands.resize(Q);
	for (int i = 0; i < Q; i++)
	{
		cin >> len;
		cin >> commands[i];
	}
}

void check_input()
{
	for (int i = 0; i < map.size(); i++)
	{
		for (int j = 0; j < map[i].size(); j++)
		{
			cout << map[i][j];
		}
		cout << '\n';
	}

	for (int i = 0; i < commands.size(); i++)
	{
		for (int j = 0; j < commands[i].size(); j++)
		{
			cout << commands[i][j];
		}
		cout << '\n';
	}

	cout << sp.y << sp.x << '\n';
	cout << tp.y << tp.x << '\n';
}

void solve()
{
	for (int i = 0; i < commands.size(); i++)
	{
		if (i==2)
		{
			int deg = 1;
		}
		int cy = sp.y;
		int cx = sp.x;

		Point np;
		np.y = cy;
		np.x = cx;
		int dir_idx = 0;

		for (int j = 0; j < commands[i].size(); j++)
		{

			if (commands[i][j] == 'A')
            {
                if (np.y + dy[dir_idx] < 0 || np.x + dx[dir_idx] < 0 ||
                    np.y + dy[dir_idx] >= N || np.x + dx[dir_idx] >= N || 
                    map[np.y + dy[dir_idx]][np.x + dx[dir_idx]] == 'T')
                {
                    continue;
                }
                np.y += dy[dir_idx];
                np.x += dx[dir_idx];
            }
			else if (commands[i][j] == 'R')
			{
				dir_idx = (dir_idx + 1) % 4;
			}
			else if (commands[i][j] == 'L')
			{
				dir_idx = (dir_idx + 3) % 4;
			}
		}
		if (np.y == tp.y && np.x == tp.x)
			check_target.push_back(1);
		else
			check_target.push_back(0);
	}
}

int main() {

	//freopen("sample_input.txt", "r", stdin);

	cin >> T;

	for (int tc = 1; tc <= T; tc++)
	{
		input();
		 check_target.clear();
		solve();

		cout << "#" << tc << " ";
		for (int i = 0; i < check_target.size(); i++)
		{
			 cout<<check_target[i]<<" ";
		}
		cout<<'\n';
	}
}
