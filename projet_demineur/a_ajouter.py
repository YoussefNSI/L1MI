def _strategie_base(self):
    cases_a_reveler = set()
    cases_a_marquer = set()
    for x in range(self.ligne):
        for y in range(self.colonne):
            if self.grille_non_visible[x][y] in range(1, 9):
                voisins = self._get_cases_voisins(x, y)
                voisins_non_reveles = [(i, j) for i, j in voisins if self.grille_non_visible[i][j] == "?"]
                voisins_marques = [(i, j) for i, j in voisins if self.grille_non_visible[i][j] == -1]
                if len(voisins_non_reveles) == self.grille_non_visible[x][y]:
                    cases_a_marquer.update(voisins_non_reveles)
                elif len(voisins_marques) == self.grille_non_visible[x][y]:
                    cases_a_reveler.update(voisins_non_reveles)
    return cases_a_reveler, cases_a_marquer


def _contraintes(self):
    indices = self._cases_a_verifier()
    liste_contraintes = []
    for x, y in indices:
        indices_voisin = self._get_cases_voisins(x, y)
        nb_bombes = 0
        cases_nn_revele = []
        for dx, dy in indices_voisin:
            if self.grille_non_visible[dx][dy] == -1:
                nb_bombes += 1
            elif self.grille_non_visible[dx][dy] == "?":
                cases_nn_revele.append((dx, dy))
        mines_restantes = self.grille_non_visible[x][y] - nb_bombes
        if mines_restantes > 0:
            contrainte = (set(cases_nn_revele), mines_restantes)
            liste_contraintes.append(contrainte)

    # Simplification des contraintes
    i = 0
    while i < len(liste_contraintes):
        j = i + 1
        while j < len(liste_contraintes):
            cases_i, mines_i = liste_contraintes[i]
            cases_j, mines_j = liste_contraintes[j]
            if cases_j.issubset(cases_i):
                cases_diff = cases_i - cases_j
                if len(cases_diff) > 0:
                    liste_contraintes[i] = (cases_diff, mines_i - mines_j)
            elif cases_i.issubset(cases_j):
                cases_diff = cases_j - cases_i
                if len(cases_diff) > 0:
                    liste_contraintes[j] = (cases_diff, mines_j - mines_i)
            j += 1
        i += 1

    return liste_contraintes

def _case_plus_probable(self):
    cases_a_reveler, cases_a_marquer = self._strategie_base()
    if cases_a_reveler:
        return random.choice(list(cases_a_reveler))
    elif cases_a_marquer:
        return None, random.choice(list(cases_a_marquer))

    contraintes = self._contraintes()
    contraintes += self._intersection(contraintes)
    if contraintes:
        probabilites = self._probabilite(contraintes)
        plus_probable = max(probabilites, key=probabilites.get)
        if plus_probable is not None:
            return plus_probable
    cases_non_revelees = [(i, j) for i in range(self.ligne) for j in range(self.colonne) if self.grille_non_visible[i][j] == "?"]
    return random.choice(cases_non_revelees)


"""
recherche profondeur limité (très couteux)
    simulation des differentes config possibles

heuristiques : estimer probabilités
    distance de Manhattan between case révelé/non révelé

optimisation du choix de la case


"""