#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numLog) {
    string answer = "";
    for(int i = 0;i<numLog.size();i++){
        if(i+1!=numLog.size() && numLog[i+1]-numLog[i]==1)
            answer += 'w';
        else if(i+1!=numLog.size() && numLog[i+1]-numLog[i]==-1)
            answer += 's';
        else if(i+1!=numLog.size() && numLog[i+1]-numLog[i]==10)
            answer += 'd';
        else if(i+1!=numLog.size() && numLog[i+1]-numLog[i]==-10)
            answer += 'a';
            
    }
    return answer;
}