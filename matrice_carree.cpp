

#include <iostream>
#include <vector>

int main()
{
    int taille, num, aux;
    std::cout<< "Entrez la taille de la matrice carrée";
    std::cin>> taille;
    std::vector<std::vector<int>> matrice(taille, std::vector<int>(taille));
    num = 1;
    for(int i = 0; i < taille; i++){
        for(int j = 0; j < taille; j++){
            matrice[i][j] = num;
            num += 1;
        }
    }
    std::vector<std::vector<int>> transposee(taille, std::vector<int>(taille));
    
    for(int i = 0; i < taille; i++){
        for(int j=0; j < taille; j++){
            transposee[j][i] = matrice[i][j];
        }
    }
    for(int i = 0; i < taille; i++){
        for(int j = 0; j < taille; j++){
            std::cout<< "matrice[i][j] = "<<matrice[i][j]<<"\n";
            std::cout<<"Transposee = "<< transposee[i][j]<<"\n";
        }
    }
    return 0;
}
