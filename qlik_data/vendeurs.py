import pandas as pd
import random
import os

# Dictionnaire ville -> code postal
ville_code_postal = {
    'Paris': '75000',
    'Lyon': '69000',
    'Marseille': '13000',
    'Toulouse': '31000',
    'Bordeaux': '33000',
    'Nice': '06000',
    'Lille': '59000',
    'Nantes': '44000',
    'Strasbourg': '67000',
    'Rennes': '35000'
}

# Zones à dupliquer
zones = [60, 90, 120]

# Liste des villes
villes = list(ville_code_postal.keys())

# Génération des vendeurs
vendeurs = []

for i in range(1, 11):
    vendeur_id = f"V{i:03d}"
    nom = f"Vendeur_{i}"
    nb_villes = random.choice([1, 2])
    villes_assignées = random.sample(villes, nb_villes)

    for ville in villes_assignées:
        code_postal = ville_code_postal[ville]
        nb_points = random.randint(3, 6)

        # Coordonnées clients (polygone simplifié)
        coords = [[[[
            round(random.uniform(-1.0, 5.0), 5),
            round(random.uniform(43.0, 50.0), 5)
        ] for _ in range(nb_points)]]]
        # Fermeture du polygone
        coords[0][0].append(coords[0][0][0])

        # Répéter pour chaque zone
        for zone in zones:
            vendeurs.append({
                "id": vendeur_id,
                "nom": nom,
                "ville": ville,
                "code_postal": code_postal,
                "zone": zone,
                "coordonnees": str(coords)
            })

# Création du DataFrame
df = pd.DataFrame(vendeurs)

# Sauvegarde avec chemin explicite
file_path = "/Users/mamoudou/Developer/Python/Internship/TimeTravel/frankfort/qlik_data/vendeurs_coordonnees.xlsx"
df.to_excel(file_path, index=False)

print("✅ Fichier enregistré ici :", os.path.abspath(file_path))
