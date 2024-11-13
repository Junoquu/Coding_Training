#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

#define MAX 100000

int n;
string id;
int cnt = 0;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	unordered_set<string> s;
	
	cin >> n;

	while(n--)
	{
		cin >> id;
		if (id == "ENTER")
		{
			cnt += s.size();
			s.clear();
			continue;
		}
		s.insert(id);
	}

	cnt += s.size();

	cout << cnt;
}