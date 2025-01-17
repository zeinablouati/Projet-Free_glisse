import pandas as pd

# Liste des fichiers CSV
fichiers = [
    r"C:\Users\MSI\Desktop\hexagone\bigdata\Projet-Free_glisse\freeglisse_catalog.csv",
    r"C:\Users\MSI\Desktop\hexagone\bigdata\Projet-Free_glisse\freeglisse_reviews.csv",
    r"C:\Users\MSI\Desktop\hexagone\bigdata\Projet-Free_glisse\freeglisse_stocks.csv"
]

for fichier in fichiers:
    try:
        # Charger le fichier CSV avec le séparateur '|'
        df = pd.read_csv(fichier, sep='|', on_bad_lines='skip') 
        
        # Supprimer les lignes où au moins une colonne contient une valeur nulle ou vide
        df = df.dropna(how='any')  # Suppression des lignes avec des NaN
        df = df.loc[~(df.astype(str).apply(lambda x: x.str.strip()).eq('').any(axis=1))]  # Suppression des lignes avec cellules vides ou espaces
        
        # Enregistrer le fichier modifié
        fichier_modifie = fichier.replace(".csv", "____modifié.csv")
        df.to_csv(fichier_modifie, index=False, sep='|')
        print(f"Toutes les lignes avec des valeurs nulles ou vides ont été supprimées dans le fichier {fichier_modifie}.")
    
    except Exception as e:
        print(f"Erreur avec le fichier {fichier}: {e}")
