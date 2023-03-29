#include <iostream>
#include <string>

using str = std::string;

char sous_chaine(str chaine, int i, int longueur){
    if(longueur == 1){
        return chaine[i];
    }
    else{
        return chaine[i] + sous_chaine(chaine, i+1, longueur-1);
    }
}

bool est_palindrome(str chaine, int i=0, int j=chaine.length()){
    ;
}

int main(){
    str chaine = "une phrase";
    std::cout<< sous_chaine(chaine, 4, 4);
}