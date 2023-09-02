#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool desc(int a,int b){
    return a>b;
}
vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> emer=emergency;
    
    sort(emer.begin(),emer.end(),desc);
    
    for(int i=0;i<emergency.size();i++){
        int j=0;
        while(1){
            if(emergency[i]==emer[j]){
                answer.emplace_back(j+1);
                break;
            }
            j++;
        }
    }
    
    return answer;
}