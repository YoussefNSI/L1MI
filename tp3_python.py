import random

class IA_Demineur:
    def __init__(self, grille):
        self.grille = grille
        self.lignes = len(grille)
        self.colonnes = len(grille[0])
        self.grille_decouverte = [[False for _ in range(self.colonnes)] for i in range(self.lignes)]
        self.nb_mines = sum([ligne.count(-1) for ligne in grille])
        self.nb_cases_decouvertes = 0
        self.nb_cases_sures = 0
        self.nb_cases_mines = 0
        self.probas = [[0 for _ in range(self.colonnes)] for i in range(self.lignes)]
        self.cases_sures = []
        self.cases_mines = []
        self.cases_inconnues = []
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if grille[i][j] == -1:
                    self.cases_mines.append((i,j))
                elif grille[i][j] == 0:
                    self.cases_sures.append((i,j))
                    self.nb_cases_sures += 1
                else:
                    self.cases_inconnues.append((i,j))
        self.calculer_probas()

    def calculer_probas(self):
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.grille_decouverte[i][j]:
                    continue
                if (i,j) in self.cases_sures:
                    self.probas[i][j] = 0
                elif (i,j) in self.cases_mines:
                    self.probas[i][j] = 1
                else:
                    nb_cases_adjacentes = 0
                    nb_cases_mines_adjacentes = 0
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            if di == 0 and dj == 0:
                                continue
                            ni = i + di
                            nj = j + dj
                            if ni < 0 or ni >= self.lignes or nj < 0 or nj >= self.colonnes:
                                continue
                            if self.grille_decouverte[ni][nj]:
                                nb_cases_adjacentes += 1
                                if self.grille[ni][nj] == -1:
                                    nb_cases_mines_adjacentes += 1
                    if nb_cases_adjacentes == 0:
                        self.probas[i][j] = 0.5
                    else:
                        self.probas[i][j] = nb_cases_mines_adjacentes / nb_cases_adjacentes
                if self.probas[i][j] == 0:
                    self.cases_sures.append((i,j))
                    self.nb_cases_sures += 1
                elif self.probas[i][j] == 1:
                    self.cases_mines.append((i,j))
                    self.nb_cases_mines += 1
                else:
                    self.cases_inconnues.append((i,j))

    def jouer_coup(self):
        if self.nb_cases_decouvertes == 0:
            i, j = random.choice(self.cases_inconnues)
        else:
            max_proba = -1
            for i, j in self.cases_inconnues:
                if self.probas[i][j] > max_proba:
                    max_proba = self.probas[i][j]
                    best_case = (i,j)
            i, j = best_case
        self.grille_decouverte[i][j] = True
        self.nb_cases_decouvertes += 1
        if self.grille[i][j] == -1:
            self.nb_mines += 1
            self.nb_cases_mines += 1
            self.cases_mines.append((i,j))
            self.cases_inconnues.remove((i,j))
            return True
        elif self.grille[i][j] == 0:
            self.cases_sures.append((i,j))
            self.cases_inconnues.remove((i,j))
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or ni >= self.lignes or nj < 0 or nj >= self.colonnes:
                        continue
                    if self.grille_decouverte[ni][nj]:
                        continue
                    self.grille_decouverte[ni][nj] = True
                    self.nb_cases_decouvertes += 1
                    if self.grille[ni][nj] == -1:
                        self.nb_mines += 1
                        self.nb_cases_mines += 1
                        self.cases_mines.append((ni,nj))
                    elif self.grille[ni][nj] == 0:
                        self.cases_sures.append((ni,nj))
                        self.cases_inconnues.remove((ni,nj))
            return False
        else:
            self.cases_sures.append((i,j))
            self.cases_inconnues.remove((i,j))
            return False
