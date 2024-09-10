#include <iostream>
#include <string>
using namespace std;

string str;
string tar;

int main()
{
	getline(cin, str);
	getline(cin, tar);

	int a = 0;
	int b = 0;
	int cnt = 0;

	while (true)
	{
		int b = str.find(tar, a);
		if (b==string::npos)
		{
			break;
		}
		cnt++;
		a = b + tar.length();
	}

	cout << cnt;
}