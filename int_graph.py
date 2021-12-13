import tkinter as tk
from tkinter import messagebox
import fct_pendue as fctp
import json

# on recupere les mots du json
with open('mots_fr.json', 'r') as file:
    data = file.read()
dict_mots = json.loads(data)

# creation de la fenetre tkinter
window = tk.Tk()
window.title('Pendue')
window['bg'] = 'white'

# centrage de la fenetre
windowX = 640
windowY = 470
fctp.centrage(window, windowX, windowY)

# creation des deux cotes: droite = mot + input, gauche= dessin pendue
frame_right = tk.Frame(window, relief='groove',
                       width=windowX/2, height=windowY)
canvas_pendue = tk.Canvas(window, relief='groove',
                          bg='white', width=windowX/2, height=windowY)
canvas_pendue.grid(row=1, column=0)
frame_right.grid(row=1, column=1)
# frame_right.grid_propagate(0)
frame_right.grid_columnconfigure(1, minsize=windowX/2)
# dessin du pendue dans le canvas
pendue = fctp.creation_pendue(canvas_pendue, windowX, windowY)

# initialisationdes variables
lettres_used = []
nbr_erreur = 0
dico_deviner = {}
list_cacher = []

# creation affichage du mot cacher et input des lettres
tk.Label(frame_right, text='Choisissez une difficulté entre 4 et 11 (longeur du mot)')

diff = tk.StringVar()
entry_diff = tk.Entry(frame_right, textvariable=diff)
entry_diff.grid(row=5, column=1)

tk.Label(frame_right, text='voici le mot a trouver: ').grid(
    row=6, column=1, sticky='s')

label_cacher = tk.Label(frame_right, text=''.join(
    list_cacher))
label_cacher.grid(row=7, column=1)

tk.Label(frame_right, text='lettres utilisé: ').grid(row=8, column=1)

label_lettres_used = tk.Label(frame_right, text=''.join(lettres_used))
label_lettres_used.grid(row=9, column=1)

input_lettres = tk.StringVar()
entry_lettres = tk.Entry(
    frame_right, textvariable=input_lettres)
entry_lettres.grid(row=10, column=1)


def choix_diff(event):
    global dict_mots, mot_deviner, dico_deviner, list_cacher
    diff = entry_diff.get()
    return_diff = fctp.choix_diff(diff, dict_mots)
    if return_diff == 'not digit':
        messagebox.showinfo(
            'Erreur', "Entrez un nombre entre 4 et 11 svp")
        entry_diff.delete(0, len(diff))
        entry_diff.focus_force()
    elif return_diff == 'Error':
        messagebox.showinfo(
            'Erreur', "Entrez un nombre entre 4 et 11 svp")
        entry_diff.delete(0, len(diff))
        entry_diff.focus_force()
    else:
        mot_deviner, dico_deviner, list_cacher = return_diff
        label_cacher.config(text=' '.join(list_cacher))
        entry_lettres.focus_set()


def update(event):
    '''
    update
    dev: Joseph
    date: 2021-11-27 21:09:09

    Description:
    recupere les lettres entree par la joueur et fait les modifcations en concequences

    Parametres:
        event [event] : [description]
    '''
    global dico_deviner, list_cacher, lettres_used, nbr_erreur
    mot_donner = entry_lettres.get().lower()

    # si le dico a dico a deviner est deja vide on ferme l'app
    if dico_deviner == {}:
        messagebox.showinfo(
            'Mot vide', "Vous n'avez pas de mot à deviner, la cession va se fermer")
        window.destroy()

    # verification de l'input mot_donner
    if not mot_donner.isalpha() or mot_donner == '':
        messagebox.showinfo(
            'Erreur', "Veuillez rentrer que des lettres")
        entry_lettres.delete(0, len(mot_donner))
        entry_lettres.focus_force()
    else:
        dico_deviner, list_cacher, lettres_used, nbr_erreur = fctp.verif_lettre(
            mot_donner, dico_deviner, list_cacher, lettres_used, nbr_erreur)
        entry_lettres.delete(0, len(mot_donner))

    # apparition du pendue:
    fctp.apparition_dessin(canvas_pendue, pendue, nbr_erreur)

    # win or loose en fct des données:
    w_or_l = fctp.win_or_loose(dico_deviner, nbr_erreur)
    if w_or_l == True:
        messagebox.showinfo(
            'Bravo', 'Vous avez gagnez! Le mot à deviner était: ' + mot_deviner.upper() + '. Bien jouer!')
        restart = messagebox.askquestion('Rejouer ?', 'Voulez vous rejouer? ')
        fctp.replay(restart)
    if w_or_l == False:
        messagebox.showinfo(
            'Perdu', ('Le mot a deviner était: ' + mot_deviner.upper() + '. \n Dommage!'))
        restart = messagebox.askquestion('Rejouer ?', 'Voulez vous rejouer? ')
        fctp.replay(restart)

    # modification des labels qui ont changé:
    label_cacher.config(text=' '.join(list_cacher))
    label_lettres_used.config(text=' '.join(lettres_used))


entry_lettres.bind('<Return>', update)
entry_diff.bind('<Return>', choix_diff)

entry_diff.focus_set()
window.mainloop()
