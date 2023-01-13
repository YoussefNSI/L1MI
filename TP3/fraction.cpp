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
 
fraction add(fraction f1, fraction f2){
    fraction f3;
    int pgcd2 = pgcd(f1.den, f2.den);
    f3.num = (f1.num * pgcd2) + (f2.num * pgcd2);
    f3.den = (f1.den * pgcd2) + (f2.den * pgcd2);
    int pgcds = pgcd(f3.den, f3.num);
    f3.num /= pgcds;
    f3.den /= pgcds;
    return f3;
}

fraction opp(fraction f){
    fraction opp;
    opp.num = 0 - f.num;
    opp.den = f.den;
    return opp;
}

fraction inv(fraction f){
    fraction inv;
    inv.num = f.den;
    inv.den = f.num;
    return inv;
}

fraction soustr(fraction f1, fraction f2){
    fraction oppose2 = opp(f2);
    return add(f1, oppose2);
}

fraction div(fraction f1, fraction f2){
    fraction inverse2 = inv(f2);
    return mult(f1, inverse2);
}

int main(){
    fraction f1, f2;
    saisie(f1);
    saisie(f2);
    fraction f3 = soustr(f1, f2);
    affichage(opp(f1));
}