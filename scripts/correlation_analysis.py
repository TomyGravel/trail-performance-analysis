import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(input_path, output_path_corr, output_path_heatmap):
    # Lire les données avec PF calculé
    df = pd.read_csv(input_path)
    
    # Sélectionner les colonnes nécessaires
    columns = ['Durée (heures)', 'Distance (km)', 'Dénivelé (m)', 
               'FC Moyenne (bpm)', 'VFC (ms)', 'Sommeil (h)', 
               'Qualité Sommeil (1-10)', 'Nutrition (1-10)', 'Hydratation (L)', 'PF Calculé']
    
    data = df[columns]
    
    # Calculer la matrice de corrélation de Pearson
    corr_matrix = data.corr(method='pearson')
    
    # Sauvegarder la matrice de corrélation
    corr_matrix.to_csv(output_path_corr)
    print(f"Matrice de corrélation sauvegardée dans {output_path_corr}")
    
    # Créer une heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Heatmap des Corrélations de Pearson')
    plt.tight_layout()
    plt.savefig(output_path_heatmap)
    plt.close()
    print(f"Heatmap de corrélation sauvegardée dans {output_path_heatmap}")

if __name__ == "__main__":
    input_path = '../data/processed/data_with_pf.csv'
    output_path_corr = '../data/processed/correlation_matrix.csv'
    output_path_heatmap = '../data/processed/correlation_heatmap.png'
    correlation_analysis(input_path, output_path_corr, output_path_heatmap)
