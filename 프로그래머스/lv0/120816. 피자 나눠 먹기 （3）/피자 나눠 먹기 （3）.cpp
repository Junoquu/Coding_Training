#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    for(int pizza = 1 ; pizza <= 100;pizza++){
        if((slice*pizza) >= n)
            return pizza;
    }
}