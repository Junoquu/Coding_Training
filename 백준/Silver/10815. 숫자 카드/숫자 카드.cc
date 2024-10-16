#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int input;
int card;
int n, m;

vector<int> DAT;
vector<int> Binary_Search_Nums;

bool binary_search(vector<int>& arr, int len, int tar)
{
	int low = 0;
	int high = len - 1;
	while (low <= high)
	{
		int mid = (low + high) / 2;

		if (tar == arr[mid])
		{
			return true;
		}

		if (tar < arr[mid])
		{
			high = mid - 1;
		}

		else if (tar > arr[mid])
		{
			low = mid + 1;
		}
	}
	return false;
}


int main()
{
	cin.tie(nullptr);
	ios_base::sync_with_stdio(false);

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> input;
		DAT.push_back(input);
	}

	sort(DAT.begin(), DAT.end());

	cin >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> card;
		Binary_Search_Nums.push_back(card);
	}

	for (int i = 0; i < Binary_Search_Nums.size(); i++)
	{
		if (binary_search(DAT, DAT.size(), Binary_Search_Nums[i]))
			cout<<1<<' ';
		else
			cout<<0<<' ';
	}
}