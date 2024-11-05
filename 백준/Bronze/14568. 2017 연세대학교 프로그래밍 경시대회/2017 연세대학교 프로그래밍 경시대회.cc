#include <iostream>
using namespace std;

int main()
{
	int candy;
	cin >> candy;

	int answer = 0;

	for (int A = 1; A < candy + 1; A++)
	{
		for (int B = 1; B < candy + 1; B++)
		{
			for (int C = 1; C < candy + 1; C++)
			{
				if (A + B + C == candy)
				{
					if (A >= B + 2)
					{
						if (C % 2 == 0)
						{
							answer++;
						}
					}
				}
			}
		}
	}
	cout << answer;
}