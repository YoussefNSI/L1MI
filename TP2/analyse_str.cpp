#include <iostream>
#include <string>

using str = std::string;

void saisie(str & chaine){
    std::cout<< "Saisissez une chaîne composée seulement de X et O\n";
    std::cin>> chaine;
}

int nb_x(str chaine){
    int taille = chaine.length();
    int nb = 0;
    for(int i = 0; i <= taille; i++){
        if(chaine[i] == 'X'){
            nb += 1;
        }
    }
    return nb;
}

str chaine_o(str chaine){
    str chaine_o = "";
    int taille = chaine.length();
    for(int i = 0; i <= taille; i++){
        if(chaine[i] != 'X'){
            chaine_o += 'O';
        }
    }
    return chaine_o;
}

str chaine_trie(str m){
    str chaine_trie = "";
    int nbx = nb_x(m);
    for(int i = 0; i <= nbx; i++){
        chaine_trie += 'X';
    }
    chaine_trie = chaine_trie + chaine_o(m);
    return chaine_trie;
}

int main(){
    str chaine;
    saisie(chaine);
    std::cout<< "Chaine sans X : " << chaine_o(chaine) << "\n";
    std::cout<< "nb de X dans chaine : " << nb_x(chaine) << "\n";
    std::cout<< "Chaine triée : " << chaine_trie(chaine) << "\n";

}