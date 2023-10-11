from enum import Enum

from attaque import Attaque
from combattant import Combattant

class Angle(Enum):
    FACE = 0
    FACE_NEGLIGEE = 1
    FLANC = 2
    MORT = 3


class Coup:
    '''
    - Attaquant : Combattant
    - Cible : Combattant
    - Attaque : Attaque
    - Angle : entier (à entrer, 0 par défaut, 0 = de face, 1 = face négligée, 2 = flancs, 3 = angle mort)
    - J20 (Jet de Dé à 20 faces) : entier (à entrer, le résultat d’un lancer de dé à 20 faces, 0 par
    défaut)
    - J10 (Jet de Dé à 10 faces) : flottant (à entrer OU calculé comme suit : J10 = J20/2)
    - J (Jet de référence) : entier (J = J10 calculé à l’excès)
    - CC (Coup Critique) : booléen (true si J10 > (10-Attaque.PCC), faux sinon)
    - BDC (Bonus de Dégâts Critiques) : entier (BDC = 0, entier Y = Attaque.PCC, entier X = 0, tant
    que CC == true :
    - X = random(1-10)
    - BDC += X
    - Y -= 1
    - Si X < 10-Y :
    - CC = false
    - JD (Jet de Dégât) : entier (JD = J+Attaque.MJD+BDC+Angle)
    - D (Distance) : entier (à entrer, 1 par défaut)
    - Elan : entier (à entrer, 0 par défaut)
    - JC (Jet Cible) : entier (à entrer, résultat d’un lancer de dé à 10 faces, 0 par défaut)
    - JE (Jet d’Esquive) : entier (JE = 0 si Cible.ESQ == 0, sinon JE = JC+(Cible.AR-30)/5) +
    Cible.ESQ-1)
    - JP (Jet de Précision) : entier (JP = J+Attaque.MJP+Attaque.BPA-Attaque.MJPD*(D-1)+Angle)
    - DGTS (Dégâts) : entier (si JE > JP ou JP < 1 : DGTS = 0, sinon DGTS = Attaque.PD(JD))
    - JH (Jet Hémorragique) : flottant (J-10+PH)
    - JETO (Jet Etourdissement) : flottant (J-10+PETO)
    - JENG (Jet Engourdissement) : flottant (J-10+PENG)
    - JAM (Jet Amputation) : flottant (J-10+PAM)
    - JES (Jet Envoi au Sol) : flottant (J-10+PES)
    - JEN (Jet Entrave) : flottant (J-10+PEN)
    - JR (Jet Recul) : flottant (J-10+PR)
    - JAS (Jet Assommage) : flottant (J-10+PAS)
    - JB (Jet Brûlure) : flottant (J-10+PB)
    - MJPAR (Modificateur de Jet de Parade) : entier (à entrer, basé sur les modificateurs de jet
    inter-armes, à 0 par défaut)

    - JPAR (Jet de Parade) : entier (JPAR = 0 si Cible.PAR <= Angle, sinon JPAR = JC + MJPAR +
    Cible.PAR-2 - max(0,Attaquant.T-Cible.T)+Cible.BPAR-Angle)
    - PRD (Pourcentage de Réduction des Dégâts) : entier (à entrer, à 100 par défaut)
    '''
    def __init__(self, cible : Combattant, attaque: Attaque):
        self.attaquant = attaque.combattant
        self.cible = cible
        self.attaque = attaque
        self.angle = 0
        self.j20 = 0

    def execute(self, j20=0, angle : Angle = Angle.FACE):
        print('--> Coup porté par %s sur %s lors d''une attaque %s' %
              (self.attaquant.nom, self.cible.nom, self.attaque.nom))
