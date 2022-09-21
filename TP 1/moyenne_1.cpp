#include <iostream>

int main(){
    float note_anglais, note_maths, note_info, moyenne;

    std::cout<< "Entrez la note d'anglais";
    std::cin>> note_anglais;
    std::cout<< "Entrez la note de maths";
    std::cin>> note_maths;
    std::cout<< "Entrez la note d'info";
    std::cin>> note_info;
    
    moyenne = ((2*note_anglais)+(5*note_maths)+(3*note_info))/10;

    std::cout<< " Note en Anglais (coeff.2) : " << note_anglais << "\n Note en Mathématiques (coeff.5) :"\
    <<  note_maths << "\n Note en Informatique(coeff.3) : " << note_info << "\n Moyenne obtenue : \
    " << moyenne << "";

}
