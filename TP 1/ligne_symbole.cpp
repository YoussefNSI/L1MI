#include <iostream>

int main(){
    
    int n;
    std::cout<<"Combien d'étoiles voulez vous afficher ?";
    std::cin>> n;
    for(int i = 0; i <= n; ++i){
        if(i % 2 == 0){
            std::cout<< "*";
        }
        else{
            std::cout<< "!";
        }
        
    }
}