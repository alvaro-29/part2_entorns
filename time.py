# time.py - Fet per Álvaro Gómez Fernández

# APARTAT 7. A):
import requests

# Coordenades de la ciutat (Barcelona en aquest exemple):
latitude = 41.3888
longitude = 2.159

# URL amb paràmetres
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m"
)

# Petició HTTP a l’API
response = requests.get(url)
data = response.json()

# Extracció de temperatures horàries
temperatures = data["hourly"]["temperature_2m"]

print("Temperatures horàries:", temperatures)


# APARTAT 7. B):
# Calcular màxima, mínima i mitjana
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print("Temperatura màxima:", max_temp)
print("Temperatura mínima:", min_temp)
print("Temperatura mitjana:", round(avg_temp, 2))


# APARTAT 7. C):
import json
from datetime import datetime

# Prepara les dades a guardar
resultats = {
    "data": datetime.now().strftime("%Y-%m-%d"),
    "max_temp": max_temp,
    "min_temp": min_temp,
    "avg_temp": round(avg_temp, 2)
}

# Nom del fitxer segons la data actual
nom_arxiu = f"temp_{datetime.now().strftime('%Y%m%d')}.json"

# Escriu el fitxer JSON
with open(nom_arxiu, "w") as f:
    json.dump(resultats, f, indent=4)

print(f"Fitxer creat: {nom_arxiu}")

# time.py - Fet per Álvaro Gómez Fernández