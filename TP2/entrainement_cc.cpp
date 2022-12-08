#include <iostream>
#include <string>
#include <array>

const int N=24;
using Calendrier = std::array<std::string,N>;

void saisie_calendrier(Calendrier & cal){
    for(int i = 0; i <= 24; i++){
        std::cout<< "Entrez la surprise du jour " << i+1 << " :\n";
        std::cin>> cal[i];
    }
}

bool Vide(Calendrier cal, int j){
    if(not(j < 1 or j > 24)){
        return cal[j-1] == "";
    }
    else{
        std::cout<<"Jour donné faux";
    }
}

void Ouvre(Calendrier & cal, int j){
    if(not(Vide(cal, j-1))){
        std::cout<< "Surprise du jour " << j << " : " << cal[j-1] << "\n";
        cal[j-1] = "";
    }
    else 
        std::cout<< "Déjà ouvert";
}

void Affiche_surprises(Calendrier & cal, char l){
    for(int i = 0; i <= 24; i++){
        if(cal[i][0] == l)
            std::cout<< cal[i];
    }
}

int Nb_occurences(Calendrier cal, std::string nom){
    int occurences = 0;
    for(int i = 0; i <= 24; i++){
        if(cal[i] == nom){
            occurences += 1;
        }
    }
    return occurences;
}

bool Unique(Calendrier cal, std::string nom){
    return Nb_occurences(cal, nom) == 1;
}

bool Ouverture_possible(Calendrier cal, int j){
    bool possible = true;
    int i = 0;
    while(possible and i < j-1){
        if(not(Vide(cal, i+1))){
            possible = false;
        }
    }
    return possible;
}

int main(){
    Calendrier C;
    //...
}

