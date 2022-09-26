/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

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

    return 0;
}
