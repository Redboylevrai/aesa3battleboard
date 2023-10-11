from enum import Enum

from combattant import Combattant


class ZoneAttaque(Enum):
    NON_CIBLE = 0
    TETE = 1
    BRAS = 2
    JAMBE = 3


class Attaque:
    ''' TODO
    - Nom : chaîne de caractère
    - Combattant : L’objet Combattant à qui est attribuée cette attaque
    - PA (Points d’Action) : entier (à entrer, le coût en PA de l’attaque)
    - Q (Qualité de l’arme) : entier (à entrer, 0 par défaut, peut être diminuée par clic-droit si
    supérieure à 0)
    - PD (entier JD) (Potentiel de Dégât) : entier (calcul différent selon l’attaque, dépend de Q, de
    JD et de Combattant.F généralement)
    - MJD (Modificateur de Jet de Dégât) : entier (à entrer, 0 par défaut, intrinsèque à l’attaque
    mais peut varier selon le combattant, peut être augmenté/diminué via clic-gauche dans
    l’interface)
    - MJP (Modificateur de Jet de Précision) : entier (à entrer, 0 par défaut, intrinsèque à l’attaque)
    - BPA (Bonus de Précision de l’Attaquant) : entier (BPA = (Combattant.P-30)/5)
    - MJPD (Malus de Jet de Précision par Distance) : entier (à entrer, 0 par défaut)
    - PCC (Probabilité de Coup Critique) : flottant (à entrer, PCC = 1 par défaut)
    - PH (Probabilité Hémorragique) : flottant (à entrer, 0 par défaut)
    - PETO (Probabilité d’Etourdissement) : flottant (à entrer, 0 par défaut)
    - PENG (Probabilité d’Engourdissement) : flottant (à entrer, 0 par défaut)

    - PAM (Probabilité d’Amputation) : flottant (à entrer, 0 par défaut)
    - PES (Probabilité d’Envoyer au Sol) : flottant (à entrer, 0 par défaut)
    - PEN (Probabilité d’Entraver) : flottant (à entrer, 0 par défaut)
    - PR (Probabilité de Recul) : flottant (à entrer, 0 par défaut)
    - PAS (Probabilité d’Assommer) : flottant (à entrer, 0 par défaut)
    - PB (Probabilité de Brûlure) : flottant (à entrer, 0 par défaut)
    - PASI (Points d’Action Supplémentaires Investis) : entier (à entrer, 0 par défaut)
    - PPAM (Perte de Points d’Action Maximale) : entier (à entrer, 100 par défaut)
    - SP (Seuil de Préservation de l’arme) : entier (à entrer, 100 par défaut, peut dépendre du
    champ Q dans les autres cas)
    - SPT (Seuil de Préservation de l’arme Temporaire) : entier (à entrer, SPT = SP par défaut)
    - PPE (Potentiel de Prise d’Elan) : entier (à entrer, 0 par défaut)
    - Reset ( ) : fonction pour réinitialiser la valeur SP en fonction de Q
    - Type : entier (à entrer, 0 par défaut, 0 = contondant, 1 = perçant, 2 = élémentaire non-magique,
    3 = magique inné, 4 = sortilège...)
    - Zone : entier (à entrer, 0 par défaut, 0 = non-ciblé, 1 = tête, 2 = bras, 3 = jambes)
    zone : ZoneAttaque = ZoneAttaque.NON_CIBLE
    '''

    def __init__(self, nom : str, pa : int, combattant : Combattant = None):
        self.nom = nom
        self.PA = pa
        self.combattant = combattant

class AttaqueTete(Attaque):
    zone = ZoneAttaque.TETE

class AttaqueBras(Attaque):
    zone = ZoneAttaque.BRAS

class AttaqueJambe(Attaque):
    zone = ZoneAttaque.JAMBE
