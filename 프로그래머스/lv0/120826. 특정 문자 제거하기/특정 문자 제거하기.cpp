#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    for(int i=0;i<my_string.size();i++){
        string str(1,my_string[i]);
        if(str!=letter)
            answer+=my_string[i];
    }
    return answer;
}