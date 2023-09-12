#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    
    for(int i=0;i<strArr.size();i++){
        string newString="";
        if(i%2==0){
            for(char c:strArr[i]){
                newString+=tolower(c);
            }
            answer.emplace_back(newString);
        }
        else{
            for(char c:strArr[i]){
                newString+=toupper(c);
            }
            answer.emplace_back(newString);
        }
    }
    return answer;
}