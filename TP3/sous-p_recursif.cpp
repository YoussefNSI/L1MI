#include <iostream>
#include <string>

char r_bonjour(int n){
    if(n == 1){
        std::cout<<"bonjour";
        return 0;
    }
    else{
        std::cout<<"bonjour\n";
        return r_bonjour(n-1);
    }
}

int r_somme_carre(int n){
    if(n == 1){
        return 1;
    }
    else{
        return n*n + r_somme_carre(n-1);
    }
}

int main(){
    int n = 5;
    r_bonjour(n);
    std::cout<< "\n";
    std::cout<< r_somme_carre(n);
}
