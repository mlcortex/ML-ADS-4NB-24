import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL do dataset Wine
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

# Nome das colunas em português BR
column_names_pt_br = [
    'classe',
    'alcool',
    'acido_malico',
    'cinzas',
    'alcalinidade_de_cinzas',
    'magnesio',
    'fenois_totais',
    'flavanoides',
    'fenois_nao_flavanoides',
    'proantocianinas',
    'intensidade_de_cor',
    'matiz',
    'od280_od315_de_vinhos_diluidos',
    'prolina'
]

# Ler o arquivo CSV com as colunas especificadas, definindo a coluna 'classe' como object
vinhos = pd.read_csv(url, names=column_names_pt_br, dtype={'classe': object})

# 1. Análise Exploratória de Variáveis

# Contagem das diferentes classes
print("Contagem das classes:")
print(vinhos['classe'].value_counts())
print("\n")

# Estatísticas descritivas para as colunas especificadas
colunas_analise = ['alcool', 'acido_malico', 'magnesio', 'matiz']
for coluna in colunas_analise:
    print(f"Estatísticas descritivas para {coluna}:")
    print(vinhos[coluna].describe())
    print("\n")

# 2. Criação de Boxplots

plt.figure(figsize=(15, 10))
for i, coluna in enumerate(['magnesio', 'prolina', 'cinzas', 'alcool'], 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x=vinhos[coluna])
    plt.title(f'Boxplot de {coluna}')
plt.tight_layout()
plt.show()

# 3. Boxplots Segregados por Classe

colunas_boxplot = ['magnesio', 'fenois_totais', 'acido_malico', 'alcool']
for coluna in colunas_boxplot:
    plt.figure(figsize=(10, 6))
    vinhos.boxplot(column=coluna, by='classe')
    plt.title(f'Boxplot de {coluna} por Classe')
    plt.suptitle('')  # Remove o título automático
    plt.show()

# 4. Criação de Histograma

plt.figure(figsize=(10, 6))
plt.hist(vinhos['fenois_totais'], bins=10)
plt.title('Histograma de Fenóis Totais')
plt.xlabel('Fenóis Totais')
plt.ylabel('Frequência')
plt.show()

# Histograma da coluna fenois_totais, filtrando apenas a classe 3
plt.figure(figsize=(10, 6))
vinhos[vinhos['classe'] == '3']['fenois_totais'].hist(bins=10)
plt.title('Histograma de Fenóis Totais (Classe 3)')
plt.xlabel('Fenóis Totais')
plt.ylabel('Frequência')
plt.show()
