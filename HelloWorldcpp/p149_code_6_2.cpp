#include <iostream>

using namespace std;
#include <vector>
#include <iostream>
#include <stdio.h>

void printPicked(vector <int> picked){
    cout << "(";
    for(int i=0; i < picked.size(); i++){
        cout << picked[i];
    }
    cout << ")";
}

//n: 전체 원소의 수
//picked: 지금까지 고른 원소들의 번호
//toPick: 더 고를 원소들의 수
//일 때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력한다.
void pick (int n, vector <int> picked, int toPick){
    //기저 사례: 더 고를 원소가 없을 때 고른 원소들을 출력한다.
 if(toPick == 0) {printPicked(picked); return;}
    //고를 수 있는 가장 작은 번호를 계산한다.
 int smallest = picked.empty() ? 0 : picked.back()+1;
//  cout << smallest;
    //이 단계에서 원소를 하나 고른다.
 for(int next = smallest; next < n ; ++next){
     picked.push_back(next);
     pick(n, picked, toPick-1);
     picked.pop_back();
 }
}


int main(){
    vector <int> a = {};
    pick(4, a, 2);

    // printPicked(a);
}

// 알게 된 것.
// #include <vector> 를 해야한다. 이건때문에 여태까지 약간 막혀있었다.
// void는 따로 return이 없는 함수이다 옛날에는 매모리 공간을 아끼려고 이렇게 코딩하는 경우도 있다.

// size() - 벡터의 요소의 개수를 반환한다.
// swap(vector객체) - 두 벡터의 내용을 교환(교체)한다.
// empty() - 벡터가 비었는지 여부를 반환한다.
// at(index) - index번째 요소에 접근한다.
// front() - 벡터의 첫 번째 요소를 반환한다.
// back() - 벡터의 마지막 요소를 반환한다.
// begin() - 벡터의 첫 번째 요소를 가리킨다.
// end() - 벡터의 마지막 요소를 가리킨다.
// push_back(값)

//등이 벡터 연산에 있으며 
//벡터는 원소를 추가 할 수 있다. 파이썬의 리스트가 약간 비슷한거 같다.
// vector는 블록 밖으로 나가거나 return을 만나면 자동으로 delete 되어 메모리를 해제해준다.
// vector는 배열처럼 개별 요소에 접근할 때는 a [i]처럼 사용할 수 있다. 
// 단, 원소를 생성하면서 write는 불가능하다.

//코딩의 태도
//항상 조건을 보며 입력값을 잘 보자.
//멍청하게 picked에 벡터 1,2,3,4 를 넣으면서 값이 왜 안나오지 라는 고민을 했다.