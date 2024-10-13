import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_pf_over_time(input_path, output_path_pf_plot):
    # Lire les données avec PF calculé
    df = pd.read_csv(input_path)
    
    # Convertir la colonne Date en datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    
    # Tracer le PF au fil du temps
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['PF Calculé'], marker='o', linestyle='-', color='b')
    plt.title('Paramètre Global de Forme (PF) sur 10 Jours')
    plt.xlabel('Date')
    plt.ylabel('PF Calculé')
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path_pf_plot)
    plt.close()
    print(f"Graphique du PF sur le temps sauvegardé dans {output_path_pf_plot}")

def plot_correlation_heatmap(input_path_corr, output_path_heatmap):
    # Lire la matrice de corrélation
    corr_matrix = pd.read_csv(input_path_corr, index_col=0)
    
    # Créer une heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Heatmap des Corrélations de Pearson')
    plt.tight_layout()
    plt.savefig(output_path_heatmap)
    plt.close()
    print(f"Heatmap de corrélation sauvegardée dans {output_path_heatmap}")

if __name__ == "__main__":
    # Plot PF over time
    input_path = '../data/processed/data_with_pf.csv'
    output_path_pf_plot = '../data/processed/pf_over_time.png'
    plot_pf_over_time(input_path, output_path_pf_plot)
    
    # Plot Heatmap
    input_path_corr = '../data/processed/correlation_matrix.csv'
    output_path_heatmap = '../data/processed/correlation_heatmap.png'
    plot_correlation_heatmap(input_path_corr, output_path_heatmap)
