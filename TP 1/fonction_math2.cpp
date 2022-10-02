#include <iostream>

int main(){

    float x, fonction, num, den;

    std::cout<< "Entrez le x : ";
    std::cin>> x;

    num = abs(x) + 3 *(x * x);
    den = (2*(x*x)/3) - 6;
    std::cout<< num << "\nden : " << den <<"\n";

    if(den == 0){
        std::cout<< "La fonction n'est pas défini pour " << x << "";
        return 0;}
    
    fonction = num/den;
    std::cout<< "f("<<x<<") est " << fonction << "";
    }

