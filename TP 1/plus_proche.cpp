
#include <iostream>
#include <cmath>


int main()
{
    int n, nb_reference, plus_proche, distance;
    
    std::cout<< "Combien de nombres voulez vous entrer ?";
    std::cin>> n;
    
    int nb[n] = {};
    
    for(int i = 0;i <= n-1;++i){
        std::cout<< "Entrez un nombre";
        std::cin>> nb[i];
    }
    
    std::cout<< "Entrez un nombre de reference";
    std::cin>> nb_reference;
    plus_proche = nb[0];
    distance = abs(nb[0] - nb[1]);
    
    for(int i = 1;i <= n-1;++i){
        if(abs(nb_reference - nb[i]) < distance){
            plus_proche = nb[i];
            distance = abs(nb_reference - nb[i]);
        }
    }
    std::cout<< plus_proche;
    
    return 0;
}
