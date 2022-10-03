

#include <iostream>
#include <vector>

int main()
{
    int taille, num, aux;
    std::cout<< "Entrez la taille de la matrice carrée";
    std::cin>> taille;
    std::vector<std::vector<int>> matrice(taille, std::vector<int>(taille));
    num = 1;
    for(int i = 0; i <= taille; i++){
        for(int j = 0; j < taille; j++){
            matrice[i][j] = num;
            num += 1;
            std::cout<< "matrice["<<i<<"]["<<j<<"] = "<< matrice[i][j] << "\n";
        }
    }
    
    std::cout<<"transposée : ";
    
    for(int i = 0; i <= taille; i++){
        for(int j=0; j <= taille; j++){
            aux = matrice[i][j];
            matrice[i][j] = matrice[j][i];
            matrice[j][i] = aux;
            std::cout<< "matrice["<<i<<"]["<<j<<"] = "<< matrice[i][j] << "\n";
        }
    }
    
    return 0;
}
