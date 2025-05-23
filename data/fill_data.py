import pandas as pd
import random

# Charger les données d’origine
df = pd.read_csv("data_test_qlik.csv")

fonctions_it = [
    "Matériel informatique",
    "Logiciels",
    "Services cloud",
    "Solutions réseau",
    "Équipements télécom",
    "Cybersécurité",
    "Périphériques (claviers, souris, écrans)",
    "Smartphones et tablettes",
    "Accessoires gaming",
    "Services de maintenance IT",
    "Solutions SaaS",
    "Consultants IT",
    "Licences logiciels",
    "Solutions de stockage",
    "Équipements serveurs"
]

# Générer les vendeurs
vendeur_data = []

for index, row in df.iterrows():
    ville = row["City"]
    nb_vendeurs = random.randint(2, 9)
    
    for i in range(1, nb_vendeurs + 1):
        vendeur_nom = f"V_{ville}_{i}"
        fonction = random.choice(fonctions_it)
        new_row = row.to_dict()
        new_row["Vendeur"] = vendeur_nom
        new_row["Fonction"] = fonction
        vendeur_data.append(new_row)

df_vendeurs = pd.DataFrame(vendeur_data)
df_vendeurs.to_csv("data_test_qlik_avec_vendeurs.csv", index=False)

# Générer les clients
clients_data = []

vendeurs = df_vendeurs["Vendeur"].tolist()

# Choisir un vendeur qui aura exactement 100 clients
vendeur_avec_100 = random.choice(vendeurs)

for vendeur in vendeurs:
    nb_clients = 100 if vendeur == vendeur_avec_100 else random.randint(1, 50)
    
    for idx in range(1, nb_clients + 1):
        client_id = f"C_{vendeur}_{idx}"
        clients_data.append({
            "idVendeur": vendeur,
            "C_vendeur_idx": client_id
        })

df_clients = pd.DataFrame(clients_data)
df_clients.to_csv("customers.csv", index=False)

print("✅ Vendeurs et clients générés avec succès dans 'data_vendeurs.csv' et 'data_clients.csv'")