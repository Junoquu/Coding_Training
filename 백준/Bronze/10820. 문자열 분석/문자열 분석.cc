#include <iostream>
#include <string>
using namespace std;

string str;

int main()
{
	while (getline(cin,str))
	{
		int upper = 0, lower = 0, digit = 0, space = 0;
		for (int i = 0; i < str.length(); i++)
		{
			if (str[i] >= 'A' && str[i] <= 'Z')
			{
				upper++;
			}
			else if (str[i] >= 'a' && str[i] <= 'z')
			{
				lower++;
			}
			else if (str[i] >= '0' && str[i] <= '9')
			{
				digit++;
			}
			else
			{
				space++;
			}
		}
		cout << lower << " " << upper << " " << digit << " " << space << '\n';
	}
	
}