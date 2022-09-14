#include <iostream>
// nombre inconnu 

int main(){

    int random_num, proposition;

    random_num = rand() % 100 + 1;

    do{
        std::cout<< " Entrez votre proposition ";
        std::cin >> proposition;
        if(proposition > random_num){
            std::cout<< "Le numéro est plus petit\n";
        }
        else if(proposition < random_num){
            std::cout<< "Le numéro est plus grand\n";
        }
    }
    while(proposition != random_num);
    std::cout<< " Le numéro était " << random_num << "";
}   