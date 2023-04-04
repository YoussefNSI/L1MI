#include <iostream>
#include <array>

int pos_max(int T[], int taille)
{
    int pos_max = 0;
    for (int i = 0; i < taille; i++)
    {
        if (T[i] > T[pos_max])
            pos_max = i;
    }
    return pos_max;
}

void echange(int &a, int &b)
{
    int z = a;
    a = b;
    b = z;
}

void tri_selection(int T[], int taille)
{
    int max = 0;
    int temp_taille = taille;
    while (temp_taille - 1 >= 0)
    {
        max = pos_max(T, temp_taille);
        echange(T[temp_taille - 1], T[max]);
        temp_taille--;
    }
}

void tri_insertion(int * T, int taille){
    for(int i = 1; i< taille;i++){
        int x = T[i];
        int j = i;
        while (j>0 and T[j-1] > x)
        {
            T[j] = T[j-1];
            --j;
        }
        T[j] = x;
    }
}

void affiche_tab(int *T, int taille)
{
    for (int i = 0; i < taille; i++)
        std::cout << "T[" << i << "] = " << T[i] << std::endl;
}

int main()
{
    int T[20] = {4, 3, 1, 8, 6, 10, 12, 11, 19, 7, 2, 15};
    std::cout << pos_max(T, 12);
    tri_insertion(T, 12);
    affiche_tab(T, 12);
    return 0;
}