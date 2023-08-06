#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    for(auto i = arr.begin();i!=arr.end();i++)
        answer.emplace_back(*i);
    for(int i=0;i<queries.size();i++){
        int tmp;
        tmp=answer[queries[i].front()];
        answer[queries[i].front()] = answer[queries[i].back()];
        answer[queries[i].back()] = tmp;
    }
    return answer;
}