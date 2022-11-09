#include <iostream>
#include <array>

const int tabMax = 12;
using TabPrecipitations = std::array<float, tabMax>;

void init(TabPrecipitations & T){

    for(int i = 0; i < tabMax; i++)
        T[i] = 0;
}

void saisie(TabPrecipitations & T){
    std::cout<< "Entrez les températures dans l'ordre des mois (de Janvier\
    à Décembre)\n";
    for(int i = 0; i < tabMax ; i++){
        std::cout<<"Mois " << i+1 <<" : ";
        std::cin>> T[i];
    }
}

void affichage(TabPrecipitations & T){
    for(int i = 0; i < tabMax; i++)
        std::cout<< "T["<< i <<"] = "<< T[i] << " \n";
}

int minimale(TabPrecipitations T){
    int min = T[0];
    for(int i = 1; i < tabMax; i++)
        if(T[i] < min)
            min = T[i];
    return min;
}
int maximale(TabPrecipitations T){
    int max = T[0];
    for(int i = 1; i < tabMax; i++)
        if(T[i] > max)
            max = T[i];
    return max;
}

int main(){
    TabPrecipitations Nantes, Angers;
    saisie(Nantes);
    saisie(Angers);
    //affichage(Nantes);
    //affichage(Angers);
    if(maximale(Angers) > maximale(Nantes))
        std::cout<< "Le max est à Angers : " << maximale(Angers) << "C°\n";
    else
        std::cout<< "Le max est à Nantes : " << maximale(Nantes) << "C°\n";
    if(minimale(Angers) < minimale(Nantes))
        std::cout<< "Le min est à Angers : " << minimale(Angers) << "C°\n";
    else
        std::cout<< "Le min est à Nantes : " << minimale(Nantes) << "C°\n";
}