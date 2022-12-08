#include <iostream>
#include <array>
#include <string>

const int M = 5;
const int taille = (2*M) + 1;
using jeu = std::array<std::string, taille>;

void init(jeu & T){
    std::string mouton1 = "B";
    std::string mouton2 = "N";
    std::string vide = "X";
    int mi_taille = taille/2;
    T[mi_taille] = vide;
    for(int i = 0; i < mi_taille; i++)
        T[i] = mouton1;
    for(int i = mi_taille+1; i < taille;i++)
        T[i] = mouton2;
}

void afficher(jeu & T){
    for(int i = 0; i < taille; i++){
        if(T[i] == "X")
            std::cout<<"| " << " " << " |";
        else
            std::cout<<"| " << T[i] << " |";
    }
}



int caseVide(jeu T){
    int caseVide = 0;
    for(int i = 0; i < taille; i++)
        if(T[i] == "X")
            caseVide = i;
    return caseVide;
}

bool peutAvancer(jeu T, int mouton){
    if(T[mouton] == "B" and mouton < taille-1) return T[mouton+1] == "X";
    else if(T[mouton] == "N" and mouton > 0) return T[mouton-1] == "X";
    else return false;
}

bool peutSauter(jeu T, int mouton){
    if((T[mouton] == "B" and mouton < taille-2) and mouton != 0) return (T[mouton+1] == "N" or T[mouton+1] == "B") and \
    T[mouton+2] == "X";
    else if((T[mouton] == "N" and mouton > 1) and mouton != taille-1) return (T[mouton-1] == "B" or T[mouton-1] == "N") and \
    T[mouton-2] == "X";
    else return false;
}

bool gagne(jeu T){
    bool gagne = true;
    int mi_taille = taille/2;
    for(int i = 0; i < mi_taille; i++)
        if(T[i] != "N")
            gagne = false;
    for(int i = mi_taille+1; i < taille;i++)
        if(T[i] != "B")
            gagne = false;
    return gagne;
}

bool perdu(jeu T){
    bool perdu = true;
    int case_vide = caseVide(T);
    for(int i = 0; i < taille; i++){
        if(i != case_vide){
            if((peutAvancer(T, i) or peutSauter(T, i))){
                perdu = false;
            }
        }
    }
    return perdu;
}

void joue(jeu & T, bool & partie_termine){
    int mouton;
    std::cout<< "Emplacement du mouton à déplacer ? ";
    std::cin>> mouton;
    std::cout<< "\n";
    mouton -= 1;
    if(peutAvancer(T, mouton)){
        if(T[mouton] == "B"){
            T[mouton] = "X";
            T[mouton+1] = "B";
        }
        else{
            T[mouton] = "X";
            T[mouton-1] = "N";
        }
    }
    else if(peutSauter(T, mouton)){
        if(T[mouton] == "B"){
            T[mouton] = "X";
            T[mouton+2] = "B";
        }
        else{
            T[mouton] = "X";
            T[mouton-2] = "N";
        }
    }
    else{
        // verifie si aucun coup n'est jouable
        partie_termine = perdu(T);
    }
}


int main(){
    jeu T;
    init(T);
    bool partie_termine = false;
    std::cout<< "⚠ Emplacement du mouton à donner à partir de 1\n";
    do{
        std::cout<< "Plateau de jeu : ";
        afficher(T);
        std::cout<< "\n";
        joue(T, partie_termine);
    }
    while(not partie_termine);

    if(gagne(T)){
        std::cout<< "Partie gagnée : ";
        afficher(T);
    }
    else{
        std::cout<< "Partie perdue, aucun coup jouable. Plateau final : ";
        afficher(T);
    }
}

