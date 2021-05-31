#~/FlaskAPI/test_auth.py

import requests
import json
from datetime import datetime

timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

BASE = "http://localhost:5000/" 

#Inserer une donnée
#print("Inscription :")
#response = requests.put(BASE + "flaskAPI/auth/signup/", {"email": "user@email.com", "password": "userpasswd"})
#print(response.json())
#input()

#Connexion
print("Connexion :")
response = requests.put(BASE + "flaskAPI/auth/login/", {"email": "user@email.com", "password": "userpasswd"})
print(response.json())
token = response.json()['token']
headers = {'Authorization':'Bearer ' + str(token)}
print(token)
input()

#Inserer une donnée
print("Insérer une donnée :")
response = requests.put(BASE + "flaskAPI/sensordata/", {"timestamp": timestamp, "temperature": 21, "pressure": 1011, "humidity": 204}, headers = headers)
print(response.json())
print(type(response.json()))
#retourne un type <class 'dict'>
id = response.json()['id']
print(id)
input()

#Chercher une donnée
print("Chercher la donnée :")
response = requests.get(BASE + "flaskAPI/sensordata/" + id, headers = headers)
print(response.json())
input()

#Supprimer une donnée
print("Supprimer la donnée :")
response = requests.delete(BASE + "flaskAPI/sensordata/" + id, headers={'Authorization': token})
print(response)
