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
    for(int i = 0; i <= nb_bateau-1; i++){
        std::cout<< "Longueur du bateau no."<<i<<" : ";
        std::cin>>long_bateau;
        tab_bateau[i] = long_bateau;
    }
    for(int i = 0; i <= nb_bateau-1; i++){
        bool horizontal = false;
        bool place_trouve = false;
        bool placer = false;
        int boucle_i = i;
        while(not placer){
            std::cout<<"\nje passe dans la boucle pour i = " << i << "\n";
            while(not place_trouve){
                position_x = (rand() % 10);
                position_y = (rand() % 10);
                std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                if(tab_bateau[i] > abs((position_x - 9))){
                    //depasse la grille a l'horizontal
                    if(tab_bateau[i] > abs((position_y - 9))){
                        //depasse la grille a la verticale
                        std::cout<< "Le bateau depasse, longueur = " << tab_bateau[i] << "\n";
                        ;
                    }
                    else{
                        //le bateau sera à l'horizontal
                        horizontal = true;
                        place_trouve = true;
                    }    
                }
                else{
                    //le bateau sera à la verticale
                    horizontal = false;
                    place_trouve = true;
                }
            }
        
            if(horizontal){
                //bateau a l'horizontal

                int position_y_test = position_y;
                placer = true;
                //cherche si obstacle
                for(int k = 0; k < tab_bateau[boucle_i]; k++){
                    if(grille[position_x][position_y_test] != 0){
                        placer = false;
                        place_trouve = false;
                    }
                    else position_y_test += 1;                   
                }
                //aucun obstacle
                if(placer){
                    for(int k = 0; k < tab_bateau[boucle_i]; k++){
                        grille[position_x][position_y] = boucle_i + 1;
                        std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                        position_y += 1;           
                    }
                }
            }
            else{
                //bateau a la verticale

                int position_x_test = position_x;
                placer = true;
                for(int k = 0; k < tab_bateau[boucle_i]; k++){
                    //cherche si il y a un obstacle
                    if(grille[position_x_test][position_y] != 0){
                        placer = false;
                        place_trouve = false;
                    }
                    else position_x_test += 1;
                }
                if(placer){
                    //aucun obstacle trouvé
                    for(int k = 0; k < tab_bateau[boucle_i]; k++){
                        grille[position_x][position_y] = boucle_i +1;
                        std::cout << "position x : " << position_x << " position y : " << position_y << "\n";
                        position_x += 1;
                    }
                }
            }
        }   
    }
    
    std::cout<<"\nGrille finale : \n";

    for(int i = 0; i <= 9; i++){
        std::cout<<"\n";
        for(int j = 0; j <= 9; j++){
            std::cout<< grille[i][j];
        }
    }
}
