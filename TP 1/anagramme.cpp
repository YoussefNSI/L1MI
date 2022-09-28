#include <iostream>
#include <algorithm>
#include <string>

int main(){
    std::string mot;
    std::string mot_2;
    bool anagramme = true;

    std::cout<<"Entrez un mot : ";
    std::cin>> mot;
    std::cout<<"Entrez le deuxième mot : ";
    std::cin>> mot_2;

    if(mot.size() != mot_2.size()){
        std::cout<<"Ce n'est pas un anagramme";
        return false;
    }
    
    for(int i = 0; i < mot.size(); i++){
        char ch = mot[i];
        if(mot_2.find(ch) == std::string::npos){
            anagramme = false;
        }
    }
    
    if(anagramme){
        std::cout<<"C'est un anagramme";
    }
    else{
        std::cout<<"Ce n'est pas un anagramme";
    }
}