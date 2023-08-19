#include <string>
#include <vector>

using namespace std;

int GCD(int a,int b){
    if(b==0) return a;
    return GCD(b,a%b);
}

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    
    int numer=(numer1*denom2+numer2*denom1);
    int denom=(denom1*denom2);
    
    int gcd=GCD(numer,denom);
    
    answer.emplace_back(numer/gcd);
    answer.emplace_back(denom/gcd);
    
    return answer;
}