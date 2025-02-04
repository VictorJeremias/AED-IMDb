# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Verificando se a pasta 'data' existe, se não, cria a pasta
if not os.path.exists('./data'):
    os.makedirs('./data')

# Caminho para o arquivo CSV
file_path = './data/IMDB_top_1000.csv'  # Caminho relativo para o arquivo CSV

# Carregando o dataset do IMDb
df = pd.read_csv(file_path)

# Exibindo as primeiras linhas do dataset
print(df.head())

# Informações gerais sobre os dados
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Verificando valores nulos
print(df.isnull().sum())

# Visualizando a distribuição das notas dos filmes
plt.figure(figsize=(8,5))
sns.histplot(df['Rate'], bins=30, kde=True) 
plt.title('Distribuição das Notas dos Filmes')
plt.xlabel('Nota IMDb')
plt.ylabel('Frequência')
plt.show()

# Contagem de filmes por gênero
plt.figure(figsize=(12,6))
df['Genre'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Quantidade de Filmes por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.show()


# Analisando a quantidade de filmes por classificação
print("Quantidade de Filmes por Classificação:")
print(df['Certificate'].value_counts())

# Analisando o tempo médio de duração dos filmes
df['Duration'] = df['Duration'].str.replace(' min', '').astype(float)  # Remove a string 'min' e converte para float
print(f'Duração média dos filmes: {df["Duration"].mean()} minutos')


# Salvando o dataset processado
df.to_csv('./data/imdb_dataset_processado.csv', index=False)

print("Análise do IMDb concluída! 🚀")
