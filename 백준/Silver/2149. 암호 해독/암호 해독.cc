#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Com
{
	char cmd;
	int idx;
};

bool cmp(Com a, Com b)
{
	return a.cmd < b.cmd;
}

string cmd;
string code;

vector<Com> v;

int main()
{
	cin >> cmd;
	cin >> code;

	for (int i = 0; i < cmd.size(); i++)
	{
		v.push_back({ cmd[i], i });
	}

	sort(v.begin(), v.end(), cmp);

	vector<string> res(cmd.size());
	int len = code.size() / cmd.size();

	for (int i = 0; i < cmd.size(); i++)
	{
		res[i] = code.substr(i * len, len);
	}

	vector<string> plain(cmd.size());

	for (int i = 0; i < v.size(); i++)
	{
		plain[v[i].idx] = res[i];
	}

	for (int row = 0; row < len; row++)
	{
		for (int col = 0; col < cmd.size(); col++)
		{
			cout << plain[col][row];
		}
	}
	cout << '\n';

	return 0;
}
