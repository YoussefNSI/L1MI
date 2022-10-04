#include <iostream>
#include <string>


int main()
{
    int occurrences;
    std::string chaine;
    std::cout<< "Entrez une phrase : ";
    std::getline(std::cin, chaine);
    char element;
    std::cout<< "Quel lettre cherchez vous ? : ";
    std::cin>> element;
    occurrences = 0;
    for(int i=0; i<chaine.length();i++){
        if(chaine[i]==element){
            occurrences += 1;
        }
    }
    std::cout<< "Nombre d'occurrences de " << element << " : " << occurrences;

    if (5 == 3) std::cout<<"oui";

    return 0;
}
