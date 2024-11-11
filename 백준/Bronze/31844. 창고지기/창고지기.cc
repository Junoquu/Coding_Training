#include <iostream>
using namespace std;

struct state
{
	int x;
};

char warehouse[11];
int cnt = 0;

state robot;
state box;
state dist;

int main()
{
	for (int i = 0; i < 10; i++)
	{
		cin >> warehouse[i];
		if (warehouse[i] == '@')
			robot = { i };
		else if (warehouse[i] == '#')
			box = { i };
		else if (warehouse[i] == '!')
			dist = { i };
	}

	if (robot.x < box.x && box.x < dist.x)
	{
		cnt = (box.x - robot.x) + (dist.x - box.x) - 1;
	}
	else if (dist.x < box.x && box.x < robot.x)
	{
		cnt = (box.x - dist.x) - 1 + (robot.x - box.x);
	}
	else
		cnt = -1;
	cout << cnt;
}