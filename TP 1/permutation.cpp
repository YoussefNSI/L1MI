#include <iostream>

int main(){

    int v1, v2, v3, aux1, aux2;

    v1 = 3;
    v2 = 6;
    v3 = 9;

    aux1 = v1;
    v1 = v3;
    aux2 = v2;
    v2 = aux1;
    v3 = aux2;

    std::cout<< "v1 : " << v1 << "\n";
    std::cout<<"v2 : " <<  v2 << "\n";
    std::cout<< "v3 : " << v3 << "";
}