import json

with open('mot.json', 'r') as file:
    data=file.read()
    
dict_mots=json.loads(data)
print(dict_mots)
