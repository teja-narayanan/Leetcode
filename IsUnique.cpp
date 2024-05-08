/*
*
* Cracking the coding interview
* 1.1 IsUnique
* Implement an algorithm to determine if a string has all unique characters.
*
*/
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

void isUnique(string s){
    sort(s.begin(), s.end());
    bool flag = true;
    for(int i = 0; i < s.size() - 1; i++){
        if(s[i] != s[i + 1]){
            flag = false;
        }
    }

    if(flag){
        cout << "True" << endl;
    }
    else{
        cout << "False" << endl;
    }
}

int main(){
    isUnique("aaaaaaa");

    return 0;
}