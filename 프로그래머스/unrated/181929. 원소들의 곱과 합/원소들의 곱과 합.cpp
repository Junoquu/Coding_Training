#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int mt=1,sum=0;
    for(auto i = num_list.begin(); i!=num_list.end();i++){
        mt*=*i;
        sum+=*i;
    }
    return mt>sum*sum?0:1;
}