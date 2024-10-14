#include <iostream>
#include <string>
using namespace std;

string s, t;
int s_len, t_len;
bool flag;

int main()
{
	while (cin >> s >> t)
	{
		flag = true;
		int pos = 0;

		for (int i = 0; i < s.size(); i++)
		{
			pos = t.find(s[i], pos);
			if (pos != string::npos)
			{
				pos++;
			}
			else
			{
				flag = false;
				break;
			}
		}
		if (flag)
			cout << "Yes\n";
		else
			cout << "No\n";
	}
}