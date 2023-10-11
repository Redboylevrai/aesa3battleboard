from enum import Enum

from etat import Etat


class EquipeCombattant(Enum):
    ALLIE = 1
    ENNEMI = 2

class Combattant:
    ''' TODO alimenter la classe interne labels après ce commentaire, cf usage test_prop, vider ce commentaire dans la foulée
    - Nom : chaîne de caractère (à entrer, dans le cas où un clone est ajouté les noms doivent être
    automatiquement modifiés, exemple : Gobelin 1, Gobelin 2, ...)
    - Equipe : entier (à entrer, 2 par défaut)
    - A joué : Booléen pour assurer qu’un même combattant ne peut pas jouer deux fois en un tour
    avec les changements d’initiative
    - I (Initiative) : entier (calculé : I = VR + PA*10)
    - R (Robustesse) : entier (à entrer, 45 par défaut)
    - PV (Points de Vie) : entier (PV = Robustesse par défaut ; quand PV = 0, l’unité meurt)
    - Endurance (de base) : entier (à entrer, 30 par défaut)
    - F (Force) : entier (à entrer, valeur 40 par défaut)

    - Agi (Agilité de base) : entier (à entrer, valeur 30 par défaut)
    - Vit (Vitesse de base) : entier (à entrer, valeur 30 par défaut)
    - P (Précision) : entier (à entrer, valeur 30 par défaut)
    - ET (Encombrement Total) : entier (à entrer, valeur égale à l’encombrement total des
    équipements, valeur 0 par défaut)
    - ER (Encombrement Réel) : entier (ER = ET-F/10)
    - AR (Agilité Réelle) : entier (Agi-ER)
    - VR (Vitesse Réelle) : entier (Vit-ER-RVJ)
    - ENDR (Endurance Réelle) : entier (Endurance-ER)
    - DSA (Diminution du Seuil d’Affaiblissement) : entier (DSA = max(0,(ENDR-38)/2))
    - SA (Seuil d’Affaiblissement) : flottant (valeur en pourcentage, SA = 50-DSA)
    - S (Santé) : flottant (valeur en pourcentage à 100 par défaut, S = min(100,PV*100/(SA*R/100)))

    - Buff : entier (le buff de PA, à 0 par défaut, est le nombre de PA ajouté par l’utilisateur via clic-
    gauche dans le tableau dynamique ; dans l’idéal, le nombre de PA change de couleur dans le

    tableau lorsqu’il est buffé, et redevient normal lorsqu’on annule les bonus via clic-droit)
    - PA (Points d’Action) : entier (varie en fonction de la somme AR+VR et de la Santé S :
    - PA = 1 ;
    - Si AR+VR > 4 : PA += 1 ;
    - Si AR+VR > 9 : PA += 1 ;
    - Si AR+VR > 19 : PA += 1 ;
    - Si AR+VR > 29 : PA += 1 ;
    - Si AR+VR > 44 : PA += 1 ;
    - Si AR+VR > 59 : PA += 1 ;
    - Si AR+VR > 79 : PA += 1 ;
    - Si AR+VR > 99 : PA += 1 ;
    - Si AR+VR > 119 : PA += 1 ;
    - Si AR+VR > 159 : PA += (AR+VR-120)/40 ;
    - PA = int(PA*S/100) (valeur entière arrondie par défaut)
    - PA += Buff (le buff de PA ajouté via clic-gauche dans le tableau dynamique doit être pris en
    compte APRES le recalcul des PA)
    - PAT (Points d’Action Temporaire) : entier (PAT = PA, valeur à laquelle on soustrait les PA
    utilisés pour les attaques, esquives, parades... PAT = PA au début de chaque tour)
    - PM (Points de Magie) : entier (à entrer, valeur 0 par défaut)
    - ESQ (Esquive) : entier (valeur 0, augmente de 1 par clic-gauche sur la valeur dans le tableau
    dynamique, indique le nombre de PA investis par le combattant donc chaque incrémentation
    doit diminuer les PAT)
    - PAD (Points d’Action à Déduire) : entier (valeur 0 par défaut, indique le nombre de PAT à
    déduire au début du prochain tour)
    - PESQ (Possibilités d’Esquives) : entier (2+max(0,(ENDR-20)/20) par défaut, diminuée de 1 à
    chaque esquive réussie par le Combattant)
    - PAR (Parade) : entier (valeur 0, augmente de 1 par clic-gauche sur la valeur dans le tableau
    dynamique, indique le nombre de PA investis par le combattant donc chaque incrémentation
    doit diminuer les PAT)
    - BPAR (Bonus de Parade) : entier (à entrer, dû aux capacités du combattant, 0 par défaut)
    - MJE (Modificateur de Jet d’Esquive) : entier (MJE = ESQ+(AR-30)/5 par défaut, la valeur
    (AR-30)/5 peut être négative)
    - T (Taille en hexagones) : entier (à entrer, valeur 1 par défaut)
    - PPAR (Possibilités de Parades) : entier (2+max(0,(ENDR-20)/20) par défaut, diminuée de 1 à
    chaque parade réussie par le Combattant)
    - CDH (Coût de Déplacement par Hexagone) : flottant (CDH = 30/VR, valeur à indiquer de
    manière bien visible, idéalement sous forme de fraction, dans le tableau)
    - CPF (Coût de Pivotement par Face) : flottant (CPF = 15/AR, valeur à indiquer de manière bien
    visible, idéalement sous forme de fraction, dans le tableau)
    - RES (Résistance) : entier (RES = max(0,(R-40)/10), résistance naturelle aux dégâts)
    - DDB (Diminution des Dégâts de Brûlure) : entier (valeur en pourcentage, DDB = max(0,R-50))
    - DDH (Diminution des Dégâts d’Hémorragie) : entier (valeur en pourcentage, DDB =
    max(0,R-50))
    - DJB (Diminution du Jet de Brûlure) : entier (DJB = max(0,(R-40)/15))

    - DJH (Diminution du Jet d’Hémorragie) : entier (DJH = max(0,(R-40)/20))
    - DJETO (Diminution du Jet d’Etourdissement) : entier (DJETO = max(0,(R-40)/20))
    - DJA (Diminution du Jet d’Assommage) : entier (DJA = max((R-30)/30))
    - DJENG (Diminution du Jet d’Engourdissement des attaques physiques) : flottant (DJENG =
    max(0,(R-40)/25)+max(0,(ENDR-30)/10))
    - DJEN (Diminution du Jet d’Entrave) : entier (DJEN = max(0,(F-30)/30))
    - DJEF (Diminution du Jet d’Effroi) : flottant (DJEF = max(0,(ENDR-30)/10))
    - QA (Qualité de l’Armure) : entier (à entrer, 0 par défaut)
    - PVA (Points de Vie de l’Armure) : entier (à entrer, PVA = QA*QA*10 par défaut)
    - RESPA (Résistance Perçante de l’Armure) : entier (à entrer, RESPA = QA*QA/3 par défaut)
    - RESCA (Résistance Contondante de l’Armure) : entier (à entrer, RESCA = QA*QA/3 par
    défaut)
    - RESMA (Résistance Magique de l’Armure) : entier (à entrer, RESMA = QA*QA/4 par défaut)
    - TAM (Taux d’Absorption Magique de l’armure) : entier (pourcentage à entrer, TAM = QA*10
    par défaut)
    - DJETOA (Diminution du Jet d’Etourdissement de l’Armure) : entier (valeur à entrer, DJETOA
    = max(0,QA-1) par défaut)
    - DJHA (Diminution du Jet d’Hémorragie de l’Armure) : entier (valeur à entrer, DJHA = QA*2
    par défaut)
    - DJENGA (Diminution du Jet d’Engourdissement de l’Armure) : entier (valeur à entrer,
    DJENGA = max(0,QA-2) par défaut)
    - DJRA (Diminution du Jet de Recul de l’Armure) : entier (valeur à entrer, DJRA = max(0,
    (QA-2)/2) par défaut)
    - DJBA (Diminution du Jet de Brûlure de l’Armure) : entier (valeur à entrer, DJBA = QA*2 par
    défaut)
    - DJESA (Diminution du Jet d’Envoi au Sol de l’Armure) : entier (valeur à entrer, DJESA =
    max(0,(QA-2)/2) par défaut)
    - QC (Qualité du Casque) : entier (à entrer, 0 par défaut)
    - PVC (Points de Vie du Casque) : entier (à entrer, PVC = QC*QC*10 par défaut)
    - RESPC (Résistance Perçante du Casque) : entier (à entrer, RESPC = QC*QC/3 par défaut)
    - RESCC (Résistance Contondante du Casque) : entier (à entrer, RESCC = QC*QC/3 par
    défaut)
    - RESMC (Résistance Magique du Casque) : entier (à entrer, RESMC = QC*QC/4 par défaut)
    - DJETOC (Diminution du Jet d’Etourdissement du Casque) : entier (valeur à entrer, DJETOC
    = max(0,QC-1) par défaut)
    - DJHC (Diminution du Jet d’Hémorragie du Casque) : entier (valeur à entrer, DJHC = QC*2
    par défaut)
    - DJASC (Diminution du Jet d’Assommage du Casque) : entier (valeur à entrer, DJASC =
    max(0,(QC-1)/2) par défaut)
    - DJESC (Diminution du Jet d’Envoi au Sol du Casque) : entier (valeur à entrer, DJESC =
    max(0,(QC-2)/2) par défaut)
    - QB (Qualité de la protection des Bras) : entier (à entrer, 0 par défaut)
    - PVB (Points de Vie de la protection des Bras) : entier (à entrer, PVB = QB*QB*2 par défaut)
    - RESPB (Résistance Perçante de la protection des Bras) : entier (à entrer, RESPB = QB*QB/3
    par défaut)
    - RESCB (Résistance Contondante de la protection des Bras) : entier (à entrer, RESCB =
    QB*QB/3 par défaut)
    - RESMB (Résistance Magique de la protection des Bras) : entier (à entrer, RESMB = QB*QB/
    4 par défaut)
    - DJETOB (Diminution du Jet d’Etourdissement de la protection des Bras) : entier (valeur à
    entrer, DJETOB = max(0,QB-1) par défaut)
    - DJHB (Diminution du Jet d’Hémorragie de la protection des Bras) : entier (valeur à entrer,
    DJHB = QB*2 par défaut)
    - DJAMB (Diminution du Jet d’Amputation de la protection des Bras) : entier (valeur à entrer,
    DJAMB = max(0,(QB-1)/2) par défaut)
    - DJENGB (Diminution du Jet d’Engourdissement de la protection des Bras) : entier (valeur à
    entrer, DJENGB = max(0,QB-2) par défaut)

    - QJ (Qualité de la protection des Jambes) : entier (à entrer, 0 par défaut)
    - PVJ (Points de Vie de la protection des Jambes) : entier (à entrer, PVJ = QJ*QJ*2 par défaut)
    - RESPJ (Résistance Perçante de la protection des Jambes) : entier (à entrer, RESPJ =
    QJ*QJ/3 par défaut)
    - RESCJ (Résistance Contondante de la protection des Jambes) : entier (à entrer, RESCJ =
    QJ*QJ/3 par défaut)
    - RESMJ (Résistance Magique de la protection des Jambes) : entier (à entrer, RESMJ =
    QJ*QJ/4 par défaut)
    - DJETOJ (Diminution du Jet d’Etourdissement de la protection des Jambes) : entier (valeur
    à entrer, DJETOJ = max(0,QJ-1) par défaut)
    - DJHJ (Diminution du Jet d’Hémorragie de la protection des Jambes) : entier (valeur à
    entrer, DJHJ = QJ*2 par défaut)
    - DJAMJ (Diminution du Jet d’Amputation de la protection des Jambes) : entier (valeur à
    entrer, DJAMJ = max(0,(QJ-1)/2) par défaut)
    - DJENGJ (Diminution du Jet d’Engourdissement de la protection des Jambes) : entier
    (valeur à entrer, DJENGJ = max(0,QJ-2) par défaut)
    - DJENJ (Diminution du Jet d’Entrave de la protection des Jambes) : entier (valeur à entrer,
    DJENJ = QJ/2 par défaut)
    - DJESJ (Diminution du Jet d’Envoi au Sol de la protection des Jambes) : entier (valeur à
    entrer, DJESJ = max(0,(QC-2)/2) par défaut)
    - RVJ (Réduction de la Vitesse par la protection des Jambes) : entier (valeur à entrer, RVJ =
    max(0,(QJ-4)*2) par défaut)
    - RM (Résistance à la Magie) : entier (à entrer, 0 par défaut)
    - PAAB (Points d’Action Anti-Brûlure) : entier (0 par défaut, à augmenter manuellement,
    chaque incrémentation doit diminuer les PAT de 1)
    - PDTH (Pourcentage de Diminution de l’état Torche Humaine) : entier (0 par défaut, à
    augmenter manuellement)
    - TV (Tours à Vivre) : entier (TV = 5 + max(0,(ENDR-30)/10))
    - MF (Malus de Force) : entier (0 par défaut)
    - MAgi (Malus d’Agilité) : entier (0 par défaut)
    - MP (Malus de Précision) : entier (0 par défaut)
    - HF (Humanoïde Rampant) : Booléen (à false par défaut, true si le combattant est un
    humanoïde rampant)
    - SRP (Seuil de Résistance de Parade) : entier (à entrer, 999 par défaut)
    - Etats [Etat] : tableau contenant un nombre infini d’objets Etat
    - AEtat (Etat) : booléen qui renvoie True si le tableau Etats [ ] contient Etat
    - AjouterEtat (Nom, Ampleur) : ajoute un new Etat (Nom, Ampleur) dans le tableau Etats [ ]
    - SupprimerEtat (Nom) : supprime l’Etat appelé « Nom »
    '''
    class labels:
        PV = 'Points de vie' # entier (PV = Robustesse par défaut ; quand PV = 0, l’unité meurt)
        F  = 'Force'         # entier (à entrer, valeur 40 par défaut)
        #TODO continue

    def __init__(self, nom : str, qa=0, qc=0, qb=0, qj=0): #TODO params valeurs par defaut
        self.nom = nom
        self.EquipeCombattant : EquipeCombattant.ENNEMI # équipe ennemie par défaut
        self.a_joue = False
        self.robustesse = 45
        self.endurance_base = 30
        self._sante = 100.0 #TODO make prop ; DONE mais à vérifier
        self.vitesse_base = 30
        self.agilite_base = 30
        self.encombrement_total = 0
        self.precision = 30
        self.force = 40
        self.qa = qa # Qualité de l'Armure
        self.qc = qc # Qualité du Casque
        self.qb = qb # Qualité de la protection des Bras
        self.qj = qj # Qualité de la protection des Jambes
        self.rvj = max(0, (self.qj - 4)**2)
        self.buffpa = 0
        self.pm = 0 # Points de Magie
        self.points_esquive = 0 # Points d'Action investis dans l'esquive
        self.nb_esquive = 0 # Nombre d'esquives du tour # TODO : à réinitialiser à chaque tour
        self.pad = 0 # Points d'Action à déduire, incrémentée en combat
        self.points_parade = 0 # Points d'Action investis dans la parade
        self.nb_parade = 0 # Nombre de parades du tour
        self.bonus_parade = 0
        self.taille = 1 # Taille du combattant en hexagones
        self.resistancemagique = 0
        self.paab = 0 # Points d'Action Anti-Brûlure
        self.malusforce = 0
        self.malusagilite = 0
        self.malusprecision = 0
        self.rampant = False
        self.srp = 999 # Seuil de Résistance de Parade, à 999 si sans arme
        # TODO : ajouter :
        '''
        tous les champs de diminution de dégâts ou de jets des différentes protections :
        armure principale, bras, jambes, casque...
        ayant pour valeur par défaut un calcul à partir des champs qa/qc/qb/qj,
        mais pouvant être entrés librement.
        Comment écrire ces champs ?
        '''

        self.etats = set()

    @property
    def initiative(self):
        return self.vitesse_reelle + self.points_action * 10

    @property
    def PV(self):
        "Points de vie"
        return self.robustesse
        #TODO : les PV sont égaux à la robustesse pour un combattant en pleine santé mais doivent diminuer indépendamment, comment faire ?

    @property
    def vitesse_reelle(self):
        return self.vitesse_base - self.encombrement_reel - self.rvj
    @property
    def agilite_reelle(self):
        return self.agilite_base - self.encombrement_reel
    @property
    def endurance_reelle(self):
        return self.endurance_base - self.encombrement_reel
    @property
    def points_action(self):
        pa = 1
        ar_vr = self.agilite_reelle + self.vitesse_reelle
        if ar_vr > 4: pa +=1
        if ar_vr > 9: pa +=1
        if ar_vr > 19: pa +=1
        if ar_vr > 29: pa +=1
        if ar_vr > 44: pa +=1
        if ar_vr > 59: pa +=1
        if ar_vr > 79: pa +=1
        if ar_vr > 99: pa +=1
        if ar_vr > 159: pa += (self.agilite_reelle + self.vitesse_reelle -120) / 40
            # TODO : pourquoi ne pas mettre juste (ar_vr - 120)/40 ??

        pa = int(pa * self.sante / 100)
        pa += self.buffpa # TODO ordre de calcul ??
                        # TODO le buff PA est le nb de PA ajouté manuellement par l'utilisateur, donc en dernier dans le calcul
        return pa
    @property
    def encombrement_reel(self):
        return self.encombrement_total - self.force / 10
    @property
    def dsa(self): # Diminution du Seuil d'Affaiblissement
        return max(0, (self.endurance_reelle - 38)/2)
    @property
    def sa(self): #SEUIL D'AFFAIBLISSEMENT : pourcentage de pv sous lequel la santé et les PA diminuent
        return 50 - self.dsa
    @property
    def sante(self):
        '''
        TODO commenter avec la spec
        :return:
        '''
        return min(100, self.PV*100 / (self.sa * self.robustesse / 100))
        #TODO erreur dans les spec !! corrigée ci-dessus

    ''' exemple de setter lorsqu'on veut écrire dans une property
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
    '''

    @property
    def pat(self):
        return self.points_action - self.pad
    ''' PAT = Points d'Action temporaires '''
    @property
    def pesq(self):
        return int(2 + max(0, (self.endurance_reelle - 20)/20)) - self.nb_esquive
        ''' PESQ = Possibilités d'Esquive '''
        # TODO le champ doit pouvoir être modifié indépendamment
    @property
    def mje(self):
        return int(self.points_esquive + (self.agilite_reelle - 30) / 5)
        ''' MJE = Modificateur de Jet d'Esquive '''

    @property
    def ppar(self):
        return int(2 + max(0, (self.endurance_reelle - 20) / 20)) - self.nb_parade
        ''' PPAR = Possibilités de Parade '''
        # TODO le champ doit pouvoir être modifié indépendamment
    @property
    def cdh(self):
        return 30 / self.vitesse_reelle
        ''' CDH = Coût de Déplacement par Hexagone '''
        # TODO : affichage sous forme de fraction
    @property
    def cpf(self):
        ''' CPF = Coût de Pivotement par Face '''
        return 15 / self.agilite_reelle

    def cpf_fraction(self, format=False):
        # TODO : affichage sous forme de fraction: agilite_reelle entier ou réel ?
        if format:
            return "%d/%d" % (15, self.agilite_reelle)
        return (15, self.agilite_reelle)

    @property
    def resistance(self):
        return int(max(0, (self.robustesse - 40) / 10))
        # montant de réduction naturelle des dégâts
    @property
    def ddb(self):
        return int(max(0, self.robustesse - 50))
        ''' DDB = Diminution des Dégâts de Brûlure, exprimée en pourcentage '''
    @property
    def ddh(self):
        return int(max(0, self.robustesse - 50))
        ''' DDH = Diminution des Dégâts d'Hémorragie, exprimée en pourcentage '''
    @property
    def djb(self):
        return int(max(0, (self.robustesse - 40)/15))
        ''' DJB = Diminution du Jet de Brûlure '''
    @property
    def djh(self):
        return int(max(0, (self.robustesse - 40) / 20))
        ''' DJH = Diminution du Jet d'Hémorragie '''
    @property
    def djeto(self):
        return int(max(0, (self.robustesse - 40) / 20))
        ''' DJETO = Diminution du Jet d'Etourdissement '''
    @property
    def dja(self):
        return int(max(0, (self.robustesse - 30) / 30))
        ''' DJA = Diminution du Jet d'Assommage '''
    @property
    def djeng(self):
        return int(max(0, (self.robustesse-40)/25) + max(0, (self.endurance_reelle-30)/10))
        ''' DJENG = Diminution du Jet d'Engourdissement des attaques physiques '''
    @property
    def djen(self):
        return int(max(0, (self.force - 30) / 30))
        ''' DJEN = Diminution du Jet d'Entrave '''
    @property
    def djef(self):
        return int(max(0, (self.endurance_reelle - 30) / 10))
        ''' DJEF = Diminution du Jet d'Effroi '''
    @property
    def toursavivre(self):
        return int(5 + max(0, (self.endurance_reelle - 30)/10))
        ''' Nombre de tours restant à vivre à un combattant asphyxié/pétrifié '''
        # TODO : est-ce possible de décrémenter toursavivre si c'est une property ?? le but : le combattant meurt quand toursavivre tombe à zéro
        # on peut faire un setter (cf. plus haut) avec un attribut mis à jour lors du get

    #def aEtat(self):
    #    return 0

    def ajoutEtat(self, type: str, valeur: int):
        self.etats.add(Etat.create(type, valeur))
        return (len(self.etats) > 1)  # True si il y avait déjà un état, c'est bien ça que tu veux ?
#TODO : aucune idée de comment coder ça ! renvoie True s'il y a au moins un état
#TODO : supprimerEtat

    def do_debut_tour(self):
        ''' TODO
        - ESQ & PAR réinitialisés à 0 pour le combattant
        - Changement éventuel de place dans le tableau en fonction de l’initiative pour tous les
        combattants ayant le champ « A joué » == false
        - Si Combattant.PV < 1 :
        - Pour tout Etat dans Combattants.Etats [ ] :
        - Combattant.supprimerEtat (Etat)
        - Griser ligne ?
        - Passer au combattant suivant
        - Pour tout Etat dans Combattant.Etats [ ] :
        - Si Etat.Nom == « ETO » :
        - Combattant.PAT -= Etat.Ampleur
        - Combattant.supprimerEtat (ETO)
        - Si Etat.Nom == « ENG » :
        - Combattant.PA -= Etat.Ampleur
        - Si Etat.Nom == « PD2 » :
        - Combattant.supprimerEtat(PD2)
        - Si Etat.Nom == « PETR » :
        - Combattant.R = Combattant.R*7
        - Combattant.PAT = 0
        - Combattant.TV -= 1
        - Si Etat.Nom == « EMP » :
        - Combattant.PV -= Etat.Ampleur
        - Si Etat.Nom == « BF » :
        - Combattant.PV -= Etat.Ampleur
        - Combattant.supprimerEtat(BF)
        - Si Etat.Nom == « BE » :
        - Combattant.PV -= Etat.Ampleur - 2*Combattant.PAAB
        - Etat.Ampleur -= 2*Combattant.PAAB
        - Combattant.PAAB = 0
        - Si Etat.Nom == « BTH » :
        - Combattant.PAT -= 2
        - Combattant.PV -= Etat.Ampleur*2-(Etat.Ampleur*2*PDTH/100)
        - Etat.Ampleur = Etat.Ampleur*2-(Etat.Ampleur*2*PDTH/100)
        - Si Etat.Ampleur == 0 :
        - Combattant.supprimerEtat(BTH)
        - Si Etat.Nom == « HF » :
        - Combattant.PV -= Etat.Ampleur
        - Etat.Ampleur = Etat.Ampleur/2
        - Si Etat.Nom == « HM » :
        - Combattant.PV -= Etat.Ampleur
        - Si Etat.Nom == « HI » :
        - Combattant.PV -= Etat.Ampleur*2
        - Etat.Ampleur = Etat.Ampleur*2
        - Combattant.PAT -= 2
        - Si Etat.Nom == « AS » :
        - Combattant.PAT = 0
        - Si Etat.Nom == « AV » :

        - Combattant.P -= 60
        - Si Combattant.P < 0 :
        - Combattant.P = 0
        - Si Etat.Nom == « ASPH » :
        - Combattant.TV -= 1
        - Si Combattant.Affaibli == false :
        - Combattant.MF = Combattant.F/5
        - Combattant.MAgi = Combattant.Agi/5
        - Combattant.MP -= Combattant.P/5
        - Combattant.F -= Combattant.MF
        - Combattant.Agi -= Combattant.MAgi
        - Combattant.P -= Combattant.MP
        - Combattant.Affaibli = true
        - Si Etat.Ampleur == 0 :
        - Combattant.supprimerEtat (Etat)
        - Si Combattant.TV == 0 :
        - Combattant.PV = 0
        - Si Combattant.Affaibli == true & Combattant.aEtat(ASPH) == false :
        - Combattant.F += Combattant.MF
        - Combattant.Agi += Combattant.MAgi
        - Combattant.P += Combattant.MP
        - Combattant.MF = 0
        - Combattant.MAgi = 0
        - Combattant.MP = 0
        :return:
        '''
        pass