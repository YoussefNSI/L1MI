import sys
import subprocess
import pkg_resources

#installe PyQt5 si il n'est pas présent
required = {'PyQt5'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, \
    QPushButton, QLabel, QMessageBox, QVBoxLayout, QLayout, QDialog, QRadioButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from classe_grille import Demineur

class UI_Demineur(QWidget):
    def __init__(self, lignes=16, colonnes=16):
        super().__init__()
        self.lignes = lignes
        self.colonnes = colonnes
        self.demineur = Demineur(self.lignes, self.colonnes)
        self.grille_non_visible = self.demineur.grille_non_visible
        self.grille_visible = self.demineur.grille
        self.liste_bouton = []
        self.joueur1 = 0 #score
        self.joueur2 = 0
        self.tour = 1 # le joueur 1 par défaut commence
        self.J_Gagnant = None
        self.contre_ia:bool
        self.adversaire_dialog()
        self.initUI()
        print(self.contre_ia)

    def initUI(self):
        self.setWindowTitle('Démineur')
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.score_j1_label = QLabel(f"Score Joueur 1 : {self.joueur1}")
        self.score_j2_label = QLabel(f"Score Joueur 2 : {self.joueur2}")
        self.tour_label = QLabel(f"Tour du joueur 1 (Rouge)")
        vbox.addWidget(self.score_j1_label)
        vbox.addWidget(self.score_j2_label)
        vbox.addWidget(self.tour_label)
        

        tabgrille = self.grille_non_visible
        grille = QGridLayout()
        grille.setSpacing(4)
        grille.setSizeConstraint(QLayout.SetFixedSize)
        vbox.addLayout(grille)
        for lignes in range(self.lignes):
            for colonnes in range(self.colonnes):
                button = QPushButton()
                button.setFont(QFont('Times', 15))
                button.setFixedSize(QSize(30, 30))
                
                valeur = str(tabgrille[lignes][colonnes])
                if valeur == "-1":
                    valeur = "*"
                if valeur == "?":
                    valeur = " "
                button.setText(valeur)
                self.liste_bouton.append(((lignes,colonnes),button)) #liste pour retrouver les boutons par ses coord.
                grille.addWidget(button, lignes, colonnes)
        
        for button in self.liste_bouton:
            button[1].clicked.connect(self.on_button_clicked)

        self.show()
    
    def adversaire_dialog(self):
        """
        Boite de dialogue pour choisir si on veut jouer contre une IA ou non.
        """
        adversaire_dialog = QDialog()

        vbox = QVBoxLayout()

        label = QLabel("Sélectionnez l'adversaire :")
        vbox.addWidget(label)

        humain = QRadioButton("Humain")
        ia = QRadioButton("IA")

        vbox.addWidget(humain)
        vbox.addWidget(ia)

        humain.setChecked(True)

        def on_button_clicked():
            if humain.isChecked():
                self.contre_ia = False
            else:
                self.contre_ia = True

            adversaire_dialog.done(0)

        button = QPushButton("Valider")
        button.clicked.connect(on_button_clicked)
        vbox.addWidget(button)

        adversaire_dialog.setLayout(vbox)
        adversaire_dialog.exec_()
    
    def on_button_clicked(self, button=False):
        """
        Action quand on clique sur un bouton
        """
        if not button:
            button = self.sender()
        indice_a_modif = []
        pos:tuple #tuple des coordonnées (x,y)
        for elem in self.liste_bouton:
            if button == elem[1]:
                pos = elem[0]
        indice_a_modif = self.demineur._cases_revele(pos[0], pos[1])
        if indice_a_modif[0] != "bombe":

            if self.tour == 1 and button.text() == " ":
                self.tour_label.setText("Tour du Joueur 2 (Bleu)")
                self.tour = 2
                if self.contre_ia:
                    self._tour_de_ia()
            elif self.tour == 2 and button.text() == " ":
                self.tour_label.setText("Tour du Joueur 1 (Rouge)")
                self.tour = 1
                
            for tuple_indice in indice_a_modif:
                for bouton in self.liste_bouton:
                    if tuple_indice == bouton[0]:
                        valeur = str(self.grille_visible[tuple_indice[0]][tuple_indice[1]])
                        bouton[1].setText(valeur)
        else:
            if self.tour == 1 and button.text() != "*":
                self.joueur1 += 1
                self.score_j1_label.setText(f"Score Joueur 1 : {self.joueur1}")
                button.setStyleSheet('QPushButton {color: red;}')
            elif self.tour == 2 and button.text() != "*":
                self.joueur2 += 1
                self.score_j2_label.setText(f"Score Joueur 2 : {self.joueur2}")
                button.setStyleSheet('QPushButton {color: blue;}')
                if self.contre_ia:
                    self._tour_de_ia()

            button.setText("*")

        if UI_Demineur._est_fini(self):
            UI_Demineur._fin_de_partie(self)
            QApplication.quit()
            return
                 
    def _est_fini(self):
        return self.joueur1 + self.joueur2 == self.demineur.bombe #si toutes les mines ont été trouvé 
    
    def _resultat(self):
        if self.joueur1 > self.joueur2:
            self.J_Gagnant = 1
        elif self.joueur2 > self.joueur1:
            self.J_Gagnant = 2
        else:
            self.J_Gagnant = 0
    
    def _fin_de_partie(self):
        UI_Demineur._resultat(self)
        msgFin = QMessageBox()
        msgFin.setIcon(QMessageBox.Information)
        if self.J_Gagnant != 0:
            msgFin.setText(f"Le gagnant est le joueur {self.J_Gagnant} avec {max(self.joueur1,self.joueur2)} points. Bravo !")
        else:
            msgFin.setText("Egalité ! Aucun gagnant.")
        msgFin.setWindowTitle("Terminé !")
        msgFin.setStandardButtons(QMessageBox.Ok)
        msgFin.exec_()
    
    def _tour_de_ia(self):
        indice_ia = self.demineur._case_plus_probable()
        self._test_clic_ia(indice_ia)
    

    def _test_clic_ia(self, coord):
        print(coord)
        for i in range(len(self.liste_bouton)):
            if self.liste_bouton[i][0] == coord:
                bouton = self.liste_bouton[i][1]
        self.on_button_clicked(bouton)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = UI_Demineur()
    sys.exit(app.exec_())

    
