import pandas as pd
import random

# Charger le CSV initial
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

# Liste pour stocker toutes les nouvelles lignes
nouveau_data = []

# Parcours ligne par ligne
for index, row in df.iterrows():
    ville = row["City"]
    # Générer entre 2 et 9 vendeurs par ville
    nb_vendeurs = random.randint(2, 9)
    
    for i in range(1, nb_vendeurs + 1):
        vendeur = f"V_{ville}_{i}"
        fonction = random.choice(fonctions_it)
        
        # On peut garder toutes les colonnes initiales + fonction et vendeur
        nouvelle_ligne = row.to_dict()
        nouvelle_ligne["Vendeur"] = vendeur
        nouvelle_ligne["Fonction"] = fonction
        
        # Ajouter cette nouvelle ligne à la liste
        nouveau_data.append(nouvelle_ligne)

# Créer un nouveau DataFrame à partir des lignes générées
df_vendeurs = pd.DataFrame(nouveau_data)

# Sauvegarder dans un nouveau CSV
df_vendeurs.to_csv("data_test_qlik_avec_vendeurs.csv", index=False)

print("Fichier CSV mis à jour avec les vendeurs et fonctions créés.")