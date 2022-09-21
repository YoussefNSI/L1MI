/* Online C++ Compiler and Editor */
#include <iostream>

int check_if_in(int size, int tab[], int value){
    bool check;
    for(int i = 0; i <= size; i++){
        check = (tab[i] == value);
    }
    return check;
}



int main()
{
   int n, nb;
   int tab[n] = {};
   n = 0;
   do{
       std::cout<<"Entrez une valeur";
       std::cin>>nb;
       tab[n] = nb;
       n += 1;
   }
   while(not (check_if_in(n, &tab[n], nb)) or n < 10);
   for(int i = 0; i <= n; i++){
       std::cout<< tab[n];
   }
   return 0;
}
