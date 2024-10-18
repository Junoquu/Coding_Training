#include <iostream>
#include <vector>
#include <string>
using namespace std;

string encrypted_cmd;
int n;
string str;
vector<string> parametor;

string decrypted_cmd(string cmd, int key)
{
	string decrypted_str; // 제대로 정의된 변수명 사용
	for (char c : cmd)
	{
		// 'a'로부터의 인덱스를 구해 key를 빼서 암호 해독
		char decrypted_char = (c - 'a' - key + 26) % 26 + 'a';
		decrypted_str += decrypted_char; // 문자열에 추가
	}
	return decrypted_str;
}

int main()
{
	cin >> encrypted_cmd;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> str;
		parametor.push_back(str);
	}

	string comp;
	bool flag = false;

	for (int i = 0; i < 27; i++)
	{
		comp = decrypted_cmd(encrypted_cmd, i);
		for (int i = 0; i < parametor.size(); i++)
		{
			if (comp.find(parametor[i])!=string::npos)
			{
				flag = true;
				break;
			}
		}
		if (flag)
		{
			cout << comp;
			break;
		}
	}
}