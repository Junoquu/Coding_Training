#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    string odd="",even="";
    for(auto i = num_list.begin();i!=num_list.end();i++){
        if(*i%2==0)
            even+=to_string(*i);
        else
            odd+=to_string(*i);
    }
    return stoi(odd)+stoi(even);
}