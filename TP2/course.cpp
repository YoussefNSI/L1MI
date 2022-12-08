#include <iostream>
#include <array>

const int N = 5;
using Dossard = std::array<int, N>;
using Temps = std::array<float, N>;

void init(Dossard & dos, Temps & tps, int n){
    for(int i = 0; i < n; i++){
        dos[i] = 0;
        tps[i] = 0;
    }
}

bool present(Dossard dos, int num, int n){
    bool est_present = false;
    int i = 0;
    //je fais un for ici car j'avais des erreurs
    //avec le while
    for(int i = 0; i < n; i++){
        if(dos[i] == num){
            est_present = true;
        }
    }
    return est_present;
}

void saisie_participants(Dossard & dos, Temps & tps, int n){
    for(int i = 0; i < n; i++){
        int nb_dossard;
        std::cout<<"Entrer le numéro du dossard du participant n°" << i+1 << "\n";
        std::cin>> nb_dossard;
        while(present(dos, nb_dossard, n)){
            std::cout<<"Ce numéro est déjà utilisé, entrez le numéro du dossard du participant n°" << i+1 << "\n";
            std::cin>> nb_dossard;
        }
        dos[i] = nb_dossard;
        std::cout<<"Entrez son temps de course\n";
        std::cin>> tps[i];
    }
}

void affichage(Dossard & dos, Temps & tps, int n){
    for(int i = 0; i < n; i++)
        std::cout<<"Dossard "<< dos[i] << " : " << tps[i] << "\n";
}

float indice_min(Temps tps, int n){
    float min = tps[0];
    int indice = 0;
    for(int i = 1; i<n; i++){
        if(tps[i] < min){
            min = tps[i];
            indice = i;
        }
    }
    return indice;
}

void supprime_coureur(int i, Dossard & dos, Temps & tps){
    dos[i] = 0;
    tps[i] = 0;
    for(int j = i+1; j <= N; j++){
        dos[j-1] = dos[j];
        tps[j-1] = tps[j];
    }
}

int main(){
    Dossard dos;
    Temps tps;
    int nb_participants;

    std::cout<<"Entrez le nombre de participants";
    std::cin>> nb_participants;

    init(dos, tps, nb_participants);
    saisie_participants(dos, tps, nb_participants);
    affichage(dos, tps, nb_participants);

    int indice_gagnant = indice_min(tps, nb_participants);
    std::cout<< "Gagnant : Dossard " << dos[indice_gagnant] << " : " << tps[indice_gagnant] << "\n";

    supprime_coureur(indice_gagnant, dos, tps);
    nb_participants = nb_participants - 1;

    affichage(dos, tps, nb_participants);
    
    int deuxieme = indice_min(tps, nb_participants);
    std::cout<< "Deuxième : Dossard " << dos[indice_gagnant] << " : " << tps[indice_gagnant] << "\n";
}