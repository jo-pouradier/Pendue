import fct_pendue as fctp
import json

dico_deviner = {}
list_cacher = []
lettres_used = []
nbr_erreur = 0

# on recupere les mots du json
with open('mots_fr.json', 'r') as file:
    data = file.read()
dict_mots = json.loads(data)

# input de la diff:


def choix_difficulte():
    '''
    choix_diff
    dev: Joseph
    date: 2021-11-28 11:25:38

    Description:
    choix de la diff de jeu

    Returns:
        [multiple] : retourne la data modifiée
    '''
    dico_deviner = {}
    list_cacher = []
    diff = input('Entrez une difficulté entre 4 et 11 svp. ')
    return_diff = fctp.choix_diff(diff, dict_mots)
    if return_diff == 'not digit':
        print("Erreur, vous n'avez pas entré un nombre. ")
        return choix_difficulte()
    elif return_diff == 'Error':
        print('\n Un chiffre entre 4 et 11 svp : ')
        return choix_difficulte()
    else:
        mot_deviner, dico_deviner, list_cacher = return_diff
    return mot_deviner, dico_deviner, list_cacher


print('\n')


def input_lettres(mot_deviner, dico_deviner, list_cacher, lettres_used, nbr_erreur):
    '''
    input_lettres
    dev: Joseph
    date: 2021-11-28 12:42:41

    Description:
    modifie l'affichage en fct des lettres données

    Parametres:
        mot_deviner [str] : mot a deviner
        dico_deviner [dict] : data du mot
        list_cacher [list] : presente les lettres trouver et non trouver
        lettres_used [list] : presente les lettres deja utilisées
        nbr_erreur [int] : compte le nbr d'erreur
    '''

    print('mot a deviner: ' + ' '.join(list_cacher))
    mot_donner = input("Entrez des lettres :")
    if not mot_donner.isalpha() or mot_donner == '':
        print('Erreur. ' + " Veuillez rentrer que des lettres")
        mot_donner = ''
        input_lettres(mot_deviner, dico_deviner,
                      list_cacher, lettres_used, nbr_erreur)
    else:
        dico_deviner, list_cacher, lettres_used, nbr_erreur = fctp.verif_lettre(
            mot_donner, dico_deviner, list_cacher, lettres_used, nbr_erreur)
        mot_donner = ''
        #print("mot a trouver: ", ''.join(list_cacher))
        print('lettres utiliser: ', ''.join(lettres_used))
        print("nombre d'erreur: ", nbr_erreur,
              'Il vous reste ', 12-nbr_erreur, 'essai.')
        print('\n')
    # win or loose:
    w_or_l = fctp.win_or_loose(dico_deviner, nbr_erreur)
    if w_or_l == True:
        print('Bravo', 'Vous avez gagnez! Le mot à deviner était: ',
              mot_deviner.upper(), '. Bien jouer!')
        restart = input('Voulez vous rejouer?  YES/NO : ')
        while fctp.verif_restart(restart) == False:
            restart = input('Voulez vous rejouer?  YES/NO : ')
        fctp.replay(restart)

    elif w_or_l == False:
        print('Perdu', 'Le mot a deviner était: ',
              mot_deviner.upper(), '. \n Dommage!')
        restart = input('Voulez vous rejouer?  YES/NO : ')
        while fctp.verif_restart(restart) == False:
            restart = input('Voulez vous rejouer?  YES/NO : ')
        fctp.replay(restart)
    else:
        input_lettres(mot_deviner, dico_deviner,
                      list_cacher, lettres_used, nbr_erreur)


mot_deviner, dico_deviner, list_cacher = choix_difficulte()
input_lettres(mot_deviner, dico_deviner, list_cacher, lettres_used, nbr_erreur)
