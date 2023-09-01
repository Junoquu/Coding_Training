#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> str_list) {
    vector<string> answer;
    for(int i = 0;i<str_list.size();i++){
        if(str_list[i]=="l"){
            for(int n = 0; n<i;n++){
                answer.emplace_back(str_list[n]);
            }
           
            break;
        }
        else if(str_list[i]=="r"){
            for(int m=i+1;m<str_list.size();m++){
                answer.emplace_back(str_list[m]);
            }
            break;
        }
    }
     return answer;
}