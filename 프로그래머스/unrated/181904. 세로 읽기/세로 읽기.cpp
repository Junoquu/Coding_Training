#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int m, int c) {
    string answer = "";
    vector<string>str;
    for (int i = 0; i < my_string.size(); i+=m)
        str.emplace_back(my_string.substr(i, m));
    for (int i = 0; i < str.size(); i++) {
        answer += str[i][c-1];
    }
    return answer;
}