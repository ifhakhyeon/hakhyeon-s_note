#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int a;
    cout << "typing your number";
    cin >> a;
    switch (a)
    {
        case 1:
            cout << "your number is 1." << endl;
            break;

        case 2:
            cout << "your number is 2." << endl;
            break;

        case 3:
            cout << "your number is 3." << endl;
            break;

        case 4:
            cout << "your number is 4." << endl;
            break;

        case 5:
            cout << "your number is 5." << endl;
            break;

        default:
            cout << "Type num 1 to 5!" << endl;
            break;

    }

    system("pause");
    // 콘솔창이 닫히지 않도록 유지..
}