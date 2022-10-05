#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <array>

int main(){
    const int longueur = 10;
    const int largeur = 10;
    int position_x, position_y;
    std::vector<std::vector<int>> grille(longueur, std::vector<int>(largeur));
    int nb_bateau, long_bateau;
    std::cout<<"Nombre de bateaux : ";
    std::cin>>nb_bateau;
    int tab_bateau[nb_bateau] = {};
    for(int i = 0; i < nb_bateau; i++){
        std::cout<< "Longueur du bateau no."<<i<<" : ";
        std::cin>>long_bateau;
        tab_bateau[i] = long_bateau;
    }
    for(int i = 0; i <= nb_bateau; i++){
        bool horizontal = false;
        bool place_trouve = false;
        bool placer = false;
        int boucle_i = i;
        while(not placer){
            while(not place_trouve){
                position_x = (rand() % 9);
                position_y = (rand() % 9);
                std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                if(9 - position_x < 0 or position_x - tab_bateau[i] < 0){
                    if((9 - position_y) < 0 or (position_y - tab_bateau[i]) < 0){
                        //depasse la grille a l'horizontal
                        std::cout<< "Le bateau depasse, longueur = " << tab_bateau[i];
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
                std::cout<< "bateau a l'horizontal";
                //bateau a l'horizontal
                placer = true;
                for(int k = 0; k < tab_bateau[boucle_i]; k++){
                    if(grille[position_x][position_y] != 0){
                        placer = false;
                    }
                    else{
                        grille[position_x][position_y] = tab_bateau[boucle_i];
                    }
                    std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                    position_y += 1;
                    
                }
            }
            else{
                std::cout<<"bateau a la verticale";
                //bateau a la verticale
                for(int k = 0; k < tab_bateau[boucle_i]; k++){
                    grille[position_x][position_y] = tab_bateau[boucle_i];
                    std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                    position_x += 1;
                }
                placer = true;
            }
        }   
    }
    for(int i = 0; i <= 9; i++){
        std::cout<<"\n";
        for(int j = 0; j <= 9; j++){
            std::cout<< grille[i][j];
        }
    }
}
