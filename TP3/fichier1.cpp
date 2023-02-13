#include <iostream>
#include <fstream>
#include <string>

//std::ifstream (lecture) std::ofstream (écriture)

bool fichier_identique_gt(std::string fichier1, std::string fichier2){
    std::ifstream fic1(fichier1);
    std::ifstream fic2(fichier2);
    std::string ch1, ch2;
    bool identique = true;
    while((not fic1.eof() or not fic2.eof()) and identique){
        std::getline(fic1, ch1);
        std::getline(fic2, ch2);
        if(ch1 != ch2) identique = false;
    }
    return identique;
}

bool fichier_identique_get(std::string fichier1, std::string fichier2){
    std::ifstream fic1(fichier1);
    std::ifstream fic2(fichier2);
    char ch1, ch2;
    bool identique = true;
    while((not fic1.eof() or not fic2.eof()) and identique){
        fic1.get(ch1);
        fic2.get(ch2);
        if(ch1 != ch2) identique = false;
    }
    return identique;
}

bool fichier_identique_op(std::string fichier1, std::string fichier2){
    std::ifstream fic1(fichier1);
    std::ifstream fic2(fichier2);
    char ch1, ch2;
    bool identique = true;
    while((not fic1.eof() or not fic2.eof()) and identique){
        fic1 >> ch1;
        fic2 >> ch2;
        if(ch1 != ch2) identique = false;
    }
    return identique;
}

int main(){
    std::string fichier1 = "fichier_1/fic1.txt";
    std::string fichier2 = "fichier_1/fic2.txt";
    std::string fichier3 = "fichier_1/fic3.txt";

    std::cout<< "premier programme : " << fichier_identique_gt(fichier1, fichier2) << "\n";
    std::cout<< "deuxieme programme : " << fichier_identique_get(fichier1, fichier2) << "\n";
    std::cout<< "troisieme programme : " << fichier_identique_op(fichier1, fichier2) << "\n";
}

