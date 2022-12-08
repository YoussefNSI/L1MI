#include <iostream>
#include <string>

std::string copie(std::string s, int j, int i){
    std::string copie = "";
    int taille = s.length();
    
    do{
        copie += s[i];
        i += 1;
        j -= 1;
    }
    while((not j == 0) or (not i == taille));
    return copie;
}

void supprime(std::string & s, int j, int i){
    s = s.erase(i, j);
}

void insere(std::string & s1, std::string & s2, int i){
    std::string mot_deplace = s2.substr(i, s1.length());
    supprime(s2, s1.length(), i);
    s2 += s1 + mot_deplace;
}

int position_str(std::string s1, std::string s2){
    taille_s2 = s2.length();
    int i = 0;
    std::string s3 = "";
    while(i != taille_s2){
        if(s2[i] == s1[i]){
            s3 += s2[i];
        }
        i += 1;
    }
}



int main(){
    std::string s = "phrase";
    std::string s2 = "deux";
    insere(s2, s, 2);
    std::cout<< s;
}