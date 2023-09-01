#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer=arr;
    for(int i=0;i<queries.size();i++){
        for(int j=queries[i].front();j<=queries[i].back();j++){
            answer[j]++;
        }
    }
    return answer;
}