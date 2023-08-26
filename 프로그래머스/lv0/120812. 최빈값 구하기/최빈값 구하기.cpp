#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    vector<int> many(1000);
    int max = 0;
    int max_idx = 0;
    
    for(int i=0;i<array.size();i++){
        many[array[i]]++;
    }
    for (int i = 0;i<many.size();i++){
		if(many[i]>max){
            max = many[i];
            max_idx = i;
        }
	}
    int cnt = 0;
    for(auto i = many.begin();i!=many.end();i++){
        if(*i == max)
            cnt++;
    }
    if(cnt>1)
        return -1;
    answer = max_idx;
    return answer;
}