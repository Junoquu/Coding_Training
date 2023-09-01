#include <string>
#include <vector>

using namespace std;

int max(int a,int b){
    return a>b?a:b;
}

int solution(vector<int> num_list) {
    int answer = 0;
    int even=0,odd=0;
    for(int i=0;i<num_list.size();i++){
        if(i%2==0){
            even+=num_list[i];
        }
        else
            odd+=num_list[i];
    }
    if(even!=odd)
        answer=max(even,odd);
    else
        answer=even;
    return answer;
}