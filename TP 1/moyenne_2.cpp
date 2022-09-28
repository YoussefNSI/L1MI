#include <iostream>

int main(){
    int note, moyenne, min, max, nb;
    moyenne = 0;
    nb = 0;
    min = 20;
    max = 0;
    std::cout<<"Arretez la saisie en entrant -1\n";
    do{
        std::cout<<"Entrez une note";
        std::cin>>note;
        if(note < 0 or note > 20 or note == -1){
            break;
        }
        moyenne += note;

        if(note < min){
            min = note;
        }
        if(note > max){
            max = note;
        }
        nb += 1;
    }
    while(note >= 0 and note < 21);
    moyenne = moyenne/nb;
    std::cout<< "\n";
    std::cout<< "Moyenne des notes : " << moyenne << "\nMinimum : " << min << "\nMaximum : " << max;

}   