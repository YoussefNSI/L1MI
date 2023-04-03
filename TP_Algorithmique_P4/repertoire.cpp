#include <iostream>

struct personne
{
    std::string nom;
    std::string prenom;
    std::string tel;
};

struct maillon
{
    personne val;
    maillon *suiv;
};

using repertoire = maillon *;

void initialiserRepertoire(repertoire &R)
{
    R = nullptr;
}

void ajouterEnTete(std::string nom, std::string prenom,
                   std::string tel, repertoire &R)
{
    repertoire aux;
    aux = new maillon;
    aux->val.nom = nom;
    aux->val.prenom = prenom;
    aux->val.tel = tel;
    aux->suiv = R;
    R = aux;
}

void ajouterEnQueue(std::string nom, std::string prenom,
                    std::string tel, repertoire &R)
{
    if (R == nullptr)
    {
        R = new maillon;
        R->val.nom = nom;
        R->val.prenom = prenom;
        R->val.tel = tel;
        R->suiv = nullptr;
    }
    else
    {
        ajouterEnQueue(nom, prenom, tel, R->suiv);
    }
}

void afficherPersonne(personne P)
{
    std::cout << "[" << P.nom << ", " << P.prenom << ", "
              << P.tel << "]" << std::endl;
}

void afficherRepertoire(repertoire R)
{
    if (R == nullptr)
    {
        std::cout << "";
    }
    else
    {
        afficherPersonne(R->val);
        afficherRepertoire(R->suiv);
    }
}

std::string telephone(std::string nom, std::string prenom,
                      repertoire R)
{
    if (R == nullptr)
        return "";
    if (R->val.nom == nom and R->val.prenom == prenom)
        return R->val.tel;
    else
        return telephone(nom, prenom, R->suiv);
}

int rechercherPosition(std::string nom, std::string prenom,
                       repertoire R, int pos = 1)
{
    if (R == nullptr)
        return 0;
    if (R->val.nom == nom and R->val.prenom == prenom)
        return pos;
    else
        return rechercherPosition(nom, prenom, R->suiv, pos + 1);
}

void ajouter(int position, std::string nom, std::string prenom,
             std::string tel, repertoire &R)
{
    if (position < 1)
    {
        std::cout << "La position doit être égale ou supérieure à 1";
        return;
    }
    if (R == nullptr and position > 1)
    {
        ajouterEnQueue(nom, prenom, tel, R);
    }
    else if (position == 1)
    {
        repertoire aux = R;
        R = new maillon;
        R->val.nom = nom;
        R->val.prenom = prenom;
        R->val.tel = tel;
        R->suiv = aux;
    }
    else
    {
        ajouter(position - 1, nom, prenom, tel, R->suiv);
    }
}

void supprimer(int position, repertoire &R)
{
    if (position < 1)
    {
        std::cout << "La position doit être égale ou supérieure à 1\n";
        return;
    }
    if (R == nullptr)
    {
        return;
    }
    else if (position == 1)
    {
        repertoire aux;
        aux = R;
        R = R->suiv;
        delete aux;
    }
    else
    {
        supprimer(position - 1, R->suiv);
    }
}

void supprimer(std::string nom, repertoire &R)
{
    while (R != nullptr and R->val.nom == nom)
    {
        repertoire aux = R;
        R = R->suiv;
        delete aux;
    }
    if (R != nullptr)
    {
        supprimer(nom, R->suiv);
    }
}

int main()
{
    repertoire R;
    initialiserRepertoire(R);
    ajouterEnTete("radouan", "youssef", "000000", R);
    ajouterEnTete("leguyader", "clement", "000000", R);
    ajouterEnQueue("leguyader", "nattan", "1234567890", R);
    ajouter(1000, "radouan", "qqlun", "987654321", R);
    afficherRepertoire(R);
    std::cout << rechercherPosition("leguyader", "nattan", R);
}
