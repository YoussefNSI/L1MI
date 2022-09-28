#include <iostream>
#include <algorithm>

int main(){

    int i1, i2;
    bool palindrome;
    std::string str;
    std::cout<<"Entrez un mot";
    std::getline(std::cin, str);
    i1 = 0;
    i2 = str.size()-1;
    palindrome = true;
    while(i1 <= str.size() - 1 or i2 >= 0){
        if(str[i1] == ' '){
            i1 += 1;
        }
        if(str[i2] == ' '){
            i2 -= 1;
        }
            if(str[i1] != str[i2]){
                palindrome = false;
                std::cout<< "str 1 " << str[i1] << " i1 : " << i1 << "\n";
                std::cout<< "str 2 " << str[i2] << " i2 : " << i2 << "\n";
            }
        i1 += 1;
        i2 -= 1;
    }
    if(palindrome){std::cout<<"C'est un palindrome";}
    else{std::cout<<"Ce n'est pas un palindrome";}
}