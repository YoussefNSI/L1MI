from random import randint
from pprint import pprint
from time import sleep
import itertools

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
    
    
    def _cases_a_verifier(self):
        liste_indice = []
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.grille_non_visible[i][j] not in ["?", 0, -1]:
                    liste_indice.append((i, j))
        return liste_indice
    
    def _get_cases_voisins(self, x, y):
        liste_indice = []
        for dx, dy in ((-1,-1),(-1, 0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            new_x, new_y = dx + x, dy + y
            if 0 <= new_x < self.ligne and 0 <= new_y < self.colonne:
                liste_indice.append((new_x, new_y))
        return liste_indice
    
    def _get_voisins_non_revele(self, coord):
        x, y = coord
        liste_indice = []
        for dx, dy in ((-1,-1),(-1, 0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            new_x, new_y = dx + x, dy + y
            if (0 <= new_x < self.ligne and 0 <= new_y < self.colonne) and (self.grille_non_visible[new_x][new_y] == "?"):
                liste_indice.append((new_x, new_y))
        return liste_indice
    
    def _get_contraintes_independantes(self, contraintes):
        independent_sets = []
        for contrainte in contraintes:
            est_dans_set = False
            for contrainte_set in independent_sets:
                if any(any(c in contrainte[2] for c in autre_contrainte[2]) for autre_contrainte in contrainte_set):
                    contrainte_set.append(contrainte)
                    est_dans_set = True
                    break
            if not est_dans_set:
                independent_sets.append([contrainte])
        return independent_sets

    def _get_combinaison_valide(self, contrainte_set, mines_restante=None, combinaison_actuelle=None, indice=0, cache=None):
        if mines_restante is None:
            mines_restante = sum(contrainte[1] for contrainte in contrainte_set)
        if combinaison_actuelle is None:
            combinaison_actuelle = set()
        if cache == None:
            cache = {}
        if indice == len(contrainte_set):
            if mines_restante == 0:
                return [combinaison_actuelle]
            else:
                return []
            
        if (indice, mines_restante) in cache:
            return cache[(indice, mines_restante)]

        case, mines_restantes, cases_nn_revele = contrainte_set[indice]
        combinaisons_possible = []
        for nb_mines in range(min(mines_restantes + 1, len(cases_nn_revele) + 1)):
            for mine_combination in itertools.combinations(cases_nn_revele, nb_mines):
                new_combinaison = combinaison_actuelle.copy()
                new_combinaison.update(mine_combination)
                if len(new_combinaison) <= mines_restante:
                    combinaisons_possible.extend(self._get_combinaison_valide(contrainte_set, mines_restante - len(new_combinaison), new_combinaison, indice + 1, cache))

        cache[(indice, mines_restante)] = combinaisons_possible

        return combinaisons_possible

    def _calcul_probabilite(self):
        contraintes = []
        cases_revele = self._cases_a_verifier()
        for case in cases_revele:
            cases_nn_revele = self._get_voisins_non_revele(case)
            x, y = case
            if cases_nn_revele:
                mines_restantes = self.grille_non_visible[x][y] - sum(1 for c in cases_nn_revele if self.grille_non_visible[c[0]][c[1]] == -1)
                contraintes.append((case, mines_restantes, cases_nn_revele))

        contraintes_independantes = self._get_contraintes_independantes(contraintes)
        probabilities = {}
        for contrainte_set in contraintes_independantes:
            combinaisons_possible = self._get_combinaison_valide(contrainte_set)
            nb_combinaisons = len(combinaisons_possible)
            for combinaison in combinaisons_possible:
                for case in combinaison:
                    if case not in probabilities:
                        probabilities[case] = 1 / nb_combinaisons
                    else:
                        probabilities[case] += 1 / nb_combinaisons

        return probabilities
    
    def _case_plus_probable(self):
        probabilite = self._calcul_probabilite()
        print(probabilite)
        if probabilite:
            plus_probable = max(probabilite, key=probabilite.get)
        else:
            plus_probable = (randint(0, self.ligne-1), randint(0, self.colonne-1))
            while self.grille_non_visible[plus_probable[0]][plus_probable[1]] != "?":
                plus_probable = (randint(0, self.ligne-1), randint(0, self.colonne-1))
        return plus_probable
    


    """
    def _case_plus_probable(self):
        contraintes = self._contraintes()
        contraintes += self._intersection(contraintes)
        probabilites = self._probabilite(contraintes)
        print(probabilites)
        if probabilites:
            plus_probable = max(probabilites, key=probabilites.get)
        else:
            plus_probable = (randint(0, self.ligne-1), randint(0, self.colonne-1))
        return plus_probable
    """


if __name__ == '__main__':
    
    grille_test = Demineur()
    grille_test._cases_revele(3,7)
    grille_test._cases_revele(3,8)
    print(grille_test._cases_revele(4,7))
    print("grille normal : \n")
    grille_test._affichage("non visible")
    print("grille visible\n")
    grille_test._affichage()
    print("autour\n")
    print(grille_test._get_cases_voisins(3, 7))
    print("indice a verifier\n")
    print(grille_test._cases_a_verifier())
    print("?? : \n")
    print(grille_test._case_plus_probable())

    


