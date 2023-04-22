from random import randint

class Demineur:

    def __init__(self, ligne=16, colonne=16, bombe=50):
        self.ligne = ligne
        self.colonne = colonne
        self.taille = colonne
        self.bombe = bombe
        self.joueur1 = 0
        self.joueur2 = 0
        self.grille = [[0]*ligne for _ in range(colonne)]
        self._creation_grille()
        self.grille_non_visible = [["?"]*ligne for _ in range(colonne)]

    def _affichage(self, grille="visible"):
        """
        Affiche la grille visible avec toutes les bombes
        param:  par defaut affiche la grille visible.
                Sinon affiche la grille de jeu avec 
                les cases non révélés.
        """
        if grille == "visible" : 
            for i in range(self.ligne):
                chaine = ""
                for j in range(self.colonne):
                    if self.grille[i][j] == -1:
                        chaine += " *"
                    else:
                        chaine += " " + str(self.grille[i][j])
                print(chaine)
        else:
            for i in range(self.ligne):
                chaine = ""
                for j in range(self.colonne):
                    if self.grille_non_visible[i][j] == -1:
                        chaine += " *"
                    else:
                        chaine += " " + str(self.grille_non_visible[i][j])
                print(chaine)


    def _place_bombe(self):
        """
        Place les bombes aléatoirement dans la grille
        """
        bombe_place = 0

        while bombe_place != self.bombe:
            ligne_random = randint(0,self.ligne-1)
            colonne_random = randint(0,self.colonne-1)
            if self.grille[ligne_random][colonne_random] != -1:
                self.grille[ligne_random][colonne_random] = -1
                bombe_place += 1
    
    def _voisins_bombes(self):
        """
        Cherche le nombre de bombes autour des cases
        """
        voisins = [(-1, -1), (-1, 0), (-1, 1), (0, -1),\
                    (0, 1), (1, -1), (1, 0), (1, 1)] # indice des voisins
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.grille[i][j] == 0:
                    nb_bombes = 0
                    for x, y in voisins:
                        if i+x >= 0 and i+x < self.ligne and j+y >= 0 \
                                and j+y < self.colonne and self.grille[i+x][j+y] == -1: #conditions pour qu'on ne verifie pas
                                                                                        # au delà de la grille + est une bombe
                            nb_bombes += 1

                    self.grille[i][j] = nb_bombes

    

    def _creation_grille(self):
        self._place_bombe()
        self._voisins_bombes()
    
    def _cases_revele(self, x, y, liste_indice_modifie=None):
        """
        Révèle  récursivement les cases autour de l'endroit cliqué
          si il n'y a aucune bombe autour (les 0)
        """
        if liste_indice_modifie == None:
            liste_indice_modifie = []

        if self.grille[x][y] != -1:
            liste_indice_modifie.append((x, y))
        else:
            liste_indice_modifie.append("bombe")

        if self.grille[x][y] == 0:
            self.grille_non_visible[x][y] = self.grille[x][y]
            # Parcours les voisins pour révéler les cases vides
            for dx, dy in ((-1,-1),(-1, 0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)): #opérations pour les positions des voisins
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.ligne and 0 <= new_y < self.colonne and \
                        self.grille_non_visible[new_x][new_y] == "?":
                    self._cases_revele(new_x, new_y, liste_indice_modifie)
        else:
            self.grille_non_visible[x][y] = self.grille[x][y]
            
        return liste_indice_modifie
    


if __name__ == '__main__':
    grille_test = Demineur()
    print(grille_test._cases_revele(3,7))
    print("grille normal : \n")
    grille_test._affichage("non visible")
    print("grille visible")
    grille_test._affichage()



