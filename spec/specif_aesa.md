# AESA III - Tableau dynamique interactif de combat #

Il nous faut :
- Un tableau dynamique interactif, qui évolue en temps réel et fait apparaître les données utiles à
la compréhension du combat par les joueurs (une classe Tableau ayant pour données membres
une liste de Combattants, un compteur de tours…)
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
### Les champs qui apparaissent dans l’interface :
- Les champs visibles dans l’interface de base, le tableau dynamique et la fenêtre « coup » : les
champs en couleur (rouge tableau dynamique, bleu fenêtre « coup »)
- Dans le menu déroulant servant à créer un objet (combattant ou attaque) : tous les champs
annotés « à entrer » de chacune de ces classes
- Dans le menu déroulant servant à modifier un objet : tous les champs de cet objet (combattant
ou attaque)
### Les champs de la classe Combattant :
  - `Nom` : chaîne de caractère (à entrer, dans le cas où un clone est ajouté les noms doivent être
  automatiquement modifiés, exemple : Gobelin 1, Gobelin 2, …)
  - Equipe : entier (à entrer, 2 par défaut)
  - A joué : Booléen pour assurer qu’un même combattant ne peut pas jouer deux fois en un tour
avec les changements d’initiative
  - `I (Initiative)` : entier (calculé : I = VR + PA*10)
  - R (Robustesse) : entier (à entrer, 45 par défaut)
  - PV (Points de Vie) : entier (PV = Robustesse par défaut ; quand PV = 0, l’unité meurt)
  - Endurance (de base) : entier (à entrer, 30 par défaut)
  - `F (Force)` : entier (à entrer, valeur 40 par défaut)
  - `Agi (Agilité de base)` : entier (à entrer, valeur 30 par défaut)
  - `Vit (Vitesse de base)` : entier (à entrer, valeur 30 par défaut)
  - P (Précision) : entier (à entrer, valeur 30 par défaut)
  - `ET (Encombrement Total)` : entier (à entrer, valeur égale à l’encombrement total des
équipements, valeur 0 par défaut)
  - `ER (Encombrement Réel)` : entier (ER = ET-F/10)
  - `AR (Agilité Réelle)` : entier (Agi-ER)
  - `VR (Vitesse Réelle)` : entier (Vit-ER-RVJ)
  - ENDR (Endurance Réelle) : entier (Endurance-ER)
  - DSA (Diminution du Seuil d’Affaiblissement) : entier (DSA = max(0,(ENDR-38)/2))
  - SA (Seuil d’Affaiblissement) : flottant (valeur en pourcentage, SA = 50-DSA)
  - `S (Santé)` : flottant (valeur en pourcentage à 100 par défaut, S = max(100,PV/R*SA))
  - Buff : entier (le buff de PA, à 0 par défaut, est le nombre de PA ajouté par l’utilisateur via clicgauche
dans le tableau dynamique ; dans l’idéal, le nombre de PA change de couleur dans le
tableau lorsqu’il est buffé, et redevient normal lorsqu’on annule les bonus via clic-droit)
  - `PA (Points d’Action)` : entier (varie en fonction de la somme AR+VR et de la Santé S :
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
utilisés pour les attaques, esquives, parades… PAT = PA au début de chaque tour)
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
  - MF (Malus de Précision) : entier (0 par défaut)
  - HF (Humanoïde Rampant) : Booléen (à false par défaut, true si le combattant est un
humanoïde rampant)
  - SRP (Seuil de Résistance de Parade) : entier (à entrer, 999 par défaut)
  - Etats [Etat] : tableau contenant un nombre infini d’objets Etat
  - AEtat (Etat) : booléen qui renvoie True si le tableau Etats [ ] contient Etat
  - AjouterEtat (Nom, Ampleur) : ajoute un new Etat (Nom, Ampleur) dans le tableau Etats [ ]
  - SupprimerEtat (Nom) : supprime l’Etat appelé « Nom »

###Les champs de la classe Attaque :
- `Nom` : chaîne de caractère
- `Combattant` : L’objet Combattant à qui est attribuée cette attaque
- `PA (Points d’Action)` : entier (à entrer, le coût en PA de l’attaque)
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
3 = magique inné, 4 = sortilège…)
- Zone : entier (à entrer, 0 par défaut, 0 = non-ciblé, 1 = tête, 2 = bras, 3 = jambes)

###Les champs de la classe Etat :
- `Nom` : chaîne de caractères permettant d’identifier l’état
- `Ampleur` : entier permettant de mesurer les effets de l’état

### Les champs de la classe Coup :
- `Attaquant` : Combattant
- `Cible` : Combattant
- `Attaque` : Attaque
- `Angle` : entier (à entrer, 0 par défaut, 0 = de face, 1 = face négligée, 2 = flancs, 3 = angle mort)
- `J20` (Jet de Dé à 20 faces) : entier (à entrer, le résultat d’un lancer de dé à 20 faces, 0 par
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
- Coup() : fonction :
  - Si Cible.aEtat(BF) :
  - JD += 1
  - Si Cible.aEtat(BE) :
  - JD += 2
  - Si Attaquant.aEtat(BE) :
  - JP -= 2
  - Si Cible.aEtat(BTH) :
  - JD += 5
  - JE -= 5
  - Si Attaquant.aEtat(BTH) :
  - JP - =5
  - Si (JD < 1 OU JP < 1) & D==1 :
  - Attaque.Q -= 1
  - Si Cible.aEtat(HI) :
  - JE -= 6
  - Si Attaque.type < 2 :
  - JD += 4
  - Si Attaquant.aEtat(HI) :
  - JP -= 4
  - Si Attaquant.aEtat(ES) :
  - JP -= 4
  - Si D == 1 :
  - JD -= 5
  - Attaque.PA += 2
  - Si Cible.aEtat(ES) :
  - JE = JE/2
  - JPAR = 0
  - Si Attaquant.aEtat(AMB) :
  - JP -= 2
  - Si Cible.aEtat(AMB) :
  - JPAR -= 3
  - JE -= 2
  - Si JPAR < 0 :
  - JPAR = 0
  - Si JE < 0 :
  - JE = 0
  - Si Cible.aEtat(PD2) & JPAR > 0 : JPAR = JPAR/2 (division par excès)
  - Si Elan > 0 & D == 1 :
  - JP -= min(Attaque.PPE, Elan)
  - JD += min(Attaque.PPE, Elan)
  - JP += max(0, (Attaquant.VR-30)/10))
  - JD += max(0, (Attaquant.VR-30)/10))
  - Si Attaque.type == 0 :
  - JR += min(Attaque.PPE, Elan)/2
  - Si PRD ≠ 100 :
  - DGTS = DGTS*PRD/100
  - Si DGTS > 0 & JP > JE & JD > JPAR-3 & JP > 0 :
  - Cible.ESQ -= 3
  - Si JPAR >= JD :
  - DGTS = DGTS/2
  - JH = 0
  - JETO = 0
  - JENG = 0
  - JAM = 0
  - JES = 0
  - JEN = 0
  - JR = 0
  - JAS = 0
  - JB = 0
  - Cible.ajouterEtat(PD2)
  - Sinon :
  - Cible.PAR = 0
  - Si Attaque..zone == 0 :
  - Si Attaque.type == 0 :
  - Tant que Cible.PVA ≠ 0 & DGTS > Cible.RESCA :
  - Cible.PVA -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESCA
  - Si Attaque.type == 1 :
  - Tant que Cible.PVA ≠ 0 & DGTS > Cible.RESPA :
  - Cible.PVA -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESPA
  - Si Attaque.type > 1 :
  - Tant que Cible.PVA ≠ 0 & DGTS*Cible.TAM/100 > Cible.RESMA :
  - Cible.PVA -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESMA
  - JH -= Cible.DJHA
  - JETO -= Cible.DJETOA
  - JENG -= Cible.DJENGA
  - JES -= Cible.DJESA
  - JR -= Cible.DJRA
  - JB -= Cible.DJBA
  - Si Attaque..zone == 1 :
  - Si Attaque.type == 0 :
  - Tant que Cible.PVC ≠ 0 & DGTS > Cible.RESCC :
  - Cible.PVC -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESCC
  - Si Attaque.type == 1 :
  - Tant que Cible.PVC ≠ 0 & DGTS > Cible.RESPC :
  - Cible.PVC -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESPC
  - Si Attaque.type > 1 :
  - Tant que Cible.PVC ≠ 0 & DGTS > Cible.RESMC :
  - Cible.PVC -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESMC
  - JH -= Cible.DJHC
  - JETO -= Cible.DJETOC
  - JES -= Cible.DJESC
  - JAS -= Cible.DJASC
  - Si Attaque..zone == 2 :
  - Si Attaque.type == 0 :
  - Tant que Cible.PVB ≠ 0 & DGTS > Cible.RESCB :
  - Cible.PVB -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESCB
  - Si Attaque.type == 1 :
  - Tant que Cible.PVB ≠ 0 & DGTS > Cible.RESPB :
  - Cible.PVB -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESPB
  - Si Attaque.type > 1 :
  - Tant que Cible.PVB ≠ 0 & DGTS > Cible.RESMB :
  - Cible.PVB -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESMB
  - JH -= Cible.DJHB
  - JETO -= Cible.DJETOB
  - JENG -= Cible.DJENGB
  - JAM -= Cible.DJAMB
  - Si Attaque..zone == 3 :
  - Si Attaque.type == 0 :
  - Tant que Cible.PVJ ≠ 0 & DGTS > Cible.RESCJ :
  - Cible.PVJ -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESCJ
  - Si Attaque.type == 1 :
  - Tant que Cible.PVJ ≠ 0 & DGTS > Cible.RESPJ :
  - Cible.PVJ -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESPJ
  - Si Attaque.type > 1 :
  - Tant que Cible.PVJ ≠ 0 & DGTS > Cible.RESMJ :
  - Cible.PVJ -= 1
  - DGTS -= 1
  - DGTS -= Cible.RESMJ
  - JH -= Cible.DJHJ
  - JETO -= Cible.DJETOJ
  - JENG -= Cible.DJENGJ
  - JAM -= Cible.DJAMJ
  - JEN -= Cible.DJENJ
  - JES -= Cible.DJESJ
  - Si Attaque.type == 3 : DGTS -= DGTS*RM/200
  - Si Attaque.type == 4 : DGTS -= DGTS*RM/100
  - DGTS -= Cible.RES
  - JH -= Cible.DJH
  - JETO -= Cible.DJETO
  - JENG -= Cible.DJENG
  - JAM -= Cible.DJAM
  - JR -= Cible.DJR
  - Si Cible.T > 1 :
  - JR -= T+2
  - Si Cible.HR :
  - JR -= 3
  - Si Cible.aEtat (ES) :
  - JD += JR
  - JR = JR/4
  - JES -= Cible.DJES
  - JEN -= Cible.DJEN
  - JAS -= Cible.DJAS
  - JB -= Cible.DJB
  - Si DGTS > 0 :
  - Cible.PV -= DGTS
  - Si JH == 1 & not(Cible.aEtat (HM)) & not(Cible.aEtat (HI)) :
  - Si pour tout Etat dans Cible.Etats[ ] Etat == HF & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDH/100) :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (HF, entier(DGTS-DGTS*Cible.DDH/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == HF & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDH/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (HF, entier(DGTS-DGTS*Cible.DDH/100))
  - Si JH == 2 & not(Cible.aEtat (HI)) :
  - Si pour tout Etat dans Cible.Etats[ ] (Etat == HM & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDH/100)) ou Etat == HF :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (HM, entier(DGTS-DGTS*Cible.DDH/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == HM & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDH/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (HM, entier(DGTS-DGTS*Cible.DDH/100))
  - Si JH > 2 :
  - Si pour tout Etat dans Cible.Etats[ ] (Etat == HI & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDH/100)) ou Etat == HF ou Etat == HM :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (HI, entier(DGTS-DGTS*Cible.DDH/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == HI & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDH/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (HI, entier(DGTS-DGTS*Cible.DDH/100))
  - Si JB == 1 & not(Cible.aEtat (BE)) & not(Cible.aEtat (BTH)) :
  - Si pour tout Etat dans Cible.Etats[ ] Etat == BF & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDB/100) :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (BF, entier(DGTS/2-DGTS*Cible.DDB/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == BF & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDB/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (BF, entier(DGTS-DGTS*Cible.DDB/100))
  - Si JB == 2 & not(Cible.aEtat (BTH)) :
  - Si pour tout Etat dans Cible.Etats[ ] (Etat == BE & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDB/100)) ou Etat == BF :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (BE, entier(DGTS-DGTS*Cible.DDB/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == BE & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDB/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (BE, entier(DGTS-DGTS*Cible.DDB/100))
  - Si JB > 2 :
  - Si pour tout Etat dans Cible.Etats[ ] (Etat == BTH & Etat.Ampleur <= entier(DGTSDGTS*
  Cible.DDB/100)) ou Etat == BF ou Etat == BE :
  - Cible.supprimerEtat (Etat)
  - Cible.ajouterEtat (BTH, entier(DGTS-DGTS*Cible.DDB/100))
  - Sinon si pour tout Etat dans Cible.Etats[ ] Etat == BTH & Etat.Ampleur > entier(DGTSDGTS*
  Cible.DDB/100) :
  - Ne rien faire
  - Sinon :
  - Cible.ajouterEtat (BTH, entier(DGTS-DGTS*Cible.DDB/100))
  - Sinon :
  - Attaque.SPT -= Attaque.PD
  - Si Attaque.SPT < 1 :
  - Attaque.Q -= 1
  - Attaque.SPT = Attaque.SP
  - Attaquant.PAT -= Attaque.PA
  - Si JENG > 0 & JAM <= 0 :
  - Cible.ajouterEtat (ENG, min(Attaque.PPAM, JENG))
  - Si JETO > 0 & Cible.aEtat(ENG) == false :
  - Si CC == true : Attaque.PPAM += 1
  - Cible.ajouterEtat (ETO, min(Attaque.PPAM, JETO))
  - Attaque.PPAM -= 1
  - Si JAM > 0 :
  - Si Attaque.zone == 2 :
  - Cible.ajouterEtat (AMB)
  - Si Attaque.zone == 3 :
  - Cible.ajouterEtat(AMJ)
  - Si Cible.aEtat(ES) == false :
  - Cible.ajouterEtat (ES)
  - Si Cible.aEtat(EN) == false :
  - Cible.ajouterEtat (EN)
  - Si JR > 1 & Cible.aEtat (ES) == false :
  - Cible.ajouterEtat (ES)
  - Si JEN > 0 & Cible.aEtat (EN) == false :
  - Cible.ajouterEtat (EN)
  - Si JAS > 0 :
  - Cible.ajouterEtat (AS)
  - Si Cible.aEtat (ES) == false :
  - Cible.ajouterEtat(ES)
  - Si JE >= JP :
  - DGTS = 0
  - Cible.PESQ -= 1
  - Si Cible.PESQ == 0 : Cible.PAD += Cible.ESQ
  - Si JPAR > JD+2 :
  - DGTS = 0
  - Cible.PPAR -= 1
  - Si Cible.PPAR == 0 : Cible.PAD += (Cible.PAR)/2 (division par excès)
  - Si DGTS > Cible.SRP & Cible.PAR > 0 :
  - Cible.SRP = 0
  - Si Attaque.Nom == « prise » :
  - Si (Attaquant.PA - Attaquant.PAT) >= 2*(Cible.ESQ + Cible.PAR + Cible.I/10 - Cible.PA -
  Cible.VR/10) :
  - Attaquant.ajouterEtat(IMMO)
  - Cible.ajouterEtat(IMMO)
  - Si Attaque.Nom == « lutte » :
  - J += Attaquant.F/5 + Attaquant.PASI
  - JC += Cible.F/5 + Cible.PA
    
### En début de tour :
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

### Au début du tour d’un combattant :
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