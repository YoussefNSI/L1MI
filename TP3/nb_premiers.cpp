#include <iostream>

int diviseur(int n, int d){
    if(d == n)
        return n;
    else{
        if(n%d == 0 and d > 1)
            return d;
        else
            return diviseur(n, d+1);    
    }
}

bool est_premier(int n){
    return diviseur(n, 1) == n;
}

void affiche_premiers(int n){
    if(n == 1){
        std::cout<< "1";
    }
    else{
        if(est_premier(n)) std::cout<< n << "\n";
        affiche_premiers(n-1);
    }
}

int main(){
    affiche_premiers(13);
}