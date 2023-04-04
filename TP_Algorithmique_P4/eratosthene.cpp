#include <iostream>

struct maillon {
    int nb;
    maillon * suiv;
};

using era = maillon *;

void inserer(era & E, int nb){
    era aux = new maillon;
    aux->nb = nb;
    aux->suiv = E;
    E = aux;
    std::cout << "Insertion de " << nb << "\n";
}

void init_era(era & E, int n){
    E = nullptr;
    for (int i = 1; i <= n; i++)
    {
        inserer(E, i);
    }
}

void supprimer(era & E){
    era aux;
    aux = E;
    E = E->suiv;
    delete aux;
}



void afficher_liste(era E){
    if(E != nullptr){
        std::cout<< E->nb << "\n";
        afficher_liste(E->suiv);
    }
}

void eratosthene(era & E, int n){
    init_era(E, n);

    for(int i = 2; i <= n ; i++){
        era p = E;
        while(p != nullptr and p->nb < i*i) {
            p = p->suiv;
        }
        while(p != nullptr and p->nb % i == 0) {
            era tmp = p;
            p = p->suiv;
            supprimer(tmp);
        }
    }
}


int main(){
    era E;
    eratosthene(E, 20);
    afficher_liste(E);
}