#include <iostream>
#include <fstream>
#include <string>

//std::ifstream (lecture) std::ofstream (ecriture)
//std::isspace(c)

void detail_txt(std::string fichier){
    std::ifstream fic(fichier);
    int nb_ligne = 0;
    int nb_c = 0;
    std::string ch;
    char c;
    while(std::getline(fic, ch))
    {
        nb_ligne += 1;

        if(not std::isspace(c))
            nb_c += 1;
        
    }
    std::cout << "Il y à " << nb_c << " caractères et " << nb_ligne << " lignes.";
}

int main(){
    std::string fichier = "fichier_1/fic3.txt";
    detail_txt(fichier);
}

