#include <iostream>
#include <map>
#include <vector>

int main(){

    int n, Nmax, note, occurence;
    Nmax = 1000;
    std::vector<int> Nb(1000);
    n = 0;
    do{
        std::cout<< "Entrez une note entre [0, 20]";
        std::cin>> note;
        if(not(note > 20 or note < 0)){
            Nb[n] = note;
            n += 1;
        }
    }
    while(note >= 0 and note <= 20);

    std::map<int,int> dict_occurences;

    //Taille du vecteur au bon nombre de note
    Nb.resize(n);

    int elem = 0;
    occurence = 0;
    for(note = 0; note <= 20; note++){
        for(int i : Nb){
            if(i == note){
                occurence += 1;
            }
            elem += 1;
        }
        dict_occurences.insert({note, occurence});
        occurence = 0;
    }

    for(int i = 0; i <= 20; i++){
        char etoile = '*';  
        int num = dict_occurences[i];
        std::cout << i << " : " << std::string(num, etoile) << "\n"; 
    }

}