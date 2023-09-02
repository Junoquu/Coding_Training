#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    string tostring=to_string(age);
    for(int i=0;i<tostring.size();i++){
        answer+=tostring[i]-'0'+'a';
    }
    
    return answer;
}