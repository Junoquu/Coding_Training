#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    stack<char> st;
    for(int i = 0;i<s.size();i++){
        if(s[i]=='('){
            st.push(s[i]);
        }
        else if(s[i]==')'){
            if(st.size()==0)
                st.push(s[i]);
            else{
                if(st.top()=='(')
                    st.pop();
                else
                    st.push(s[i]);
            }
        }
    }
    if(!st.empty())
        answer = false;
    
    // // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // while(!st.empty()){
    //     cout<<st.top();
    //     st.pop();
    // }

    return answer;
}