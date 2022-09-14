#include <iostream>

int multiplication(int a, int b){
    return a * b;
}

int somme(int a, int b){
    return a + b;
}

int main(){

    int n1, n2, proposition, resultat;
    char operateur;

    std::cout << "Parents/Enseignants, entrez le premier nombre :";
    std::cin >> n1;
    std::cout << "\nEt le deuxième : ";
    std::cin >> n2;
    std::cout<< "Quel opération voulez vous effectuer ? (*, -, +)";
    std::cin>> operateur;
    
    if(operateur == '+'){
        resultat = somme(n1, n2);
    }
    else if(operateur == '-'){
        resultat = somme(n1, -n2);
    }
    else{
        resultat = multiplication(n1, n2);
    }
    std::cout<< "\nEleve, calcule " << n1 << operateur << n2 << " !\n";
    std::cin>> proposition;

    if(proposition ==  resultat){
        std::cout<< "Bravo !";
        return 0;
    }
    else{
        std::cout<< "Faux, la réponse était " << resultat << ".";
        return 0;
        }
}