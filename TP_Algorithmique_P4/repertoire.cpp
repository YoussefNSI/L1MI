#include <iostream>

struct personne
{
    std::string nom;
    std::string prenom;
    std::string tel;
};


struct maillon
{
personne val;
maillon * suiv;
};

using repertoire = maillon *;

void initialiserRepertoire(repertoire & R){
    
}