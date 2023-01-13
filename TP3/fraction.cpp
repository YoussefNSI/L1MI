#include <iostream>

struct fraction
{
    int num, den;
};

void saisie(fraction & f){
    std::cout<<"Entrez le numérateur de la fraction";
    std::cin>> f.num;
    std::cout<<"Entrez le dénominateur de la fraction";
    std::cin>> f.den;
}

void affichage(fraction f){
    std::cout<< f.num << "/" << f.den;
}

fraction mult(fraction f1, fraction f2){
    fraction f3;
    f3.num = f1.num * f2.num;
    f3.den = f1.den * f2.den;
    return f3;
}
int pgcd(int a, int b)
{
    if (b==0) return a ;
    else return pgcd (b, a%b) ; 
}
 

int add(fraction f1, fraction f2){
    int pgcd2 = pgcd(f1.den, f2.den);
    return pgcd2;
}

int main(){
    saisie
}