#include <iostream>
#include <map>

int main(){

    int n, Nmax, note, occurence;
    Nmax = 1000;
    int Nb[Nmax] = {};
    n = 0;
    do{
        std::cout<< "Entrez une note entre [0, 20]";
        std::cin>> note;
        if(not(note > 20 or note < 0)){
            Nb[n] = note;
        }
        n += 1;
    }
    while(note >= 0 and note <= 20);
    std::cout<< "N : " << n << "\n";
    std::map<int,int> dict_occurences;
    
    for(note = 0; note <= 20; note++){
        for(int i = 0;i <= n; i++){
            if(Nb[i] == note){
                occurence += 1;
            }
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