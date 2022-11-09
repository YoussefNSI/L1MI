#include <iostream>
#include <cmath>
#include <string>


int x, y, z;

void cote_triangle(float &x, float &y, float &z){

    std::cout<< "Entrez les longueurs du triangle : ";
    std::cin>> x >> y >> z;
}

bool est_valide(float x, float y, float z){
    bool est_valide = false;
    if(x+y > z and x+z > y and y+z > x) 
        est_valide = true;
    else
        est_valide = false;
    return est_valide;
}

float perimetre_t(float x, float y, float z){
    return x + y + z;
}

float aire_t(float x, float y, float z){
    float s = (x + y + z)/2;

    return sqrt(s*(s-x)*(s-y)*(s-z));
}

bool est_isocele(float x, float y, float z){
    if(x == y or x == z or y == z) return true;
    else return false;
}
bool est_equi(float x, float y, float z){
    if(x == y and y == z) return true;
    else return false;
}
bool est_rectangle(float x, float y, float z){
    if(x > y and x > z)
        if(x*x == z*z + y*y)
            return true;
        else return false;
    else if(y > x and y > z)
        if(y*y == x*x + z*z)
            return true;
        else return false;
    else
        if(z*z == x*x + y*y)
            return true;
        else return false;
}

bool est_plat(float x, float y, float z){
    return false;
}

std::string nature_t(float x, float y, float z){
    std::string nature;
    if(est_valide(x,y,z)){
        if(est_equi(x,y,z))
            nature = "équilatéral";
        else if(est_isocele(x,y,z))
            nature = "isocèle";
        else if(est_rectangle(x,y,z))
            nature = "triangle rectangle";
        else if(est_plat(x,y,z))
            nature = "triangle plat";
        else
            nature = "triangle quelconque";
    }
    else{
        nature = "Non valide";
    }
    return nature;
}

int main(){
    float x, y, z;
    cote_triangle(x, y, z);
    std::cout<< nature_t(x,y,z);
}

