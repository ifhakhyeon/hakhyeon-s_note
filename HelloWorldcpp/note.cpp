#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    double a = 10;
    double b = 10;
    

    cout << abs(a-b < 1e-10);

    // return 으로만은 값이 출력 x 파이썬도 동일하잖어..

    const char* str = "asdasd";

    // c++ 에서도 이리 호출이 가능하군..
    cout << str[1];

    string boggle[5][5] = {
    {"N","N","N","N","S"},
    {"N","E","E","E","N"},
    {"N","E","Y","E","N"},
    {"N","E","E","E","N"},
    {"N","N","N","N","S"}
    };

    cout << boggle[0][0];

    string str_1 = {"NYE"};

    string COM1 = boggle[0][0]; 
    // string COM2 = str_1[0];

    string str_2[1] = {"yes"};
    cout << str_2[0][1];
    cout << "d"<<str_2[0];
    
}
