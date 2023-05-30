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
from time import sleep

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
    QPushButton, QLabel, QMessageBox, QVBoxLayout, QLayout, QDialog, QRadioButton, QHBoxLayout
from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QFont, QIcon
from time import sleep

dict_style_boutons = {

    "bouton 0" : "QPushButton {color: white; background-color: white;}",
    "bouton 1" : "QPushButton {color: blue; background-color: white;}",
    "bouton 2" : "QPushButton {color: green; background-color: white;}",
    "bouton 3" : "QPushButton {color: red; background-color: white;}",
    "bouton 4" : "QPushButton {color: purple; background-color: white;}",
    "bouton 5" : "QPushButton {color: maroon; background-color: white;}",
    "bouton 6" : "QPushButton {color: turquoise; background-color: white;}",
    "bouton 7" : "QPushButton {color: black; background-color: white;}",
    "bouton 8" : "QPushButton {color: grey; background-color: white;}",
    "bouton bombe j1" : "QPushButton {color: red; background-color: #3f3f40;}",
    "bouton bombe j2" : "QPushButton {color: #0563fa; background-color: #3f3f40;}",
    "bouton non révelé" : "QPushButton {background-color: #a5a8a6; border: 1px solid black;}",
}

        

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
        self.tour_ia = False
        self.contre_ia:bool = True
        self.adversaire_dialog()
        self.initUI()

    def initUI(self):
        """
        Initialisation de l'interface et du démineur
        """
        self.setWindowTitle('Démineur')
        vbox = QVBoxLayout()
        vbox_child = QVBoxLayout()
        hbox = QHBoxLayout()
        self.setLayout(vbox)
        self.score_j1_label = QLabel(f"Score Joueur 1 : {self.joueur1}")
        self.score_j2_label = QLabel(f"Score Joueur 2 : {self.joueur2}")
        self.tour_label = QLabel(f"Tour du joueur 1 (Rouge)")
        self.score_j1_label.setStyleSheet("QLabel {font-size: 24px;}")
        self.score_j2_label.setStyleSheet("QLabel {font-size: 24px;}")
        self.tour_label.setStyleSheet("QLabel {font-size: 24px;}")
        vbox_child.addWidget(self.score_j1_label)
        vbox_child.addWidget(self.score_j2_label)
        hbox.addLayout(vbox_child)
        hbox.addWidget(self.tour_label)
        vbox.addLayout(hbox)

        tabgrille = self.grille_non_visible
        grille = QGridLayout()
        grille.setSpacing(2)
        
        vbox.addLayout(grille)
        for lignes in range(self.lignes):
            for colonnes in range(self.colonnes):
                button = QPushButton()
                button.setFont(QFont('Times', 15))
                button.setFixedSize(QSize(30, 30))
                button.setStyleSheet(dict_style_boutons["bouton non révelé"])
                
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

        QApplication.setWindowIcon(QIcon("logo_demineur.jpg")) #logo de l'interface
        self.show() #affichage de l'interface
    
    def adversaire_dialog(self):
        """
        Boite de dialogue pour choisir si on veut jouer contre une IA ou non.
        """
        adversaire_dialog = QDialog()
        adversaire_dialog.setWindowIcon(QIcon("logo_demineur.jpg"))
        adversaire_dialog.setWindowTitle("Séléction de l'adversaire")
        vbox = QVBoxLayout()
        vbox_menu = QVBoxLayout()

        label = QLabel("Sélectionnez l'adversaire :")
        label.setStyleSheet("QLabel {font-size: 14px;}")
        vbox.addWidget(label)

        humain = QRadioButton("Humain")
        ia = QRadioButton("IA")

        vbox_menu.addWidget(humain)
        vbox_menu.addWidget(ia)

        vbox.addLayout(vbox_menu)
        humain.setChecked(True)

        def on_button_clicked():
            """
            Action lorsqu'on valide notre choix
            """
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
                    self.tour_ia = True
            elif self.tour == 2 and button.text() == " ":
                self.tour_label.setText("Tour du Joueur 1 (Rouge)")
                self.tour = 1
                self.tour_ia = False
                
            for tuple_indice in indice_a_modif:
                for bouton in self.liste_bouton:
                    if tuple_indice == bouton[0]:
                        valeur = str(self.grille_visible[tuple_indice[0]][tuple_indice[1]])
                        bouton[1].setText(valeur)
                        bouton[1].setStyleSheet(dict_style_boutons[f"bouton {valeur}"])
                        
        else:
            if self.tour == 1 and button.text() != "*":
                self.joueur1 += 1
                self.score_j1_label.setText(f"Score Joueur 1 : {self.joueur1}")
                button.setStyleSheet(dict_style_boutons["bouton bombe j1"])
            elif self.tour == 2 and button.text() != "*":
                self.joueur2 += 1
                self.score_j2_label.setText(f"Score Joueur 2 : {self.joueur2}")
                button.setStyleSheet(dict_style_boutons["bouton bombe j2"])
                if self.contre_ia:
                    QApplication.processEvents()
                    self.tour_ia = True

            button.setText("*")

        #boucle lorsque l'ia joue plusieurs fois d'affilés
        while self.tour_ia and self.contre_ia:
            sleep(0.2)
            bouton_ia = self._tour_de_ia()
            indice_a_modif = []
            pos:tuple #tuple des coordonnées (x,y)
            for elem in self.liste_bouton:
                if bouton_ia == elem[1]:
                    pos = elem[0]
            indice_a_modif = self.demineur._cases_revele(pos[0], pos[1])

            if indice_a_modif[0] != "bombe":

                if bouton_ia.text() == " ":
                    self.tour_label.setText("Tour du Joueur 1 (Rouge)")
                    self.tour = 1
                    self.tour_ia = False
                    
                for tuple_indice in indice_a_modif:
                    for bouton in self.liste_bouton:
                        if tuple_indice == bouton[0]:
                            valeur = str(self.grille_visible[tuple_indice[0]][tuple_indice[1]])
                            bouton[1].setText(valeur)
                            bouton[1].setStyleSheet(dict_style_boutons[f"bouton {valeur}"])
            else:
                if bouton_ia.text() != "*":
                    self.joueur2 += 1
                    self.score_j2_label.setText(f"Score Joueur 2 : {self.joueur2}")
                    bouton_ia.setStyleSheet(dict_style_boutons["bouton bombe j2"])
                    self.tour_ia = True
                bouton_ia.setText("*")

            QApplication.processEvents() #force la mise a jour de l'interface

        if UI_Demineur._est_fini(self):
            UI_Demineur._fin_de_partie(self)
            QApplication.quit() #ferme tout
            return
                 
    def _est_fini(self):
        """
        Vérifie si la partie est terminé
        """
        return self.joueur1 + self.joueur2 == self.demineur.bombe #si toutes les mines ont été trouvé 
    
    def _resultat(self):
        """
        La fonction détermine le gagnant ou égalité
        """
        if self.joueur1 > self.joueur2:
            self.J_Gagnant = 1 
        elif self.joueur2 > self.joueur1:
            self.J_Gagnant = 2
        else:
            self.J_Gagnant = 0 #égalité
    
    def _fin_de_partie(self):
        """
        Affiche le message de fin avec le gagnant (ou égalité) et ferme le jeu.
        """
        UI_Demineur._resultat(self)
        msgFin = QMessageBox()
        msgFin.setWindowIcon(QIcon("logo_demineur.jpg"))
        msgFin.setIcon(QMessageBox.Information)
        if self.J_Gagnant != 0:
            msgFin.setText(f"Le gagnant est le joueur {self.J_Gagnant} avec {max(self.joueur1,self.joueur2)} points. Bravo !")
        else:
            msgFin.setText("Egalité ! Aucun gagnant.")
        msgFin.setWindowTitle("Terminé !")
        msgFin.setStandardButtons(QMessageBox.Ok)
        msgFin.exec_()
    
    def _tour_de_ia(self):
        """
        Fait jouer 1 tour a l'IA en récupérant l'indice et le bouton associé
        """
        indice_ia = self.demineur._case_plus_probable()
        return self._test_clic_ia(indice_ia)
    

    def _test_clic_ia(self, coord):
        """
        Renvoie le bouton associé aux coordonnées donné par l'IA
        """
        for i in range(len(self.liste_bouton)):
            if self.liste_bouton[i][0] == coord:
                bouton = self.liste_bouton[i][1]
        return bouton
            

def lancer_demineur(): #fonction pour importer le démineur dans d'autres fichier
                        #sans devoir importer la classe UI_Demineur
    app = QApplication(sys.argv)
    game = UI_Demineur()
    sys.exit(app.exec_())


if __name__ == '__main__':
    lancer_demineur()
    


    
