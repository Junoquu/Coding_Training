#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int DAT[26] = { -1 };

string str;

int main()
{
	getline(cin, str);
	memset(DAT, -1, sizeof(DAT));
	for (int i = 0; i < str.size(); i++)
	{
		DAT[str[i] - 'a'] = str.find(str[i]);
	}

	for (int i = 0; i < 26; i++)
	{
		cout << DAT[i] << ' ';
	}
}