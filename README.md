# 📽️ Análise de Filmes - IMDb Top 1000 🎬

Bem-vindo ao repositório de análise dos 1000 filmes mais bem avaliados no IMDb! ✨ Aqui você encontrará o código utilizado para analisar as informações dos filmes e gerar insights interessantes. 💡

## 🔍 Sobre o Projeto

Este projeto utiliza um dataset com os **1000 filmes mais populares do IMDb**, e realiza uma análise dos seguintes aspectos:

- **Distribuição das notas**: Como as avaliações dos filmes estão distribuídas.
- **Quantidade de filmes por gênero**: Quais são os gêneros mais populares.
- **Duração média dos filmes**: Qual o tempo médio dos filmes do top 1000.
- **Classificação dos filmes**: Quantos filmes possuem classificações como PG, R, etc.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
  - **Pandas** 📊 para análise de dados
  - **Matplotlib** 🎨 para gráficos
  - **Seaborn** 🌈 para visualizações avançadas
- **CSV** 🗂️ para armazenar e processar os dados

## 📂 Como Rodar o Projeto

1. **Clonar o repositório**:
   - Abra seu terminal e execute:
     ```
     git clone https://github.com/VictorJeremias/AED-IMDb.git
     ```

2. **Instalar as dependências**:
   - Crie um ambiente virtual:
     ```
     python -m venv env
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```
       .\env\Scripts\activate
       ```
     - No macOS/Linux:
       ```
       source env/bin/activate
       ```
   - Instale as bibliotecas necessárias:
     ```
     pip install -r requirements.txt
     ```

3. **Colocar o arquivo CSV**:
   - Coloque o arquivo `IMDB_top_1000.csv` na pasta `./data/` (se não houver a pasta, crie-a).

4. **Rodar o código**:
   - Execute o código Python:
     ```
     AED-IMDb.py
     ```

## 📊 Análises Realizadas

- **Distribuição das Notas**: Um gráfico mostrando como as avaliações dos filmes estão distribuídas.
- **Gêneros mais Populares**: Quantos filmes existem em cada gênero?
- **Duração Média dos Filmes**: Qual é a duração média dos filmes listados no top 1000?
- **Correlação de Notas e Metascore**: Existe uma relação entre a pontuação do IMDb e a pontuação do Metascore?

## 📈 Visualizações

Veja as visualizações geradas pelo código:

1. **Distribuição das Notas dos Filmes**
2. **Quantidade de Filmes por Gênero**
3. **Quantidade de Filmes por Classificação**
4. **Tempo Médio de Duração dos Filmes**



🎬 Divirta-se explorando os filmes mais populares e suas análises! 🚀
