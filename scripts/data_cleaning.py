import pandas as pd

def clean_data(input_path, output_path):
    # Lire les données
    df = pd.read_csv(input_path)
    
    # Convertir la colonne Date en datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    
    # Vérifier les valeurs manquantes
    if df.isnull().sum().any():
        df = df.dropna()
    
    # Sauvegarder les données nettoyées
    df.to_csv(output_path, index=False)
    print(f"Données nettoyées sauvegardées dans {output_path}")

if __name__ == "__main__":
    input_path = '../data/raw/fake_data.csv'
    output_path = '../data/processed/cleaned_data.csv'
    clean_data(input_path, output_path)
