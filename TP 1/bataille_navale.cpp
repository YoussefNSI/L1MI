#include <iostream>
#include <algorithm>
#include <cstdlib>

int main(){
    const int longueur = 9;
    const int largeur = 9;
    int grille[longueur][largeur] = {};
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

        while(not place_trouve){
            int position_x = rand() % 9;
            int position_y = rand() % 9;
            if(position_x - 9 < 0){
                if(position_y - 9 < 0){
                    //depasse la grille
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
        bool placer = false;
        while(not placer){
            if(horizontal){
                //bateau a l'horizontal
            }
            else{
                //bateau a la verticale
            }
        }
    }
}
