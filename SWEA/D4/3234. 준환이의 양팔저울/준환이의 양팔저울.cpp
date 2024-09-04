#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

int T, N;
int arr[10];
int visited[10];
int leftArr[10];
int rightArr[10];
int sum = 0;
int cnt = 0;

void init()
{
	memset(arr, 0, sizeof(arr));
	memset(visited, 0, sizeof(visited));
	memset(leftArr, 0, sizeof(leftArr));
	memset(rightArr, 0, sizeof(rightArr));
	cnt = 0;
	sum = 0;
}

void input()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
		sum += arr[i];
	}
}

void recur(int lev, int leftSum, int rightSum)
{
	if (lev == N)
	{
		cnt++;
		return;
	}

	if (leftSum >= sum-leftSum)
	{
		int remain = N - lev;
		int permutations = 1;

		for (int i = 1; i <= remain; i++)
		{
			permutations = permutations * 2 * i;
		}

		cnt += permutations;
		return;
	}

	for (int i = 0; i < N; i++)
	{
		if (visited[i])
		{
			continue;
		}

		visited[i] = 1;

		// 왼쪽 배열에 추가
		leftArr[lev] = arr[i];

		recur(lev + 1, leftSum + arr[i], rightSum);

		// 오른쪽 배열에 추가 (단, 조건을 만족하는 경우만)
		if (rightSum + arr[i] <= leftSum)
		{

			rightArr[lev] = arr[i];
			recur(lev + 1, leftSum, rightSum + arr[i]);
		}

		// 방문 해제 및 초기화
		visited[i] = 0;
	}
}


void solve()
{
	recur(0, 0, 0);
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

		cout << "#" << tc << " " << cnt << '\n';
	}
}