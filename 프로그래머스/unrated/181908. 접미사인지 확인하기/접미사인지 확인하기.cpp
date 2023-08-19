#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_suffix) {
    int answer = 0;
    vector<string>str;
    for(int i=0;i<my_string.size();i++){
        str.emplace_back(my_string.substr(i,my_string.size()-i));
    }
    for(int i=0;i<str.size();i++){
        if(str[i]==is_suffix){
            answer=1;
        }
    }
    return answer;
}