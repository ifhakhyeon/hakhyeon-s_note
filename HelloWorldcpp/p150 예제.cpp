// #include <iostream>

// using namespace std;
// #include <vector>
// #include <iostream>
// #include <stdio.h>
// #include <array>
// #include <string.h>

// // vector <string> boggle 
// string boggle[5][5] = {
//     {"N","N","N","N","S"},
//     {"N","E","E","E","N"},
//     {"N","E","Y","E","N"},
//     {"N","E","E","E","N"},
//     {"N","N","N","N","S"}
//     };


// int main(){
//     int move[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    
//     //const char* 은 메모리에 첫요소가 문자열을 할달할 수 있도록 하는 변수선언
//     // const char* boggle[5][5] = {
//     //     {"N","N","N","N","S"},
//     //     {"N","E","E","E","N"},
//     //     {"N","E","Y","E","N"},
//     //     {"N","E","E","E","N"},
//     //     {"N","N","N","N","S"}
//     //     };

// }

// bool hasWord(int y, int x, const string str) {
//     if(!(0 <= y <=4 && 0<= x <=4)){
//         return false;
//     }

//     if(boggle[y][x] != str[0]){
//         return false;
//     }

//     if(str.size() == 1){
//         return true;
//     }
// }

// input 값을 고려안해서 보류