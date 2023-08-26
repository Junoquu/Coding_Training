#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    for(int pizza=1;pizza<=n;pizza++){
        if((pizza*6)%n==0){
            return pizza;
        }
    }
}