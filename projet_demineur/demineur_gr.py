from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class Demineur(QWidget):

    def __init__(self, ligne=16, colonne=16, bombe=50):
        super().__init__()
        self.ligne = ligne
        self.colonne = colonne
        self.bombe = bombe
        self.grille = [[0]*ligne for _ in range(colonne)]

        self.joueur = 1
        self.joueur2 = 1
        self.joueur1_score = 0
        self.joueur2_score = 0
        self.tour = 1
        self._initUI()

    def _initUI(self):
        """
        Initialise l'interface graphique du jeu
        """
        self.setWindowTitle("Démineur à deux joueurs")
        self.setGeometry(100, 100, 600, 400)
        
        # Ajoute une grille de boutons pour que les joueurs puissent cliquer sur les cases
        self.boutons_cases = []
        for i in range(self.ligne):
            ligne_boutons = []
            for j in range(self.colonne):
                bouton = QPushButton(self)
                bouton.setFixedSize(20, 20)
                bouton.clicked.connect(self._case_cliquee)
                ligne_boutons.append(bouton)
            self.boutons_cases.append(ligne_boutons)

        # Ajoute un label pour afficher le score des joueurs
        self.label_score = QLabel(self)
        self.label_score.setFont(QFont('Arial', 12))
        self._affichage_score()
        
        # Ajoute les éléments à la fenêtre
        vbox = QVBoxLayout()
        for ligne_boutons in self.boutons_cases:
            hbox = QHBoxLayout()
            for bouton in ligne_boutons:
                hbox.addWidget(bouton)
            vbox.addLayout(hbox)
        hbox_score = QHBoxLayout()
        hbox_score.addWidget(self.label_score)
        vbox.addLayout(hbox_score)
        self.setLayout(vbox)

        

        self._affichage()
        
        # Ajoute un bouton pour que les joueurs puissent cliquer sur une case
        self.bouton_case = QPushButton('Joueur 1', self)
        self.bouton_case.clicked.connect(self._case_cliquee)
        
        # Ajoute un label pour afficher le score des joueurs
        self.label_score = QLabel(self)
        self.label_score.setFont(QFont('Arial', 12))
        self._affichage_score()
        
        # Ajoute les éléments à la fenêtre
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_grille)
        hbox = QHBoxLayout()
        hbox.addWidget(self.bouton_case)
        hbox.addWidget(self.label_score)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def _affichage(self):
        """
        Affiche la grille visible avec toutes les bombes
        """
        chaine = ""
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.grille[i][j] == -1:
                    chaine += " *"
                else:
                    chaine += " " + str(self.grille[i][j])
            chaine += "\n"
        self.label_grille.setText(chaine)
        
    def _case_cliquee(self):
        """
        Fonction appelée lorsqu'un joueur clique sur une case
        """
        # Récupère la position de la case cliquée
        position = self.sender()
        x, y = position.pos()

        # Calcule la position de la case dans la grille
        i = (y-30) // 20
        j = x // 20

        # Vérifie si la case a déjà été cliquée
        if self.grille[i][j] == -2:
            return

        # Détermine si la case est une bombe ou non
        if self.grille[i][j] == -1:
            self.grille[i][j] = -2  # Marque la case comme étant cliquée
            if self.joueur == 1:
                self.joueur1_score += 1
            else:
                self.joueur2_score += 1
        else:
            self.grille[i][j] = -2  # Marque la case comme étant cliquée

        # Met à jour l'affichage de la grille et du score
        self._affichage()
        self._affichage_score()

        # Vérifie si toutes les cases non-bombes ont été cliquées
        if self._toutes_cases_cliquees():
            self._fin_de_partie()
        else:
            # Passe au joueur suivant
            self.tour += 1
            if self.tour % 2 == 1:
                self.joueur = 1
                self.bouton_case.setText("Joueur 1")
            else:
                self.joueur = 2
                self.bouton_case.setText("Joueur 2")
    
    def _toutes_cases_cliquees(self):
        """
        Vérifie si toutes les cases non-bombes ont été cliquées
        """
        for i in range(self.ligne):
            for j in range(self.colonne):
                if self.grille[i][j] >= 0 and self.grille[i][j] != -2:
                    return False
        return True

    def _fin_de_partie(self):
        """
        Affiche le score final et le joueur gagnant
        """
        message = "Fin de la partie !\n"
        message += "Joueur 1 : {}\n".format(self.joueur1_score)
        message += "Joueur 2 : {}\n".format(self.joueur2_score)
        if self.joueur1_score > self.joueur2_score:
            message += "Le joueur 1 gagne !"
        elif self.joueur1_score < self.joueur2_score:
            message += "Le joueur 2 gagne !"
        else:
            message += "Match nul !"
        self.label_score.setText(message)
        self.bouton_case.setDisabled(True)

    def _affichage_score(self):
        """
        Affiche le score des joueurs
        """
        message = "Score : Joueur 1 {} - Joueur 2 {}".format(self.joueur1_score, self.joueur2_score)
        self.label_score.setText(message)


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demineur = Demineur()
    demineur.show()
    sys.exit(app.exec())