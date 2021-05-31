import requests
import json
from datetime import datetime

timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

BASE = "http://localhost:5000/" 

#Inserer une donnée
print("Insérer une donnée :")
response = requests.put(BASE + "flaskAPI/sensordata/", {"id": "123", "timestamp": timestamp, "temperature": 21, "pressure": 1011, "humidity": 204})
print(response.json())
print(type(response.json()))
#retourne un type <class 'dict'>
id = response.json()['id']
print(id)
input()

#Afficher toutes les données
print("Afficher toutes les données :")
response = requests.get(BASE + "flaskAPI/sensordata/")
print(response.json())
input()

#Chercher une donnée
print("Chercher la donnée :")
response = requests.get(BASE + "flaskAPI/sensordata/" + id)
print(response.json())
input()

#Modifier une donnée
#print("Modifier la donnée :")
#response = requests.patch(BASE + "pigarden/" + id, {"timestamp": timestamp, "temperature": 81, "pressure": 1032, "humidity": 215})
#print(response.json())
#input()

#Supprimer une donnée
print("Supprimer la donnée :")
response = requests.delete(BASE + "flaskAPI/sensordata/" + id)
print(response)
