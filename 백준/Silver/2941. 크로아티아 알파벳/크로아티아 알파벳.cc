#include <iostream>
#include <string>
using namespace std;

string croatia[] = { "c=","c-","dz=","d-","lj","nj","s=","z=" };
string str;
int cnt = 0;

int main()
{
	int tar=0;
	string tmp;

	getline(cin, str);

	for (int i = 0; i < 8; i++)
	{
		int pos = 0;
		while ((pos = str.find(croatia[i],pos)) != string::npos)
		{
			str.replace(pos, croatia[i].length(), "#");
		}
	}
	cout << str.size();
}