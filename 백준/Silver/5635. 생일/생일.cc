#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

struct Students
{
	string name;
	int year;
	int month;
	int day;
};

bool compare(Students a, Students b)
{
	if (a.year != b.year)
	{
		return a.year < b.year;
	}
	else if (a.month != b.month)
	{
		return a.month < b.month;
	}
	else
	{
		return a.day < b.day;
	}
}

vector<Students> stu;

int n;

string name;
int year;
int month;
int day;

int main()
{
	cin >> n;

	stu.resize(n);

	for (int i = 0; i < n; i++)
	{
		cin >> stu[i].name >> stu[i].day >> stu[i].month >> stu[i].year;
	}

	sort(stu.begin(), stu.end(), compare);

	cout << stu[n - 1].name << '\n' << stu[0].name;
}