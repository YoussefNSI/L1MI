#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <array>

int main(){
    const int longueur = 9;
    const int largeur = 9;
    int position_x, position_y;
    std::vector<std::vector<int>> grille(longueur);
    int nb_bateau, long_bateau;
    std::cout<<"Nombre de bateaux : ";
    std::cin>>nb_bateau;
    int tab_bateau[nb_bateau+1] = {};
    for(int i = 1; i <= nb_bateau; i++){
        std::cout<< "Longueur du bateau no."<<i<<" : ";
        std::cin>>long_bateau;
        tab_bateau[i] = long_bateau;
    }
    for(int i = 1; i <= nb_bateau; i++){
        bool horizontal = false;
        bool place_trouve = false;
        bool placer = false;
        while(not placer){
            while(not place_trouve){
                position_x = rand() % 9;
                position_y = rand() % 9;
                if(position_x - 9 < 0){
                    if(position_y - 9 < 0){
                        //depasse la grille a l'horizontal
                        ;
                    }
                    else{
                        horizontal = true;
                        place_trouve = true;
                    }    
                }
                else{
                    horizontal = false;
                    place_trouve = true;
                }
            }
        
            if(horizontal){
                //bateau a l'horizontal
                for(int k = 0; k > tab_bateau[i]; k++){
                    grille[position_x][position_y] = tab_bateau[i];
                    position_y += 1;
                    placer = true;
                }
            }
            else{
                //bateau a la verticale
                for(int k = 0; k > tab_bateau[i]; k++){
                    grille[position_x][position_y] = tab_bateau[i];
                    position_x += 1;
                    placer = true;
                }
            }
        }   
    }
    for(int i = 0; i <= longueur; i++){
        std::cout<< i+1 << "ligne :\n";
        for(int j = 0; j <= largeur; j++){
            std::cout<< grille[i][j];
        }
    }
}
