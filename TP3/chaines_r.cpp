#include <iostream>
#include <string>

using str = std::string;

char sous_chaine(str chaine, int i, int longueur){
    if(longueur == 1){
        return chaine[i];
    }
    return chaine[i] + sous_chaine(chaine, i+1, longueur-1);
}

int main(){
    str chaine = "une phrase";
    std::cout<< sous_chaine(chaine, 4, 4);
}