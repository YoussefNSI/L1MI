#include <iostream>
#include <algorithm>
#include <cstdlib>

int main(){
    std::string mot;
    std::string proposition;
    bool trouver;
    int essai = 0;

    std::cout<< "Entrez le mot à deviner:";
    std::getline(std::cin, mot);
    std::system("CLS");

    std::string underscore(mot.size(), '_');
    for(int i = 0; i < mot.size(); i++){
        if(mot[i] == ' ')underscore[i] = ' ';
    }

    while(not trouver){
        essai += 1;
        std::cout<< underscore << "\n";
        std::cout<<"Proposez une lettre ou un mot: ";
        std::getline(std::cin, proposition);
        if(proposition.size() == 1){
            trouver = true;
            for(int i = 0; i < mot.size(); i++){
                if(proposition[0] == mot[i]){
                    underscore[i] = proposition[0];
                }
                if(underscore[i] == '_'){
                    trouver = false;
                }
            }
        }
        else{
            if(mot == proposition){
                trouver=true;
            }
            else{
                std::cout<<"Ce n'est pas ce mot\n";
            }
        }
    
    }

    std::cout<< "Bravo après " << essai << "essai(s)";
    return 0;
}