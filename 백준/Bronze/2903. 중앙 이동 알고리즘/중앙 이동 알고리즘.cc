#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

int N;
int ans;
int init_state = 2;
int dp[16];

void init()
{
	memset(dp, -1, sizeof(dp));
	ans = 0;
}

void input()
{
	cin >> N;
}

int dp_func(int n) {
	if (n == 1)
		return 3;
	if (n == 2)
		return 5;
	if (dp[n] != -1)
		return dp[n];
	return dp[n] = dp_func(n - 1) * 2 - 1;
}

void solve()
{
	ans = dp_func(N)*dp_func(N);
}

int main()
{
	init();
	input();
	solve();

	cout << ans;

	return 0;
}