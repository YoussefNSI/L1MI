from random import randint

class Demineur:

    def __init__(self, ligne=16, colonne=16, bombe=50):
        self.ligne = ligne
        self.colonne = colonne
        self.bombe = bombe
        self.grille = [[0]*ligne for _ in range(colonne)]
        self._creation_grille()

    def affichage(self):
        for i in range(self.ligne):
            chaine = ""
            for j in range(self.colonne):
                chaine = chaine + " " + str(self.grille[i][j])
            print(chaine, "\n")

    def _place_bombe(self):
        bombe_place = 0

        while bombe_place != self.bombe:
            ligne_random = randint(0,15)
            colonne_random = randint(0,15)
            if self.grille[ligne_random][colonne_random] != -1:
                self.grille[ligne_random][colonne_random] = -1
                bombe_place += 1

    def _grille_somme(self):
        grille_somme = self.grille
        grille_somme.insert(0, [0 for _ in range(self.ligne)])
        grille_somme.append([0 for _ in range(self.ligne)])
        for ligne in grille_somme:
            ligne.insert(0, 0)
            ligne.insert(-1, 0)
        return grille_somme

        



    def _voisins(self):
        grille_somme = self._grille_somme()
        indice_voisins = [(-1, 0), (1, 0), (0, 1), (0, -1),  # haut + bas + droite + gauche
                 (-1, -1), (1, -1), (1, 1), (-1, 1), ] # diagonales
        for x in range(1, len(grille_somme)):
            for y in range(1, len(grille_somme[x])):
                somme = 0
                for x_inc, y_inc in indice_voisins:
                    if grille_somme[x + x_inc][y + y_inc] != -1:
                        print("indice : x = ", x + x_inc, ", y = ", y + y_inc, "\n")
                        somme += grille_somme[x + x_inc][y + y_inc]
        self.grille = grille_somme




    def _creation_grille(self):
        self._place_bombe()
        self._voisins()

grille_test = Demineur()
print("grille normal : \n")
grille_test.affichage()

