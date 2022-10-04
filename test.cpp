#include <iostream>

int main(){

    int x,y;
    bool test1, test2;
    x = 10;
    y = 12;
    test1 = (x<y%7) or (x+8>y);
    test2 = test1 and (x==y);

    if(test1==true)
        if (test2==true) x=y-2;
        else x=-y+4;
    else y=2*x;
    
    std::cout<< "x = " << x << " y = " << y;
}