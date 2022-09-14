#include <iostream>

int main(){

    int x, max;

    std::cout<< "Quelle table de multiplication ?";
    std::cin>> x;
    do{
        std::cout<< "Jusqu'à combien ? (nombre strictement positif)";
        std::cin>> max;
    }
    while(max < 1);
    for(int i = 1; i <= max; ++i){
        std::cout<< x << " x " << i << " = " << x * i << "\n";
    }
}