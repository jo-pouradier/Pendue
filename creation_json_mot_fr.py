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
for diff in range(11):
    a = []
    for mot in mots:
        mot = mot.strip('\n').lower()
        if len(mot) == diff:
            a.append(mot)
            a.sort()
    dico[str(diff)] = a
json.dump(dico, new_js)
new_js.close()
