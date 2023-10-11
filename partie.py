from typing import List

from combattant import Combattant

'''
- Un tableau dynamique interactif, qui évolue en temps réel et fait apparaître les données utiles à
la compréhension du combat par les joueurs (une classe Tableau ayant pour données membres
une liste de Combattants, un compteur de tours...)
- Dans l’idéal, on peut incrémenter/décrémenter de 1 les données du tableau par un clic
gauche/clic droit, ce qui modifie dynamiquement les données de l’objet
- 1 ligne = 1 combattant, dans l’idéal les lignes changent de place en fonction de l’initiative (si
deux combattants ont la même initiative, celui qui possède le plus de PV commence avant
l’autre)
- Possibilité de savoir à qui est le tour et de passer au joueur suivant via un bouton, dans
l’idéal de zapper automatiquement les joueurs morts (à 0 PV ou moins) (et de griser leurs
lignes), et de connaître le numéro du tour en cours
- Possibilité du Ctrl+Z, Ctrl+Y (memento)
- Possibilité d’ajouter ou de supprimer facilement des combattants
- Registre de sauvegarde de combattants pour mémoriser leurs stats à partir du nom d’un
combat sur l’autre (pour chaque combattant : une version « vierge », avec les stats tels qu’au
moment de la création, + une ou plusieurs versions sauvegardées avec les stats modifiées)
- Possibilité de réinitialiser un tableau, de le sauvegarder avec son historique, de stocker les
données des combattants et des attaques créés
- Une classe Combattant, la possibilité de créer facilement et rapidement de nouveaux objets
combattant via un formulaire accessible depuis l’interface utilisateur ( + dupliquer, + modifier)
- De très nombreux champs sont à implémenter pour cette classe, la plupart d’entre eux
doivent évoluer dynamiquement en fonction d’autres champs, les autres doivent être
renseignés mais ont une valeur par défaut
- Une classe Attaque, chaque combattant possédant une sélection d’attaques différentes, la
possibilité de créer facilement de nouveaux objets Attaque attribués à un ou plusieurs
Combattant (chaque objet Attaque pointe vers un parent Combattant dont elle connaît les
champs) via un formulaire accessible depuis l’interface utilisateur (+ dupliquer, + modifier)
- Une classe Coup pour modifier les données du combat en faisant appel à 1 Combattant
attaquant, 1 Combattant cible et 1 Attaque (parmi les attaques attribuées au Combattant
attaquant, à sélectionner via un menu déroulant ; l’objet Coup doit être créé puis détruit via un
formulaire/fenêtre de l’interface utilisateur pour modifier le tableau dynamique en temps réel)
- Un bouton « go ! » pour lancer le calcul
- Un bouton « ok » pour réinitialiser le formulaire afin de pouvoir entrer un nouveau coup
- Une classe Etat pour implémenter les règles de changements induits sur les données des
combattants en fonction des Etats et du temps, chaque Combattant peut avoir un nombre
illimité d’états
Les champs qui apparaissent dans l’interface :
- Les champs visibles dans l’interface de base, le tableau dynamique et la fenêtre « coup » : les
champs en couleur (rouge tableau dynamique, bleu fenêtre « coup »)
- Dans le menu déroulant servant à créer un objet (combattant ou attaque) : tous les champs
annotés « à entrer » de chacune de ces classes
- Dans le menu déroulant servant à modifier un objet : tous les champs de cet objet (combattant
ou attaque)
'''

class Partie:
    def __init__(self, nom : str):
        self.nom = nom
        self.combattants : List[Combattant] = []

    def do_debut_tour(self):
        ''' TODO
        - Initiative réinitialisée pour tous les Combattants
        - PAT -= PAD pour tous les Combattants
        - I += PAT*10 pour tous les Combattants
        - I -= PAD*10 pour tous les Combattants
        - PAT = PA-PAD pour tous les Combattants
        - Si PESQ < 1 : PAT -= ESQ et I -= ESQ*10 pour tous les Combattants
        - Si PPAR < 1 : PAT -= PAR/2 (division par excès) et I -= PAR*5 pour tous les Combattants
        - PESQ réinitialisée pour tous les Combattants à 2+max(0,(ENDR-20)/20)
        - PPAR réinitialisée pour tous les Combattants à 2+max(0,(ENDR-20)/20)
        - PAD réinitialisé à 0 pour tous les Combattants
        :return:
        '''
        pass
