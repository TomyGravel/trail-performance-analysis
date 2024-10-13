import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_pf(input_path, output_path):
    # Lire les données nettoyées
    df = pd.read_csv(input_path)
    
    # Sélectionner les colonnes nécessaires
    columns = ['Durée (heures)', 'Distance (km)', 'Dénivelé (m)', 
               'FC Moyenne (bpm)', 'VFC (ms)', 'Sommeil (h)', 
               'Qualité Sommeil (1-10)', 'Nutrition (1-10)', 'Hydratation (L)']
    
    data = df[columns].copy()
    
    # Normaliser les données avec Min-Max Scaling
    scaler = MinMaxScaler()
    data_normalized = pd.DataFrame(scaler.fit_transform(data), columns=columns)
    
    # Inverser la normalisation pour FC Moyenne (une FC plus basse est meilleure)
    data_normalized['FC Moyenne (bpm)'] = 1 - data_normalized['FC Moyenne (bpm)']
    
    # Définir les poids (ajustés si nécessaire)
    weights = {
        'FC Moyenne (bpm)': 0.20,
        'VFC (ms)': 0.20,
        'Sommeil (h)': 0.20,
        'Qualité Sommeil (1-10)': 0.10,
        'Nutrition (1-10)': 0.10,
        'Hydratation (L)': 0.05,
        'Durée (heures)': 0.05,
        'Distance (km)': 0.05,
        'Dénivelé (m)': 0.05
    }
    
    # Calculer le PF
    data_normalized['PF'] = data_normalized.apply(lambda row: sum(row[col] * weight for col, weight in weights.items()), axis=1)
    
    # Ajouter le PF au DataFrame original
    df['PF Calculé'] = data_normalized['PF']
    
    # Sauvegarder les résultats
    df.to_csv(output_path, index=False)
    print(f"Paramètre Global de Forme (PF) calculé et sauvegardé dans {output_path}")

if __name__ == "__main__":
    input_path = '../data/processed/cleaned_data.csv'
    output_path = '../data/processed/data_with_pf.csv'
    calculate_pf(input_path, output_path)
