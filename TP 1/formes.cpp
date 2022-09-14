#include <iostream>


int main()
{
    //déclaration de variables
    int longueur;
    std::string etoile;
    
    std::cout<< "Entrez la longueur du coté";
    std::cin>>longueur;
    
    //carré vide
    std::cout<<"carré vide : \n";
    for(int i = 0; i <= longueur; ++i){
        if(i == 0 or i == longueur){
            std::cout<< " *******\n";
        }
        else{
            std::cout<< " *     *\n";
        }
    }
     //carré plein
     std::cout<< "carré plein : \n";
     for(int i = 0; i <= longueur; ++i){
        std::cout<< " *******\n";
    }
    //damier
    std::cout<<"damier : \n";
    for(int i = 0;i <=longueur; ++i){
        if(i % 2 == 0){
            std::cout<< "  * * *  \n";
        }
        else{
            std::cout<< "   * * * \n";
        }
    }
    //triangle rectangle isocèle
    etoile = "******";
    std::cout<< "Triangle rectangle isocèle : \n";
    for(int i = 0; i <= 5; ++i){
        std::cout<< " " << etoile.substr(i) << "\n";
    }
    return 0;
}
