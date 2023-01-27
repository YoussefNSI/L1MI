#include <iostream>
#include <string>
#include <array>

const int N_max = 100;

struct lecteur{
    int id;
    std::string nom;
    std::string prenom;
};

struct enslecteurs{
    int nb_l;
    std::array<lecteur, N_max> tab_lecteurs;
};

struct livre{
    int isbn;
    std::string titre, nom_auteur, nom_emprunt;
    bool emprunt;
};

struct enslivre{
    std::array<livre, N_max> ensL;
};

struct biblio{
    enslivre ensL;
};

void saisie(lecteur l){
    std::cout<< "Entrez le numéro de lecteur";
    std::cin>> l.id;
    std::cout<< "Entrez le nom et prénom du lecteur";
    std::cin>> l.nom, l.prenom;
}

void affiche(lecteur l){
    std::cout<<"Numéro de lecteur : " << l.id << ", Nom Prénom : " << l.nom <<\
     " " << l.prenom;
}

void init_tab(enslecteurs ens){
    lecteur l;
    for(int i = 0; i <= N_max; i++)
        ens.tab_lecteurs[i] = l;
}

void ajoute(enslecteurs ens, lecteur l){
    if(ens.nb_l != N_max){
        ens.tab_lecteurs[ens.nb_l] = l;
        ens.nb_l += 1;
    }
}

void saisietous(enslecteurs ens){
    int max;
    std::cout<< "Combien de lecteurs voulez vous ajouter ? (max : " << N_max <<")";
    std::cin>> max;
    for(int i = 0; i < max; i++){
        lecteur l;
        saisie(l);
        ajoute(ens, l);
    }
}

void affichetous(enslecteurs ens){
    for(int i = 0; i < ens.nb_l; i++){
        std::cout<< i+1 << " : nb_lecteur = " << ens.tab_lecteurs[i].id << ", nom prénom : " \
        << ens.tab_lecteurs[i].nom << " " << ens.tab_lecteurs[i].prenom << "\n";
    }
}

std::string rechercheNom(enslecteurs ens, int nb){
    std::string nom_lecteur = "None";
    for(int i = 0; i <= ens.nb_l; i++){
        if(nb == ens.tab_lecteurs[i].id)
            nom_lecteur = ens.tab_lecteurs[i].nom;
    }
    return nom_lecteur;
}

int main(){
    enslecteurs ens;
    init_tab(ens);
    saisietous(ens);
    affichetous(ens);
    rechercheNom(ens, 10);
}

