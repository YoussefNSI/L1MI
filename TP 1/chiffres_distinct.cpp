#include <iostream>


int main()
{
    int premier, milieu, dernier;
    
    for(int i = 100; i <=999;++i){
        premier = i/100 % 10;
        milieu = i/10 % 10;
        dernier = i % 10;
        
        if((premier == milieu and milieu == dernier) and \
        (premier + milieu + dernier == 9)){
            std::cout<< i;
        }
    }
    return 0;
}
