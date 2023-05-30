from ui_demineur import lancer_demineur

lancer_demineur()
"""
<p><br><br><br>Pour la page d'explications sur le développement vous prendrez le temps d'expliquer 
            les choix effectués pour l'interface graphique et les différentes IA implantées (modules, fonctions implantées, ...).
             Vous pourrez mettre en avant les difficultés ainsi que les points que vous pensez intéressants.</p>


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


"""            



