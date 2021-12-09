import random
import os
import sys


def win_or_loose(dico, nbr_erreur,):
    '''
    win_or_loose
    dev: Joseph
    date: 2021-11-27 20:52:28

    Description:
    Donne True si le joueur a gagné False si perdu

    Parametres:
        dico [dict] : clé=lettre dans le mot a deviner, valeur= une list contenant le/les indices de la clé
        nbr_erreur [int] : compte le nombre d'erreur
    Returns:
        [bool] : True= victoire, False= defaite
    '''
    # si le dico viens d'etre vider on dit que le joueur a gagné
    if dico == {}:
        return True
    # si defaite:
    if nbr_erreur >= 12:
        return False


def centrage(window, windowX, windowY):
    '''
    centrage
    dev: Joseph
    date: 2021-11-27 20:54:14

    Description:
    centre la fenetre tkinter sur l'ecran de l'utilisateur

    Parametres:
        window [class Tk object] : c'est une fenetre tkinter
        windowX [int] : largeur de la fenetre voulu
        windowY [int] : longueur de la fenetre voulu
    '''
    screenX = window.winfo_screenwidth()
    screenY = window.winfo_screenheight()
    positionX = screenX//2-windowX//2
    positionY = screenY//2-windowY//2
    window.geometry("{}x{}+{}+{}".format(windowX,
                    windowY, positionX, positionY))


def creation_pendue(canvas, windowX, windowY):
    '''
    creation_pendue
    dev: Joseph
    date: 2021-11-27 20:58:10

    Description:
    Creation d'un pendue grace a des lignes tkinter

    Parametres:
        canvas [canvas TK object] : un canvas
        windowX [int] : largeur de la fenetre tk
        windowY [int] : longueur de la fenetre tk
    Returns:
        [dict] : clé=int donnant l'ordre d'affichage de ma valeur=canvas_object(line,oval)
    '''
    # dessin du pendue dans le canvas
    base = canvas.create_line(
        50, windowY-50, windowX/2-50, windowY-50, state='hidden', fill='black', width='5')
    potence = canvas.create_line(
        50+30, windowY-50, 50+30, 50, state='hidden', fill='black', width='5')
    bar_diag = canvas.create_line(
        50+30, windowY-50-50, 50+30+50, windowY-50, state='hidden', fill='black', width='5')
    bar_haut = canvas.create_line(
        50+30-10, 50, windowX/2-100, 50, state='hidden', fill='black', width='5')
    corde = canvas.create_line(
        windowX/2-100-20, 50, windowX/2-100-20, 200, state='hidden', fill='black', width='2')
    tete = canvas.create_oval(
        windowX/2-100-20-12, 210-12, windowX/2-100-20+12, 210+12, state='hidden', fill='black', width='5', outline='black')
    tronc = canvas.create_line(
        windowX/2-100-20, 200, windowX/2-100-20, 300, state='hidden', fill='black', width='2')
    bras_droit = canvas.create_line(
        windowX/2-100-20, 220, windowX/2-100-20-30, 200+70, state='hidden', fill='black', width='2')
    bras_gauche = canvas.create_line(
        windowX/2-100-20, 220, windowX/2-100-20+30, 200+70, state='hidden', fill='black', width='2')
    jambe_droite = canvas.create_line(
        windowX/2-100-20, 300, windowX/2-100-20-30, 300+70, state='hidden', fill='black', width='2')
    jambe_gauche = canvas.create_line(
        windowX/2-100-20, 300, windowX/2-100-20+30, 300+70, state='hidden', fill='black', width='2')

    # date du pendue qui s'affichera en fct des erreurs
    pendue = {0: base, 1: potence, 2: bar_diag, 3: bar_haut, 4: corde, 5: tete,
              6: tronc, 7: bras_droit, 8: bras_gauche, 9: jambe_droite, 10: jambe_gauche}
    return pendue


def creation_dico_mot(mot):
    '''
    creation_dico_mot
    dev: Joseph
    date: 2021-11-27 21:00:24

    Description:
    cree la data (dict) sur le mot donne (cle=lettre:valeur=indice(s) de la lettre)

    Parametres:
        mot [str] : mot a faire deviner 
    Returns:
        [dict] : voir description 
    '''
    dico = {}
    for v in mot:
        dico[v] = []
    for i, v in enumerate(mot):
        dico[v].append(i)
    return dico


def creation_list_cacher(mot):
    '''
    creation_list_cacher
    dev: Joseph
    date: 2021-11-27 22:52:59

    Description:
    cree une list ou les lettres sont remplacer par des '_'.

    Parametres:
        mot [str] : le mot a "crypter"
    Returns:
        [list] : list du mot crypter
    '''
    list = []
    for i in range(len(mot)):
        list += ['_']
    return list


def verif_lettre(mot_donner, dico_deviner, list_cacher, lettre_used, nbr_erreur):
    '''
    verif_lettre
    dev: Joseph
    date: 2021-11-27 21:02:05

    Description:
    verifie si une/plusieurs lettres sont dans le mot a deviner

    Parametres:
        mot_donner [str] : mot entree par le joueur
        dico_deviner [dict] : data sur le mot/le reste du mot a deviner
        list_cacher [list] : presente les lettres qu'il reste a trouver
        lettre_used [list] : lettres deja utiliser
        nbr_erreur [int] : nombre d'erreur
    Returns:
        [multiple] : retourne les données necessaire au rapelle de cette fonction (dico, list, lettres, erreur)
    '''
    # on parcours les lettres pour les ajouter ou pas
    for l in mot_donner:
        # si la lettre est dans le mot chercher on l'ajoute a l'inconnu
        if l in dico_deviner.keys():
            for i in range(len(dico_deviner[l])):
                list_cacher[dico_deviner[l][i]] = l
            # on enleve cette lettre du dico (avec l'indice qui lui correspond)
            dico_deviner.pop(l)
            
        # si la lettre est deja utiliser on ajoute une erreur
        elif l in ''.join(lettre_used):
            nbr_erreur += 1
            # +option
        # sinon on l'ajoute aux lettres utilisées
        # si la lettre n'est pas dans le mot chercher on ajoute une erreur
        else:
            lettre_used.append(l)
            nbr_erreur += 1

    return dico_deviner, list_cacher, lettre_used, nbr_erreur


def apparition_dessin(canvas, dessin, nbr):
    '''
    apparition_dessin
    dev: Joseph
    date: 2021-11-27 21:05:14

    Description:
    fait apparaitre un dessin en fct d'un nombre

    Parametres:
        canvas [tk canvas object] : canvas au quel appartient le dessin
        dessin [dico] : clé=ordre d'apparition : valeur=morceau de dessin
        nbr_erreur [int] : donne le nombre de morceau du dessin a faire apparaitre
    '''
    for i in range(nbr):
        try:
            canvas.itemconfig(dessin[i], state='normal')
        except KeyError:
            pass


def choix_diff(diff, dict_mots):
    '''
    choix_diff
    dev: Joseph
    date: 2021-11-28 12:01:11

    Description:
    return un mot et sa data en fonction de la diff donner

    Parametres:
        diff [int] : difficulté choisi
        dict_mots [dict] : [description]
        mot_deviner [[type]] : [description]
    Returns:
        [[type]] : [description]
    '''
    if not diff.isdigit():
        diff = ''
        return 'not digit'
    try:
        mot_deviner = dict_mots[diff][random.randint(
            0, len(dict_mots[diff])-1)].lower()
        dico_deviner = creation_dico_mot(mot_deviner)
        list_cacher = creation_list_cacher(mot_deviner)
    except KeyError:
        return 'KeyError'
    return mot_deviner, dico_deviner, list_cacher


def replay(restart):
    '''
    replay
    dev: Joseph
    date: 2021-12-09 08:35:45

    Description:
    permet de rejouer
    '''
    if restart.upper() == "YES":
        os.execl(sys.executable, sys.executable, * sys.argv)
    else:
        sys.exit()
