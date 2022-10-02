#include <iostream>
#include <cmath>
#include <complex>

int main(){

    float a, b, c, delta, x1, x2;
    
    std::complex<double> z1 = (0.0, 1.0);
    std::cout<< "Entrez les coefficients a, b, c";
    std::cin>> a;
    std::cin>> b;
    std::cin>> c;

    delta = b*b - 4*a*c;
    

    if(delta < 0){
        std::cout<< "Pas de solution dans R, deux racines dans C a trouver (calculatrice)";
        return 0;
    }
    else if(delta == 0){
        x1 = -b/2*a;
        std::cout<< "Delta = 0, une racine qui est : " << x1 << "";
        return 0;
    }
    else{
        x1 = (-b - sqrt(delta))/2 * a;
        x2 = (-b + sqrt(delta))/2 * a;
        std::cout<< "deux racines : x1 = "<< x1 << "et x2 = " << x2 << "";
        return 0;
    }
}