
#include <iostream>

int somme_diviseurs(int a){
    int somme;
    somme = 0;
    for(int i = 1;i <= a; ++i){
        if(a % i == 0){
            somme += i;
        }
    }
    return somme;
}

int main()
{
    int borne;
    std::cout<<"Afficher les nombres parfaits de 0 à ... : ";
    std::cin>> borne;
    for(int i = 1; i <= borne; ++i){
        if(i == somme_diviseurs(i)/2){
            std::cout<< i << "\n";
        }
    }
    return 0;
}
