import json

# on prend tout les mots du fichier
file = open('liste_francais_sans-accent.txt', 'r')
mots = file.readlines()
file.close()

# on supprime les mots du fichier
new_js = open('mots_fr.json', 'r+')
new_js.seek(0)
new_js.truncate()
new_js.close()

# on reprend les mots pour les mettres dans le json
new_js = open('mots_fr.json', 'w')
dico = {}
for diff in range (12):
    dico[str(diff)]=[]
for diff in range(12):
    for mot in mots:
        if ' ' in mot:
            pass
        else:
            mot = mot.strip('\n').lower()
            if len(mot) == diff:
                dico[str(diff)].append(mot)
                dico[str(diff)].sort()
            if len(mot)>=11:
                dico['11'].append(mot)
json.dump(dico, new_js)
new_js.close()
