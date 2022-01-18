#include <iostream>
#include <stdio.h>
using namespace std;


int main()
{
     int a[1] = {3};
     int b[2] = {1,3};
     int c[1] = {2};
     // int IntergerSet[3] = {1,2,3};

     // 비트 연산자


     // a가 b의 진부분집합이면 true, 아니면 false를 반환한다.
     bool isProperSubset(const IntegerSet& a, const IntegerSet& b);
    
     //a가 b의 진부분집합일 때 a가 항상 앞에 오도록 집합들을 정렬한다.
     bool operator < (const IntegerSet& a, const IntegerSet& b) {
          //a가 b의 진부분집합이면 a가 앞에 와야 한다.
          if(isProperSubset(a,b)) return true;
          //b가 a의 진부분집합이면 b가앞에 와야한다.
          if(isProperSubset(b,a)) return false;
          //a와 b의 크기가 다르다면 작은 쪽이 앞에 와야 한다.
          if(a.size() != b.size()) return a.size() < b.size();
          //a와 b를 사전순으로 비교해 반환한다.
          return lexicographical_compare(a.begin(), a.end(), b.begin(), b.end());
     }
}

//씨발 이거 안되는거잖아 개새들아..